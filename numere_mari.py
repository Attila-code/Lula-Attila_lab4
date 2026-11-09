import os

def adunare(num1, num2):
    i = len(num1) - 1
    j = len(num2) - 1
    transport = 0
    rezultat = []

    while i >= 0 or j >= 0 or transport:
        c1 = int(num1[i]) if i >= 0 else 0
        c2 = int(num2[j]) if j >= 0 else 0

        suma = c1 + c2 + transport
        transport = suma // 10
        rezultat.append(str(suma % 10))

        i -= 1
        j -= 1

    return "".join(reversed(rezultat)).lstrip("0") or "0"

def inmultire(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"

    n, m = len(num1), len(num2)
    rez = [0] * (n + m)

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            produs = int(num1[i]) * int(num2[j]) + rez[i + j + 1]
            rez[i + j + 1] = produs % 10
            rez[i + j] += produs // 10

    text = "".join(map(str, rez)).lstrip("0")
    return text if text else "0"

def main():
    if not os.path.exists("numere.txt"):
        print("Eroare: Fisierul numere.txt nu exista!")
        return

    with open("numere.txt", "r", encoding="utf-8-sig") as f:
        linii = [linie.strip() for linie in f if linie.strip()]

    if len(linii) < 2:
        print("Eroare: numere.txt trebuie sa aiba cel putin doua numere!")
        return

    nr1, nr2 = linii[0].replace(" ", ""), linii[1].replace(" ", "")

    if not (nr1.isdigit() and nr2.isdigit()):
        print(f"Eroare: Fisierul contine caractere invalide -> '{nr1}' sau '{nr2}'")
        return

    print("Numar 1:", nr1)
    print("Numar 2:", nr2)
    print("Suma     :", adunare(nr1, nr2))
    print("Produsul :", inmultire(nr1, nr2))

if __name__ == "__main__":
    main()
