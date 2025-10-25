import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

r.setnx("fib:0", 0)
r.setnx("fib:1", 1)


def fib(n: int) -> int:
    if n < 0:
        raise ValueError("Error")

    key = f"fib:{n}"

    cached = r.get(key)
    if cached is not None:
        return int(cached)

    result = fib(n - 1) + fib(n - 2)

    r.set(key, result)

    return result


print(fib(10))
print(fib(50))
