def caesar(char, shift):
    if char.islower():
        return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    elif char.isupper():
        return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    else:
        return char
def encrypted(text):
    words = text.split()
    encrypted_words = []
    for word in words:
        shift = sum(1 for c in word if c.isalpha())
        encrypted_word = ''
        for char in word:
            encrypted_word += caesar(char, shift)
        encrypted_words.append(encrypted_word)
    return ' '.join(encrypted_words)

print(encrypted(input))
