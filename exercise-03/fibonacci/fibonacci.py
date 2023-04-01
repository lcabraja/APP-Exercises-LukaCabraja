import time

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def generate(n):
    return list(fibonacci_generator(n))

def measure_duration(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    duration = end_time - start_time
    return result, duration

if __name__ == "__main__":
    n = 10
    fib_sequence, duration = measure_duration(generate, n)
    print(f"Fibonacci sequence of {n} numbers: {fib_sequence}")
    print(f"Duration of generate() call: {duration:.6f} seconds")
