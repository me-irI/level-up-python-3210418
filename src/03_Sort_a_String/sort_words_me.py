def sort_words(word):
    words = word.split(" ")
    n = len(words) - 1

    for _ in range(n):
        for i in range(n):
            if words[i].lower() > words[i + 1].lower():
                words[i], words[i + 1] = words[i + 1], words[i]
    return " ".join(words)


if __name__ == '__main__':
    print(sort_words('banana ORANGE apple'))  # apple banana ORANGE