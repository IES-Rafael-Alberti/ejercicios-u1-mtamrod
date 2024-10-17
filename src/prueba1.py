def n_mayor(n1, n2) -> int:
    if n1 == n2:
        return 0
    elif n1 > n2:
        return n1
    else:
        return n2

def main():
    n1 = 5
    n2 = 6
    print(n_mayor(n1, n2))


if __name__ == "__main__":
    main()