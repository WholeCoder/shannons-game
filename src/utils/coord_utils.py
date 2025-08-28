


def get_tiny_matrix(matrix, cell_size, shannon_speed):
    sub_div = cell_size // shannon_speed
    num_rows = len(matrix) * sub_div
    num_cols = len(matrix[0]) * sub_div
    tiny_matrix = [["null"] * num_cols for _ in range(num_rows)]
    tiny_r, tiny_c = 0, 0
    for row in matrix:
        for cell in row:
            if cell != "wall":
                cell = "null"
            for sx in range(sub_div):
                for sy in range(sub_div):
                    tiny_matrix[tiny_r + sx][tiny_c + sy] = cell
            tiny_c += sub_div
        tiny_r += sub_div
        tiny_c = 0
    return tiny_matrix

def precompute_matrix_coords(start_x, start_y, cell_size, num_rows, num_cols):
    matrix_coords = []
    col_start = start_y
    for _ in range(num_rows):
        row_start = start_x
        m = []
        for _ in range(num_cols):
            m.append((row_start, col_start))
            row_start += cell_size
        col_start += cell_size
        matrix_coords.append(m)
    return matrix_coords