import subprocess

def trace():
    subprocess.run(f"python -m trace --count -C /app/feedback /app/main.py", shell=True)

trace()
