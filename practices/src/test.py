def two_sum(numbers, target):
    _len = len(numbers)

    for start, item in enumerate(numbers):
        arr = numbers[start + 1 :]
        for index, item in enumerate(arr):
            if numbers[start] + arr[index] == target:
                return [start, index + start + 1]


print(two_sum([1, 2, 3], 4))
print(two_sum([1234, 5678, 9012], 14690))
print(two_sum([2, 2, 3], 4))


def count(s):
    res = {}
    for i in s:
        res[i] = res.get(i, 0) + 1
    return res


count("aba")


def is_valid_walk(walk):
    map = {"n": 0, "e": 0, "s": 0, "w": 0}
    if not walk:
        return True
    if len(walk) != 10:
        return False
    for i in walk:
        map[i] = map.get(i) + 1
    return map["n"] == map["s"] and map["e"] == map["w"]


res = is_valid_walk(["s", "e", "w", "n", "n", "w", "e", "w", "n", "s"])
print(res)

nums = [2, 3]


def find_it(seq):
    lst = list(filter(lambda x: seq.count(x) % 2 != 0, seq))
    return lst[0]


# print(find_it(nums))
print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))


import math


def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    # _sqrt = int(math.sqrt(sq))

    # if isinstance(_sqrt, int) and sq / _sqrt == _sqrt:
    #     return (_sqrt + 1) ** 2
    # else:
    #     return -1
    sqrt = sq**0.5
    if sqrt.is_integer():
        return (sqrt + 1) ** 2
    return -1


res = find_next_square(121)
# print(res)


def get_middle(s):
    _len = len(s) // 2
    return s[_len - 1 :: _len]


print(get_middle("test"))

print("==============")


def expanded_form(num):
    _num = str(num)
    _len = int(len(_num))
    res = []
    for index, item in enumerate(_num):
        if item == 0:
            continue
        res.append(str(int(item) * (10 ** (_len - index - 1))))

    return " + ".join(res)


res = expanded_form(12)
print(res)


def make_readable(seconds):
    # minute = int(seconds / 60) if seconds % 60 == 0 else seconds % 60
    # hour = int(seconds / (60 * 60))
    # second = (
    #     seconds - hour * 3600 - minute * 60
    #     if seconds > 60 * 60
    #     else seconds - minute * 60
    # )
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds %= 60
    # while seconds / 1:
    #     return 1

    return f"{hours:02}:{minutes:02}:{seconds:02}"


print(make_readable(86399))
print(make_readable(359999))

hex_string = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
]


def num2hex(n):
    return f"{format(hex_string[int(n / 16)] + hex_string[int(n % 16)]):02}"


def rgb(r, g, b):
    print(num2hex(r))
    return num2hex(r) + num2hex(g) + num2hex(b)


print(rgb(255, 255, 255))
print(rgb(0, 1, 2))


def zero(args=None):
    return 0 if args == None else args(0)


def one(args=None):
    return 1 if args == None else args(1)


def two(args=None):
    return 2 if args == None else args(2)


def three(args=None):
    return 3 if args != None else args(3)


def four(args=None):
    return 4 if args == None else args(4)


def five(args=None):
    return 5 if args == None else args(5)


def six(args=None):
    return 6 if args == None else args(6)


def seven(args=None):
    return 7 if args == None else args(7)


def eight(args=None):
    return 8 if args == None else args(8)


def nine(args=None):
    return 9 if args == None else args(9)


def plus(args):
    return lambda a: a + args


def minus(args):
    return lambda a: a - args


def times(args):
    return lambda a: a * args


def divided_by(args):
    return lambda a: a / args


print(five())
print(times(five()))
res = seven(times(five()))
print(res)

print("===============")


def fac(n):
    return fac(n - 1) * n if n > 2 else 1 if n == 2 else 1


def zeros(n):
    num = fac(n)
    print(num)
    _str = "".format(reversed(str(num)))
    print(_str)
    return _str.count("0", 0)


count = zeros(0)
print(count)
print(zeros(6))
