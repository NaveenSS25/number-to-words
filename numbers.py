
ONES = {0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"}
TENS = {0: "",
        1: "ten",
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety"}
SPECIALS = {0: "ten",
            1: "eleven",
            2: "twelve",
            3: "thirteen",
            4: "fourteen",
            5: "fifteen",
            6: "sixteen",
            7: "seventeen",
            8: "eighteen",
            9: "nineteen"}
MAGNITUDE = {0: "",
             1: "thousand",
             2: "million",
             3: "billion",
             4: "trillion",
             5: "quadrillion",
             6: "quintillion",
             7: "sextillion",
             8: "septillion",
             9: "octillion",
             10: "nonillion",
             11: "decillion"}


def number_to_words(n):
    if n == 0: return "zero"
    ns = str(abs(n))
    result = ""
    for mag, num in enumerate(splitapart(ns)):
        if num != 0:
            result = nw(num) + " " + MAGNITUDE[mag] + ", " + result
    if n < 0: result = "negative " + result
    return result.rstrip(" -,")


def splitapart(ns):
    while len(ns) % 3 > 0:
        ns = "0" + ns
    num = [int(ns[i:i + 3]) for i in range(0, len(ns), 3)]
    return num[::-1]


def nw(n):
    ns = str(n)
    res = ""
    if len(ns) == 1:
        return ONES[n]
    elif len(ns) == 2:
        if ns[0] == "1":
            res = SPECIALS[n % 10]
        else:
            res = TENS[n / 10] + "-" + ONES[n % 10]
    elif len(ns) == 3:
        res = ONES[n / 100] + " hundred " + nw(n % 100)
    return res.rstrip(" -,")

