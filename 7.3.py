class Cell:

    def __init__(self, cells_count):
        self.cells_count = cells_count

    def __add__(self, other):
        new_cell = self.cells_count + other.cells_count
        return new_cell

    def __sub__(self, other):
        if self.cells_count - other.cells_count > 0:
            new_cell = self.cells_count - other.cells_count
            return new_cell
        else:
            print('Вычитание данных двух клеток невозможно!')

    def __mul__(self, other):
        new_cell = self.cells_count * other.cells_count
        return new_cell

    def __truediv__(self, other):
        new_cell = self.cells_count // other.cells_count
        return new_cell

    def make_order(self, cells_in_row):
        var1 = self.cells_count // cells_in_row
        var2 = self.cells_count % cells_in_row

        container = ('* ' * cells_in_row + '\n\n') * var1

        if var2 != 0:
            container += '* ' * var2

        return container


cell1 = Cell(17)
cell2 = Cell(13)

our_new_cell = cell1 * cell2
print(our_new_cell)

cell3 = Cell(our_new_cell)
print(cell3.make_order(5))
