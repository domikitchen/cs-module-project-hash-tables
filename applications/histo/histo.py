# Your code here

f = open('robin.txt', 'r')

f = f.read()
f = f.lower()

wordies = {}
thisissobadandinefficient = {}

chars = '":;,.-+=/\|[]{}()*^&'
for baddy in chars:
    f = f.replace(baddy, '')


for word in f.split():
    if word in wordies.keys():
        haskdfjKAJKLJF = wordies.get(word)
        wordies[word] = haskdfjKAJKLJF + 1

    else:
        wordies[word] = 1


def sort_this_heccing_stuff(c):
    nummy = 0
    count = 0
    phing = ""
    heckingHASHES = ""

    if c == 0:
        for i in thisissobadandinefficient:
            print(f'{i.ljust(17)}{thisissobadandinefficient[i]}')

    else:
        for thing in wordies:
            if wordies[thing] > nummy:
                nummy = wordies[thing]
                phing = thing
        
        while count < nummy:
            count += 1
            heckingHASHES = f'{heckingHASHES}#'

        thisissobadandinefficient[phing] = heckingHASHES
        del wordies[phing]
        return sort_this_heccing_stuff(c - 1)

    return 'hecc'

print(sort_this_heccing_stuff(len(wordies)))