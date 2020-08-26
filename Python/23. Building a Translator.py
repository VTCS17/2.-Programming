def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "BUNNY"
            else:
                    translation = translation + "bunny"
        else:
            translation = translation + letter
    return translation

phrase = input("Enter a phrase")
print(translate(phrase))
