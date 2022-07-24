import sys
from modules.Cell import Cell

VALUE_LIST = [28, 34, 6, 20, 7, 89, 34, 18, 29, 51]

def create_cells_based_on_value_list(value_list):
    if len(value_list) == 0:
        return []
    cells = []
    start_ptr = Cell(-1)
    current_cell = Cell(value_list[0])
    start_ptr.right_neighbor = current_cell
    current_cell.left_neighbor = start_ptr
    cells.append(current_cell)
    for i in range(1, len(value_list)):
        cell = Cell(value_list[i])
        cells.append(cell)
        cell.left_neighbor = current_cell
        current_cell.right_neighbor = cell 
        current_cell = cell

    return cells, start_ptr 

def print_current_list(start_ptr):
    p = start_ptr.right_neighbor
    values = []
    while p:
        values.append(p.value)
        p = p.right_neighbor
    print(values)

def sort_cells(cells):
    need_to_sort = True 
    while need_to_sort:
        need_to_sort = False 
        for cell in cells:
            if cell.should_move_to_right():
                need_to_sort = True
                cell.move_to_right()
                # We start from only allow 1 cell move each time.
                # TODO: make this multi thread to allow cells moving
                # at the same time.
                break 

def main(argv):
    cells, start_ptr = create_cells_based_on_value_list(VALUE_LIST)
    sort_cells(cells)
    print_current_list(start_ptr)

if __name__ == "__main__":
    main(sys.argv[1:])