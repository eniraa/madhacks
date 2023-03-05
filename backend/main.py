import os
import shutil
from uuid import uuid4
import pathlib
import subprocess
import datetime

from flask import Flask, request


app = Flask(__name__)


@app.route("/execute", methods=["POST"])
def execute():
    dir = pathlib.Path(uuid4().hex)
    os.mkdir(dir)

    data = request.get_json()
    code: str = data.get("code", "")
    language: str = data.get("language", "")
    inputs: str = data.get("inputs", "")
    outputs: str = data.get("outputs", "")

    with open(dir / f"main.{language}", "w") as f:
        f.write(code)

    with open(dir / "Dockerfile", "w") as f:
        match language:
            case "py":
                f.write("FROM python:3.11\n")
                f.write("COPY . /app\n")
                f.write("WORKDIR /app\n")
                f.write("CMD python main.py\n")
            case _:
                shutil.rmtree(dir)
                return {"error": "language not supported"}

    try:
        proc = subprocess.run(
            f"docker build . -t {dir}",
            cwd=dir,
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=True,
        )
    except subprocess.CalledProcessError:
        shutil.rmtree(dir)
        return {"error": "docker build failed"}

    proc = subprocess.Popen(
        f"docker run -i --rm {dir}",
        cwd=dir,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

    now = datetime.datetime.now()
    out = proc.communicate(input=inputs.encode())[0].decode()
    elapsed = datetime.datetime.now() - now

    if out.rstrip("\n") != outputs:
        print(out, outputs)
        shutil.rmtree(dir)
        proc.kill()
        return {"error": "test failed"}

    proc.kill()

    shutil.rmtree(dir)
    return {"success": "tests passed", "time": elapsed.total_seconds()}


if __name__ == "__main__":
    app.run(debug=True, port=5000)
