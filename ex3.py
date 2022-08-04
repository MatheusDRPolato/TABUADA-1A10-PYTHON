#[0.5] Faça uma solução em Python que calcule as tabuadas de 1 até 10 (inclusive).
n1 = 1
n2 = 1
while n1 <= 11:
    print(f"{n2} x {n1} = {n1*n2}")
    n1 += 1
    if n1 == 11:
        n2 += 1
        n1 = 1
        if n2 == 11:
            break