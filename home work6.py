#1)
"""line, line_1 = set(input("==")), set(input("=="))
z =  line & line_1
print(z)"""
#2)
"""line, line_1 = set(range(3,1000,3)), set(range(5,1000,5))
line_2 = line & line_1

print(line_2)"""
#3)
"""units = {
    #0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'elven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifeteen',
    16: 'sixteen',
    17: 'seventenn',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'fourtty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousend',
    1_000_000: 'million',
    1_000_000_000: 'billion',
    'currency': 'dollar',
    'cents': 'cents'
}


output_on_display = ""
vvod = str(input("=="))

vvod = vvod.rjust(10, "0")
print(vvod)

part_1, part_2, part_3 = list(vvod[0:4]), list(vvod[4:7]), list(vvod[7:10])
print(part_1, part_2, part_3)
part_1[2] += "0"
part_2[1] += "0"
part_3[1] += "0"

hundreds = {"num_1": units[int(part_1[1])] + " " + units[100] if int(part_1[1]) > 0 else "",
            "num_2": units[int(part_2[0])] + " " + units[100] if int(part_2[0]) > 0 else "",
            "num_3": units[int(part_3[0])] + " " + units[100] if int(part_3[0]) > 0 else "",
            "num_4": units[int(part_1[0])] + " " + units[1_000_000_000] if int(part_1[0]) > 0 else "",

 }
output_on_display += hundreds["num_4"] + " "
output_on_display += hundreds["num_1"]
count = 0
for elem in part_1[2:4]:
    print(elem)

    count = 1 + count
    if int(elem) > 0:
       output_on_display += " " + units.get(int(elem), "") + " "
       if count == 2:
          output_on_display += units.get(1_000_000, "") + " "

output_on_display +=hundreds["num_2"]


for elem in part_2[1:3]:
    count = count - 1
    if int(elem) > 0:
       output_on_display += " " + units.get(int(elem), "") + " "
       if count == 0:
          output_on_display += units.get(1000, "") + " "

output_on_display += hundreds["num_3"]
for elem in part_3[1:3]:
    count = 1 + count
    if int(elem) > 0:
       output_on_display += " " + units.get(int(elem), "") + " "
       if count == 2:
          output_on_display += units.get('currency', "") + " "
print("You have:", output_on_display, sep="")"""

