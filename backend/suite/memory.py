import subprocess

def memory_profile():
    """Return a dict with memory usage information."""
    
    with open("/app/main.py") as f:
        code = f.read()
    
    new_code = f"""
import tracemalloc

tracemalloc.start()

{code}

with open("/app/feedback/memory.txt", "w") as f:
    peak = tracemalloc.get_traced_memory()[1]
    f.write(str(peak))

tracemalloc.stop()
"""

    with open("/app/main_mem.py", "w") as f:
        f.write(new_code)
    
    subprocess.run(f"cat /app/in | python3 /app/main_mem.py", shell=True)

memory_profile()
