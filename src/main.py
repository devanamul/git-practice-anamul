from datetime import date

from utils import add, subtract, multiply

if __name__ == "__main__":
    print("Anamul Hasan")
    print(date.today().isoformat())

    try:
        print(add(5, 3))
        print(subtract(5, 3))
        print(multiply(5, 3))
        print(add(5, "3"))
    except TypeError as error:
        print(f"Error: {error}")
