import sys


def ackermann(m: int, n: int) -> int:
    """
    contrato

    Calcula la funcion de Ackermann A(m, n).

    pre: m y n son numeros enteros no negativos
    post: devuelve n + 1 si m es 0; A(m - 1, 1) si n es 0; A(m - 1, A(m, n - 1)) en otro caso
    """
    if m == 0:
        return n + 1

    if n == 0:
        return ackermann(m - 1, 1)

    return ackermann(m - 1, ackermann(m, n - 1))


def main() -> None:
    sys.setrecursionlimit(5000)

    print("m\\n" + "".join(f"{n:6}" for n in range(8)))
    for m in range(4):
        print(f"{m:3}" + "".join(f"{ackermann(m, n):6}" for n in range(8)))


if __name__ == "__main__":
    main()
