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
                return {"success": False, "error": "language not supported"}
    
    os.mkdir(dir / "trace")

    with open(dir / "trace/Dockerfile", "w") as f:
        match language:
            case "py":
                f.write(f"FROM {dir}\n")
                f.write("CMD python -m trace --count -C ./test /app/main.py\n")
            case _:
                shutil.rmtree(dir)
                return {"success": False, "error": "language not supported"}

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

        proc = subprocess.run(
            f"docker build trace -t {dir}trace",
            cwd=dir,
            shell=True,
            stdin=subprocess.PIPE,
            # stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=True,
        )
    except subprocess.CalledProcessError:
        # shutil.rmtree(dir)
        return {"success": False, "error": "docker build failed"}

    # normal run
    proc = subprocess.Popen(
        f"docker run -i -v {dir.absolute()}/test:/app/test --rm {dir}",
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
        # shutil.rmtree(dir)
        proc.kill()
        return {"success": False, "error": "test failed"}

    proc.kill()

    # trace
    proc = subprocess.Popen(
        f"docker run -i -v {dir.absolute()}/test:/app/test --rm {dir}trace",
        cwd=dir,
        shell=True,
        stdin=subprocess.PIPE,
        # stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    proc.communicate(input=inputs.encode())

    # shutil.rmtree(dir)
    return {"success": True, "time": elapsed.total_seconds(), "cov": open(dir / "test/main.cover").read()}


if __name__ == "__main__":
    app.run(debug=True, port=5000)
