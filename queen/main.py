class Board:
    def __init__(self, size=8):
        self.size = size
        self.queens = []  # список позиций ферзей (row, col)

    def is_safe(self, row, col):
        """Проверка: можно ли поставить ферзя в (row, col)."""
        for qr, qc in self.queens:
            # одна строка, один столбец
            if qr == row or qc == col:
                return False
            # диагонали
            if abs(qr - row) == abs(qc - col):
                return False
        return True

    def place_queen(self, row, col):
        """Ставим ферзя в безопасное место."""
        self.queens.append((row, col))

    def remove_queen(self):
        """Удаляем последнего ферзя (нужно для бэктрекинга)."""
        self.queens.pop()

    def solve(self, row=0):
        """
        Рекурсивный backtracking:
        пытаемся поставить ферзя в каждую строку.
        """
        if row == self.size:
            return True  # все ферзи размещены

        for col in range(self.size):
            if self.is_safe(row, col):
                self.place_queen(row, col)
                if self.solve(row + 1):
                    return True
                self.remove_queen()

        return False  # нет решения для этой конфигурации

    def print_board(self):
        """Красивый вывод результата."""
        board = [["." for _ in range(self.size)] for _ in range(self.size)]
        for r, c in self.queens:
            board[r][c] = "Q"
        for row in board:
            print(" ".join(row))


class NQueens:
    def __init__(self, size=8):
        self.board = Board(size)

    def run(self):
        if self.board.solve():
            print("Ферзи расставлены успешно:\n")
            self.board.print_board()
        else:
            print("Решения нет.")


if __name__ == "__main__":
    game = NQueens(8)
    game.run()
