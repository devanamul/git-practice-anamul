from datetime import date

from utils import add, subtract, multiply, divide

if __name__ == "__main__":
    print("Anamul Hasan")
    print(date.today().isoformat())

    try:
        print(add(5, 3))
        print(subtract(5, 3))
        print(multiply(5, 3))
        print(divide(6, 3))
        print(divide(5, 0))
    except (TypeError, ZeroDivisionError) as error:
        print(f"Error: {error}")
