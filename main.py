# Cauã Pinheiro - 98319
# Emilly Oliveira - 97915
# Guilherme Richetto - 550407
# Vitor Manzoli - 551551

PUNCTUATION = "\"'.,;:!?()[]{}"


def read_files():
    with open("positivas.txt", "r") as file:
        positivas = file.read().splitlines()

    with open("negativas.txt", "r") as file:
        negativas = file.read().splitlines()

    with open("stopwords.txt", "r") as file:
        stopwords = file.read().splitlines()

    return positivas, negativas, stopwords


def tokenize(text, stopwords):
    words = text.split()

    tokens = []

    for w in words:
        token = w.lower()

        if w in stopwords or w in PUNCTUATION or w == "":
            continue

        if w[-1] in PUNCTUATION:  # Remove pontuação no final das palavras
            token = w[:-1]

        # Junta "não" com a próxima palavra, para que a próxima palavra seja negada
        if w == "não":
            token = f"{token} {words[words.index(w) + 1]}"
            words[words.index(w) + 1] = ""

        tokens.append(token)

    return tokens


def main():

    positivas, negativas, stopwords = read_files()

    text = input("Digite uma frase: ")

    tokens = tokenize(text, stopwords)

    print(f"Tokens: {tokens}")

    positivas_count = 0
    negativas_count = 0

    for w in tokens:
        if w in positivas:
            positivas_count += 1
        elif w in negativas:
            negativas_count += 1

    print(f"Positivas: {positivas_count}")
    print(f"Negativas: {negativas_count}")

    if positivas_count > negativas_count:
        print("A frase é positiva")
    elif negativas_count > positivas_count:
        print("A frase é negativa")
    else:
        print("A frase é neutra")


main()
