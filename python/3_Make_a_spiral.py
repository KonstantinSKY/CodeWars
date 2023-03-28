# 3 kyu
# Make a spiral

def spiralize(size):
    # Create the initial spiral with all elements set to 1
    spiral = [[1] * size for i in range(size)]

    # Initialize the current position and movement direction
    x, y = -1, 1
    del_x, del_y = 1, 0

    # Initialize variables for turning and controlling movement distance
    turn, koef = 0, 1
    finish = False

    # Helper function to check if the next position is valid
    def check_next():
        if 0 <= x + del_x * 2 < size and 0 <= y + del_y * 2 < size:
            # Check if the next position is not already visited and if it is safe to turn in the current direction
            return not (spiral[y + del_y * 2][x + del_x * 2] == 0 or (del_x == -1 and spiral[y][x - 1] == 0))
        return False

    # Main loop to generate the spiral
    while True:
        if check_next():
            # If the next position is valid, move to it and mark it as visited
            x += del_x
            y += del_y
            spiral[y][x] = 0
            finish = False
        else:
            # If the next position is not valid, finish if we've already tried turning in both directions
            if finish:
                return spiral
            finish = True
            # Turn in the other direction and update movement distances accordingly
            turn += 1
            if turn == 2:
                turn = 0
                koef *= -1
            del_x, del_y = abs(del_y) * koef, abs(del_x) * koef


if __name__ == "__main__":
    import codewars_test as test

    test.assert_equals(spiralize(5), [[1, 1, 1, 1, 1],
                                      [0, 0, 0, 0, 1],
                                      [1, 1, 1, 0, 1],
                                      [1, 0, 0, 0, 1],
                                      [1, 1, 1, 1, 1]])
    test.assert_equals(spiralize(8), [[1, 1, 1, 1, 1, 1, 1, 1],
                                      [0, 0, 0, 0, 0, 0, 0, 1],
                                      [1, 1, 1, 1, 1, 1, 0, 1],
                                      [1, 0, 0, 0, 0, 1, 0, 1],
                                      [1, 0, 1, 0, 0, 1, 0, 1],
                                      [1, 0, 1, 1, 1, 1, 0, 1],
                                      [1, 0, 0, 0, 0, 0, 0, 1],
                                      [1, 1, 1, 1, 1, 1, 1, 1]])
