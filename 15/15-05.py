def number_in_english(number):
    numbers = {
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        "10": "ten",
        "11": "eleven",
        "12": "twelve",
        "13": "thirteen",
        "14": "fourteen",
        "15": "fifteen",
        "16": "sixteen",
        "17": "seventeen",
        "18": "eighteen",
        "19": "nineteen",
        "20": "twenty",
        "30": "thirty",
        "40": "forty",
        "50": "fifty",
        "60": "sixty",
        "70": "seventy",
        "80": "eighty",
        "90": "ninety",
    }
    if number < 20:
        return numbers.get(str(number))
    if number < 100:
        n_ten = number // 10 * 10
        n_one = number % 10
        return numbers.get(str(n_ten)) + " " + numbers.get(str(n_one))
    n_hundred = number // 100
    n_ten = number % 100 // 10 * 10
    n_one = number % 100 % 10
    return numbers.get(str(n_hundred)) + " hundred and " + numbers.get(str(n_ten)) + " " + numbers.get(str(n_one))


print(number_in_english(125))