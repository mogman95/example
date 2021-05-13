print("example")
import string
alph = list(string.ascii_lowercase)
aword = ""
for letter in alph:
    aword = aword + letter
print(aword)

aword = ""
x = 0
while x < 26:
    aword = aword + alph[x]
    x += 1
print(aword)
