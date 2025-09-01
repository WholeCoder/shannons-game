

def __get_x_y(pos, num_rows, num_cols):
    x = pos[0]
    y = pos[1]
    if pos[0] < 0:
        x = num_rows + x
    if pos[1] < 0:
        y = num_cols + y
    return x, y

def get_coords_from_idx(shannon_pos, start_x, start_y, cell_w, cell_h, num_rows, num_cols):
    x, y = __get_x_y(shannon_pos, num_rows, num_cols)
    x_coord = start_x + (y * cell_w)
    y_coord = start_y + (x * cell_h)
    return x_coord, y_coord


def place_elements_offset(
    screen_width,
    screen_height,
    element_width,
    element_height,
    xoffset,
    yoffset):
    x = (screen_width - element_width) * xoffset
    y = (screen_height - element_height) * yoffset
    return x, y
    


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