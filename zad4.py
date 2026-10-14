def three(a:int,b:int,c:int) -> bool:
    return a+b >= c

czyWieksze = three(1,1,3)
if czyWieksze:
    print("2 pierwsze wieksze lub równe")
else:
    print("ostatnia większa")