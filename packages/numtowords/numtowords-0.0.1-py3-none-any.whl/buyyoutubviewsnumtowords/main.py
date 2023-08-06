units = [
"Zero",
"One",
"Two",
"Three",
"Four",
"Five",
"Six",
"Seven",
"Eight",
"Nine",
"Ten",
"Eleven",
"Twelve",
"Thirteen",
"Fourteen",
"Fifteen",
"Sixteen",
"Seventeen",
"Eighteen",
"Nineteen"
]
tens = [
"Zero",
"Ten",
"Twenty",
"Thirty",
"Forty",
"Fifty",
"Sixty",
"Seventy",
"Eighty",
"Ninety"
]

def ConvertNumberToWords(number = 0):
    if (number == 0): 
        return "zero"

    if (number < 0): 
        return "minus " + ConvertNumberToWords(abs(number))

    words = ""

    if (number // 1000000) > 0:
        words =words + ConvertNumberToWords(number // 1000000) + " million "
        number = number % 1000000

    if (number // 1000) > 0:
        words =words + ConvertNumberToWords(number // 1000) + " thousand "
        number = number % 1000

    if (number // 100) > 0: 
        words = words + ConvertNumberToWords(number // 100) + " hundred "
        number = number % 100

    if (number > 0):
        if (words != ""):
            words = words + "and "

    if (number < 20):
        words = words + units[number]
    else: 
        words = words + tens[number // 10]
        if (number % 10 > 0):
            words = words + "-" + units[number % 10]

    return words