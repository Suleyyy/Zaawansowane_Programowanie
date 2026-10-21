def find(lista: list, n: int) -> bool:
    return n in lista


res = find(range(0, 6), 7)
if res:
    print("Jest")
else:
    print("Nie ma")
