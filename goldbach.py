def este_prim(n):
    if n < 2:
        return False
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return False
    return True

def main():
    text = input("Introdu un numar par mai mare ca 2: ").strip()

    if not text.isdigit():
        print("Eroare: Te rog introdu un numar valid!")
        return

    n = int(text)

    if n <= 2:
        print("Eroare: Numarul trebuie sa fie mai mare decat 2!")
        return

    if n % 2 != 0:
        print("Eroare: Numarul trebuie sa fie par!")
        return

    print(f"Perechile Goldbach pentru {n} sunt:")
    for p in range(2, n // 2 + 1):
        q = n - p
        if este_prim(p) and este_prim(q):
            print(f"{n} = {p} + {q}")

if __name__ == "__main__":
    main()