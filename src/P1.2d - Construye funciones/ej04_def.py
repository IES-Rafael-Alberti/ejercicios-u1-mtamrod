def inputs():
    fahrenheit = float(input("Introduce una temperatura en grados Fahrenheit: "))

    return fahrenheit

def fahr_to_celsius():
    fahrenheit = inputs()
    celsius = (fahrenheit - 32) * (5 / 9)

    return celsius, fahrenheit


def main():
    celsius, fahrenheit = fahr_to_celsius()
    print(f"{celsius:.2f}ºC ({fahrenheit:.2f}ºF)")


if __name__ == "__main__":
    main()