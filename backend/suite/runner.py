import subprocess

subprocess.run(f"cat /app/in | python3 /app/main.py > /app/feedback/out", shell=True)

with open("/app/feedback/out") as f:
    received = f.read().rstrip("\n")

from timing import time
time()

from tracing import trace
trace()

from memory import memory_profile
memory_profile()

# from gpt import analyze
# analyze()

...
