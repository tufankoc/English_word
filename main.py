import string

regularized_word = []
counter = []
allliste = []
while 1<10:
    sentence = input("\nCümle Gir: ")
    liste = sentence.split(" ")
    for word in liste:
        allliste.append(word)
        if word not in string.punctuation:
            word = word.replace('.', ' ')
            word = word.strip()
            word = word.strip(',.“!*:;”') #karakter dizisinin baş ve sondaki boşluk karakterlerini siler.
            word = word.capitalize()
            regularized_word.append(word)

    for word in regularized_word:
        counter.append(regularized_word.count(word))
        if word not in regularized_word:
            regularized_word.append(word)
    regularized_word = list(set(regularized_word))

    sonuc = len(allliste) - len(regularized_word)
    print("\nToplam kelime  = " + str(len(allliste)) + "| Farklı kelime  = " + str(len(regularized_word)) + "| Tekrar eden kelime = " +  str(sonuc))
    print("Kelimeleeeeer\n")
    for word in regularized_word:
        print(word)



