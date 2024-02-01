def to_roman(num):
    output = ""
    roman_numerals = {
    'M' : 1000,
    'CM': 900,
    'D' : 500,
    'CD': 400,
    'C' : 100,
    'L' : 50,
    'XL': 40,
    'X' : 10,
    'IX': 9,
    'V' : 5,
    'IV': 4,
    'I' : 1,
    }
    
    for k in roman_numerals:
        while num >= roman_numerals[k]:
            output = output + k
            num = num - roman_numerals[k]
    return output

print(to_roman(944))

     