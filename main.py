def karatsuba(x: int, y: int) -> int:
    if x == 0 or y == 0:
        return 0

    sign = 1
    if x < 0:
        x, sign = -x, -sign
    if y < 0:
        y, sign = -y, -sign

    if x < 10 or y < 10:
        return sign * x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2
    power = 10 ** m

    a1, a0 = divmod(x, power)
    b1, b0 = divmod(y, power)

    z2 = karatsuba(a1, b1)
    z0 = karatsuba(a0, b0)
    z1 = karatsuba(a1 + a0, b1 + b0) - z2 - z0

    return sign * (z2 * 10 ** (2 * m) + z1 * power + z0)


def main():
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    print("Resultado:", karatsuba(x, y))


if __name__ == "__main__":
    main()