from ASCII import ascii


def double_encrypt(plaintext, key1, key2):
    return ascii(ascii(plaintext, key1), key2)


def double_decrypt(ciphertext, key1, key2):
    return ascii(ascii(ciphertext, key2, True), key1, True)


def middle_crack(plaintext, ciphertext):
    # 中间相遇攻击
    mid_texts = {}
    find_keys = []

    for key in range(pow(2, 16)):
        mid_texts[ascii(plaintext, key)] = key

    for key in range(pow(2, 16)):
        mid_text = ascii(ciphertext, key, True)
        if mid_text in mid_texts:
            find_keys.append([mid_texts[mid_text], key])

    return find_keys


if __name__ == '__main__':
    # 第四关：多重加密
    input_text = "Hello world!"

    # 双重加密
    key1 = 0b1111010101110000
    key2 = 12345

    ciphertext = double_encrypt(input_text, key1, key2)
    print(ciphertext)

    text = double_decrypt(ciphertext, key1, key2)
    print(text)

    # 中间相遇攻击
    print(middle_crack(input_text, ciphertext))

    # 三重加密
    key3 = 0x7F7F

    ciphertext = ascii(double_encrypt(input_text, key1, key2), key3)
    print(ciphertext)

    text = double_decrypt(ascii(ciphertext, key3, True), key1, key2)
    print(text)

