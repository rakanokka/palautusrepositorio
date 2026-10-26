class Calculator:
    def __init__(self, io):
        self._io = io

    def execute(self):
        while True:
            num1 = int(self._io.read("Luku 1:"))

            if num1 == -9999:
                return

            num2 = int(self._io.read("Luku 2:"))

            if num2 == -9999:
                return

            result = self._compute_sum(num1, num2)

            self._io.write(f"Summa: {result}")

    def _compute_sum(self, a, b):
        return a + b
