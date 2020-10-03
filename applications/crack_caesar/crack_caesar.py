# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

f = open('ciphertext.txt', 'r')

doc = []

commonLet = ["E", "T", "A", "O", "H", "N", "R", "I", "S", "D", "L", "W", "U", "G", "F", "B", "M", "Y", "C", "P", "K", "V", "Q", "J", "X", "Z"]

characters = {}

for letters in f.read():
  doc.append(letters)
  if letters.isupper() == True:
      if letters in characters.keys():
          numLet = characters.get(letters)
          characters[letters] = numLet + 1
      else:
          characters[letters] = 1

print(characters)

def sort_via_greatest(c):
    num = 0
    value = "thing"
    c -= 1
    
    if c == 0:
        return "\nhm\n"
    else:
        for l in characters:
            if isinstance(characters[l], int) == True:
                if characters[l] > num:
                    num = characters[l]
                    value = l
        characters[value] = commonLet[0]
        commonLet.pop(0)
        sort_via_greatest(c)

    return "\nDone? <_<\n"

print(sort_via_greatest(27))

print(characters)

def decode(s):
    r = ""

    for c in s:
        if c.isupper() == True:
            r += characters[c]
        else:
            r += c

    return r

print(decode(doc))