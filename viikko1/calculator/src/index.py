from console_io import ConsoleIO
from calculator import Calculator

def main():
    io = ConsoleIO()
    calc = Calculator(io)

    calc.execute()


if __name__ == "__main__":
    main()
