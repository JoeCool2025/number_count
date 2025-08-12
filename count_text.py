def count_to_num_as_text(input_num):
    num = int(input_num)
    text = ""
    
    if num >= 1000000:
        raise ValueError
    
    for i in range(1, num + 1):
        if i < 1000:
             text += _group_of_magnitude(i) + ", "
        elif i < 1000000:
            if i % 1000 == 0:
                text += _group_of_magnitude(i // 1000) + " thousand, "
            else:
                text += _group_of_magnitude(i // 1000) + " thousand " + _group_of_magnitude(i % 1000) + ", "

    return text[:-2] # Remove the trailing comma and space

def _group_of_magnitude(num):
    group = ""
    if 0 < num < 20:
            group += _convert_0_to_19(num)
    elif 20 <= num < 100:
        tens_digit = num // 10
        units_digit = num % 10
        group += f"{_convert_tens(tens_digit)} {_convert_0_to_19(units_digit)}"
    elif 100 <= num < 1000:
        hundreds_digit = num // 100
        if num % 100 >= 20:
            tens_digit = (num % 100) // 10
            units_digit = num % 10
            group += f"{_convert_hundreds(hundreds_digit)} {_convert_tens(tens_digit)} {_convert_0_to_19(units_digit)}"
        else:
            group += f"{_convert_hundreds(hundreds_digit)} {_convert_0_to_19(num % 100)}"
    
    if group[-1] == " ":
        group = group[:-1]
    return group

def _convert_0_to_19(num):
    num_words = {
        1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
        14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
        18: "eighteen", 19: "nineteen"
    }
    return num_words.get(num, "")

def _convert_tens(num):
    tens_words = {
        2: "twenty", 3: "thirty", 4: "forty", 5: "fifty",
        6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"
    }
    return tens_words.get(num, "")

def _convert_hundreds(num):
    hundreds_words = {
        1: "one hundred", 2: "two hundred", 3: "three hundred",
        4: "four hundred", 5: "five hundred", 6: "six hundred",
        7: "seven hundred", 8: "eight hundred", 9: "nine hundred"
    }
    return hundreds_words.get(num, "")