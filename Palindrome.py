def process_text(text):
    text = text.lower()
    forbidden = ("!", "@", "#")
    for i in forbidden:
        text = text.replace(i, "")
    return text

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    new = process_text(text)
    return process_text(text) == reverse(process_text(text))

something = input("Enter word: ")
if (is_palindrome(something)):
    print("You got a palindrome")
else:
    print("It is not a palindrome")
