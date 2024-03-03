def encrypt(key, message):
    alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha_lower = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for letter in message:
        if letter in alpha_upper:
            letter_index = (alpha_upper.find(letter) + key) % len(alpha_upper)
            result = result + alpha_upper[letter_index]
        elif letter in alpha_lower:
            letter_index = (alpha_lower.find(letter) + key) % len(alpha_lower)
            result = result + alpha_lower[letter_index]
        else:
            result = result + letter

    return result


print(encrypt(1, "The quick brown fox jumps over the lazy dog."))
