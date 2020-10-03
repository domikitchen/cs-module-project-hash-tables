def word_count(s):
    thing = {}
    doobleS = s.lower()
    chars = '":;,.-+=/\|[]{}()*^&'
    for baddy in chars:
        doobleS = doobleS.replace(baddy, '')


    for w in doobleS.split():
        if w in thing:
            num = thing.get(w)
            thing[w] = num + 1
        else:
            thing[w] = 1
            

    return thing


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))