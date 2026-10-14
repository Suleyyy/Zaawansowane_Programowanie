def parzysta(n: int) -> bool:
    return n % 2 == 0

n = parzysta(3)

if n:
    print("parzysta")
else:
    print("nieparzysta")