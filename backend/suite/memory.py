def memory_profile():
    """Return a dict with memory usage information."""
    
    with open("/app/main.py") as f:
        code = f.read()

    import tracemalloc

    tracemalloc.start()

    exec(code)

    with open("/app/feedback/memory.txt", "w") as f:
        peak = tracemalloc.get_traced_memory()[1]
        f.write(f"{peak}")
    
    tracemalloc.stop()
