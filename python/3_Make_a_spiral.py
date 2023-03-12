# 3 kyu
# Make a spiral

def spiralize(size):
    spiral = [[1] * size for i in range(size)]

    x, y = -1, 1
    del_x, del_y = 1, 0
    turn, koef = 0, 1
    finish = False

    def check_next():
        if 0 <= x + del_x * 2 < size and 0 <= y + del_y * 2 < size:
            return not (spiral[y + del_y * 2][x + del_x * 2] == 0 or (del_x == -1 and spiral[y][x - 1] == 0))
        return False

    while True:
        if check_next():
            x += del_x
            y += del_y
            spiral[y][x] = 0
            finish = False
        else:
            if finish:
                return spiral
            finish = True
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
