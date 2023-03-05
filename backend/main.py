import os
import shutil
from uuid import uuid4
import pathlib
import subprocess

from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/execute", methods=["POST"])
def execute():
    dir = pathlib.Path(uuid4().hex)
    os.mkdir(dir)

    data: dict = request.get_json()
    code: str = data.get("code", "")
    language: str = data.get("language", "")
    inputs: str = data.get("inputs", "")
    should_analyze: bool = data.get("analysis", False)

    print(language)
    # outputs: str = data.get("outputs", "")

    # """edge case when the code input is just empty lol"""
    # if not code:
    #     return {"Success": False, "Error": "Code is empty"}

    """only python support for now (without this, it throws errors for other langs)"""
    if language != "py":
        return {"success": False, "error": "Language not supported"}

    with open(dir / f"main.{language}", "w") as f:
        f.write(code)

    with open(dir / "in", "w") as f:
        f.write(inputs)

    # with open(dir / "out", "w") as f:
    #     f.write(outputs)

    for file in ["runner.py", "tracing.py", "timing.py", "memory.py", "gpt.py"]:
        with open(dir / file, "w") as f:
            with open(dir / ".." / "suite" / file) as f2:
                f.write(f2.read())

    with open(dir / "Dockerfile", "w") as f:
        match language:
            case "py":
                f.write("FROM python:3.11\n")
                f.write("RUN pip install openai\n")
                f.write("COPY . /app\n")
                f.write("WORKDIR /app\n")
                f.write(f"ENV ANALYZE={1 if should_analyze else 0}\n")
                f.write("CMD python runner.py\n")
            case _:
                shutil.rmtree(dir)
                return {"success": False, "error": "Language not supported"}

    try:
        subprocess.run(
            f"docker build . -t {dir}",
            cwd=dir,
            shell=True,
            stdin=subprocess.PIPE,
            # stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=True,
        )
    except subprocess.CalledProcessError:
        return {"success": False, "error": "Build failed"}

    # normal run
    try:
        subprocess.run(
            f"docker run -i -v {dir.absolute()}/feedback:/app/feedback --rm {dir}",
            cwd=dir,
            shell=True,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        return {
            "success": False,
            "error": "Run failed",
        }

    elapsed = float(open(dir / "feedback" / "time.txt").read())
    coverage = open(dir / "feedback" / "main.cover").read()
    output = open(dir / "feedback" / "out").read()
    memory = int(open(dir / "feedback" / "memory.txt").read())

    if should_analyze:
        analysis = open(dir / "feedback" / "analysis.txt").read().strip("\n")
    else:
        analysis = None

    shutil.rmtree(dir)
    return {
        "success": True,
        "time": elapsed,
        "coverage": coverage,
        "output": output,
        "memory": memory,
        "analysis": analysis,
    }


if __name__ == "__main__":
    app.run(debug=True, port=5000)
