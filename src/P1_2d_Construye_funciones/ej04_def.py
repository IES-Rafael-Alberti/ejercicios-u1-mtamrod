def fahr_to_celsius():
    fahrenheit = float(input("Introduce una temperatura en grados Fahrenheit: "))
    celsius = (fahrenheit - 32) * (5 / 9)

    return f"Son {celsius}ºC ({fahrenheit})"


def main():
    print(fahr_to_celsius())


if __name__ == "__main__":
    main()