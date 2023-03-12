#!/bin/python

def fib(num):
    x, y, an = 0, 1, abs(num) // 2
    if num % 2:
        for i in range(an): x, y = y, x + y
        return x ** 2 + y ** 2
    else:
        for i in range(an): x, y = y, x + y
        return (2 * y - x) * x if num > 0 else (x - 2 * y) * x


if __name__ == "__main__":
    import codewars_test as test  # pip install codewars-test-teey    - fork

    test.assert_equals(fib(0), 0)
    test.assert_equals(fib(1), 1)
    test.assert_equals(fib(2), 1)
    test.assert_equals(fib(3), 2)
    test.assert_equals(fib(4), 3)
    test.assert_equals(fib(5), 5)
    test.assert_equals(fib(1000),
                       43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875)