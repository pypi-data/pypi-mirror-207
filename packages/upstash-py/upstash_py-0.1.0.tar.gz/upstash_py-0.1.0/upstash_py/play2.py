def function(p1: str, p2: bool = False, *p3: int):
    print(p2)


function("a", "b", "c", "d", "e", "f", p2=True)
