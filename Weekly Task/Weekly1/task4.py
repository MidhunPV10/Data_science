length = int(input("Enter the length of identifiers : "))
chars = []
print("Enter",length,"characters:")
for i in range(length):
    ch = input("Character " + str(i+1) + ": ")
    chars.append(ch)
print("Valid Identifiers are:")
for i in range(length):
    for j in range(length):

            if i != j  :
                word = chars[i] + chars[j]
                if (word[0].isalpha() or word[0] == "_"):
                    valid = True
                    for ch in word:
                        if not (ch.isalpha() or ch.isdigit() or ch == "_"):
                            valid = False
                    if valid:
                        if word != "for" and word != "if" and word != "else" and word != "while":
                             print(word)

