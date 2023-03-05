import os
import subprocess

subprocess.run(f"cat /app/in | python3 /app/main.py > /app/feedback/out", shell=True)

with open("/app/feedback/out") as f:
    received = f.read().rstrip("\n")

# from timing import time
# time()
subprocess.run(f"cat /app/in | python3 /app/timing.py", shell=True)

# from tracing import trace
# trace()
subprocess.run(f"cat /app/in | python3 /app/tracing.py", shell=True)

# from memory import memory_profile
# memory_profile()
subprocess.run(f"cat /app/in | python3 /app/memory.py", shell=True)

if os.environ.get("ANALYZE", "0") == "1":
    from gpt import analyze
    analyze()
