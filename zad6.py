def duplikaty(l: list, l2: list) -> list:
    return [i**2 for i in set(l+l2)]

fusion = duplikaty([2,3,4], [3,4,5])
print(fusion)