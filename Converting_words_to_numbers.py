
def words_to_number(words):
    num_dict = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
        "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
        "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90, "hundred": 100, "thousand": 1000, "million": 1000000
    }

    # words = words.lower().replace("-,',\"", " ").split()  # Handle hyphenated words
    words = words.lower().replace('"', " ").replace("-", " ").replace(",", " ").replace("'", " ").replace(".", " ").replace("and", " ").replace("of", " ").replace("the", " ").replace("to", " ").replace("a", " ").replace("an", " ").split()
    total = 0
    current = 0

    for word in words:
        if word in num_dict:
            value = num_dict[word]
            if value < 100:  # Handling numbers
                current += value
            elif value == 100:  # Handling "hundred"
                current *= value
            elif value >= 1000:  # Handling "thousand", "million"
                total += current * value
                current = 0

    total += current
    return total

# Example Usage:
# test_cases = [
#     "three hundred thousand",
#     "one thousand two hundred",
#     "two million five hundred thousand",
#     "forty-two",
#     "nineteen",
#     "six hundred seventy-five",
#     "five thousand and sixty"
# ]
test_cases = input("Enter the text: ")
test_cases = [test_cases]

for case in test_cases:
    print(f"{case} -> {words_to_number(case)}")