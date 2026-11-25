def is_palindrome(text):
    text = text.replace(" ", "").replace("'", "").replace(".","").replace(",","").lower()
    right = -1
    palindrome = None

    for left in range(int(len(text)/ 2)):
        if text[left] != text[right]:
            print(f"text left: {text[left]} and text righ: {text[right]}")
            return False
        right -= 1

    return True



if __name__ == '__main__':
    print(is_palindrome('hello world'))  # false
    print(is_palindrome("Go hang a salami, I'm a lasagna hog."))  # true