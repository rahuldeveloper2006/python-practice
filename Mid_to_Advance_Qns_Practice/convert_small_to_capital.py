# wap to convert a sentence's all letters from small letter to capital letter

"""

letter = input("Enter a sentence : ")
result = ""
for char in letter:
    if 'a'<= char <= 'z':
        capital_let = chr((ord(char)-ord('a')) + ord('A'))
        result+=capital_let
    else:
        result+=char
print(result)

"""


# wap to convert capital to small

letter = input("Enter a sentence : ")
result = ""
for char in letter:
    if 'A'<= char <= 'Z':
        small_let = chr((ord(char)-ord('A')) + ord('a'))
        result+=small_let
    else:
        result+=char
print(result)