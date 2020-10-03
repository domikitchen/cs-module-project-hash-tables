def no_dups(s):
    existingWords = []
    reee = ""

    for w in s.split():
      if w not in existingWords:
        existingWords.append(w)

    for w in existingWords:
      if reee == "":
        reee = w
      else:
        reee = reee + " " + str(w)

    return reee
          

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
