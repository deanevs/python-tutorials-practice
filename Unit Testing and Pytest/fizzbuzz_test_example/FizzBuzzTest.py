import pytest


def fizzBuzz(value):
    if is_multiple(value, 3):
        if is_multiple(value, 5):
            return 'FizzBuzz'
        return 'Fizz'
    elif is_multiple(value, 5):
        return 'Buzz'
    return str(value)


def is_multiple(value, mod):
    return value % mod == 0


# create a utility function for test cases
def checkFizzBuzz(value, expected):
    ret_val = fizzBuzz(value)
    assert ret_val == expected


def test_canCallFizzBuzz():
    fizzBuzz(1)


def test_returns1with1passedin():
    checkFizzBuzz(1, '1')


def test_return2With2PassedIn():
    checkFizzBuzz(2, '2')


def test_returns_fizz_when_pass_in_3():
    checkFizzBuzz(3, 'Fizz')


def test_returns_buzz_when_pass_5():
    checkFizzBuzz(5, 'Buzz')


def test_multiple_3_fizz():
    checkFizzBuzz(6, 'Fizz')


def test_mult_10_return_buzz():
    checkFizzBuzz(10, 'Buzz')


def test_mul_3_5_fizzbuss():
    checkFizzBuzz(15, 'FizzBuzz')
