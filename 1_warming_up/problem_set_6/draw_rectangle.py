def get_rectangles():
    rectangles = []

    while True:
        rectangle_coords = input("Enter Rectangle Coords in Format [rowTL colTL rowBR colBR]: ")
        if rectangle_coords == ".":
            break
        rectangles.append(rectangle_coords)

    return rectangles


def get_max_rows(all_rectangles):
    rows = []
    for rectangle in all_rectangles:
        split_coords = rectangle.split()
        rows.append(int(split_coords[0]))
        rows.append(int(split_coords[2]))
    return max(rows)


def get_max_columns(all_rectangles):
    columns = []
    for rectangle in all_rectangles:
        split_coords = rectangle.split()
        columns.append(int(split_coords[1]))
        columns.append(int(split_coords[3]))
    return max(columns)


def generate_coords(rectangle_coords):
    coords = rectangle_coords.split()
    row_tl = int(coords[0])
    col_tl = int(coords[1])
    row_br = int(coords[2])
    col_br = int(coords[3])

    rectangle_top_left = (row_tl, col_tl)
    rectangle_top_right = (row_tl, col_br)
    rectangle_bottom_left = (row_br, col_tl)
    rectangle_bottom_right = (row_br, col_br)

    return rectangle_top_left, rectangle_top_right, rectangle_bottom_left, rectangle_bottom_right


def get_all_coords(all_rectangles):
    all_coords = set()

    for rectangle_coords in all_rectangles:
        top_left, top_right, bottom_left, bottom_right = generate_coords(rectangle_coords)
        for i in range(top_left[1], top_right[1] + 1):
            all_coords.add((top_left[0], i))
            all_coords.add((bottom_left[0], i))

        for i in range(top_left[0], bottom_left[0] + 1):
            all_coords.add((i, top_left[1]))
            all_coords.add((i, top_right[1]))

    return all_coords


def print_rectangles(all_rectangles, all_coords):
    max_rows = get_max_rows(all_rectangles)
    max_columns = get_max_columns(all_rectangles)

    for i in range(max_rows + 1):
        for j in range(max_columns + 1):
            message = "*" if (i, j) in all_coords else " "
            print(message, end="")
        print()


def draw_rectangles():
    all_rectangles = get_rectangles()
    all_coords = get_all_coords(all_rectangles)
    print_rectangles(all_rectangles, all_coords)


if __name__ == "__main__":
    draw_rectangles()
