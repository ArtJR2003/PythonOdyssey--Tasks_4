alphabet = ""
for i in range(65, 91):
    alphabet = alphabet + chr(i)
vowels = "aeouiAEOUI"
cons = ""
for i in alphabet:
    if i not in vowels:
        cons = cons + i
some_string = ""
some_string = input()
count_vowels = 0
count_cons = 0
for i in some_string:
    if i in vowels:
      count_vowels = count_vowels + 1
    elif i in cons:
      count_cons = count_cons + 1
print(i)
