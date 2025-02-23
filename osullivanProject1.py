import string

alpha = string.ascii_lowercase

#Keyword Encrypt/Decrypt Methods
def encryptKeyword(plaintext, keyword):

    keyword_usable = ""
    alphabet = ""
    ciphertext = ""

    for c in keyword:
        if c.isalpha() and c not in keyword_usable:
            keyword_usable += c

    for c in keyword_usable:
        alphabet += c

    for i in range(len(alpha)):
        if alpha[i] not in alphabet.lower():
            alphabet += alpha[i]

    for i in range(len(plaintext)):

        if plaintext[i].isalpha():

            if plaintext[i].isupper():
                value = ord(plaintext[i]) - 65
                ciphertext += alphabet[value].upper()

            else:
                value = ord(plaintext[i]) - 97
                ciphertext += alphabet[value].lower()

        else:
            ciphertext += plaintext[i]

    return ciphertext

def decryptKeyword(ciphertext, keyword):
    keyword_usable = ""
    alphabet = ""
    plaintext = ""

    for c in keyword:
        if c.isalpha() and c not in keyword_usable:
            keyword_usable += c

    for c in keyword_usable:
        alphabet += c

    for i in range(len(alpha)):
        if alpha[i] not in alphabet.lower():
            alphabet += alpha[i]

    for i in range(len(ciphertext)):
        value = 0
        for j in range(len(alphabet)):
            if alphabet[j].lower() == ciphertext[i].lower():
                value = j

        if ciphertext[i].isalpha():
            if ciphertext[i].isupper():
                plaintext += alpha[value].upper()
            else:
                plaintext += alpha[value].lower()
        else:
            plaintext += ciphertext[i]

    return plaintext

#Columnar Encrypt/Decrypt Methods
def encryptColumnar(plaintext, keyword):
    plaintext = plaintext.replace(" ", "_")
    keyword_length = len(keyword)

    columns = [[] for i in range(keyword_length)]

    for i,char in enumerate(plaintext):
        index = i % keyword_length
        columns[index].append(char)
        print(columns[index])

    sorted_keyword = sorted(range(keyword_length), key =lambda x: keyword[x].lower())

    ciphertext = ""
    for i in sorted_keyword:
        print(columns[i])
        ciphertext += "".join(columns[i])

    return ciphertext

def decryptColumnar(ciphertext, keyword):
    keyword_length = len(keyword)
    extra = len(ciphertext) % keyword_length
    rows = len(ciphertext)//keyword_length
#    print(rows)

    columns = [""] * keyword_length
    index = 0

    sorted_keyword = sorted(range(keyword_length), key=lambda x: keyword[x].lower())

    for i in sorted_keyword:
        if i < extra:
            columns[i] = ciphertext[index:index + rows + 1]
            index += rows + 1
        else:
            columns[i] = ciphertext[index:index +rows]
            index += rows

    plaintext = []

    for r in range(rows):
        for c in columns:
            plaintext.append(c[r])

    for j,c in enumerate(columns):
        if j < extra:
            plaintext.append(c[rows])

    return ''.join(plaintext).replace("_", " ")

# Vigenere Encrypt/Decrypt Methods
def encryptVigenere(plaintext, keyword):
    key_length = len(keyword)
    keyword_list = [c for c in keyword]
    plaintext_list = [c for c in plaintext]
    ciphertext = ""
    a = 0

    for i in range(len(plaintext_list)):
        if plaintext_list[i].isalpha():
            if plaintext_list[i].isupper():
                key_char = keyword_list[a % key_length].upper()
                # print(plaintext_list[i] + "; " + key_char)
                value = ((ord(plaintext_list[i])-65) + (ord(key_char)-65)) % 26
                ciphertext += chr(value + 65)
                a += 1
            else:
                key_char = keyword_list[a % key_length].lower()
                # print(plaintext_list[i] + "; " + key_char)
                value = ((ord(plaintext_list[i])-97) + (ord(key_char)-97)) % 26
                ciphertext += chr(value + 97)
                a += 1
        else:
            ciphertext += plaintext_list[i]

    return ciphertext

def decryptVigenere(ciphertext, keyword):
    key_length = len(keyword)
    keyword_list = [c for c in keyword]
    ciphertext_list = [c for c in ciphertext]
    plaintext = ''
    a = 0

    for i in range(len(ciphertext_list)):
        if ciphertext_list[i].isalpha():
            if ciphertext_list[i].isupper():
                key_char = keyword_list[a % key_length].upper()
                # print(ciphertext_list[i] + "; " + key_char)
                value = ((ord(ciphertext_list[i]) - 65) - (ord(key_char) - 65)) % 26
                plaintext += chr(value + 65)
                a += 1
            else:
                key_char = keyword_list[a % key_length].lower()
                # print(ciphertext_list[i] + "; " + key_char)
                value = ((ord(ciphertext_list[i]) - 97) - (ord(key_char) - 97)) % 26
                plaintext += chr(value + 97)
                a += 1
        else:
            plaintext += ciphertext_list[i]

    return plaintext

#main method
def main():

    encryptColumnar("encryption", "whale")

    # cipher_choice = input("Please select a cipher to apply: \n [1] Keyword Cipher \n [2] Columnar Cipher \n [3] Vigenere Cipher \n")
    # print(cipher_choice)
    #
    # if cipher_choice == "1":
    #     print("Keyword Cipher Chosen")
    #     mode = input("Please select \n [1] Encrypt \n [2] Decrypt \n")
    #     if mode == "1":
    #         keyword_keyword = input("Please provide a keyword: ")
    #         plaintext_keyword = input("Please provide a message to encrypt: ")
    #         print("Encrypting...")
    #         ciphertext_keyword = encryptKeyword(plaintext_keyword, keyword_keyword)
    #
    #         print(plaintext_keyword + "\n" + ciphertext_keyword)
    #     elif mode == "2":
    #         keyword_keyword = input("Please provide a keyword: ")
    #         ciphertext_keyword = input("Please provide a message to decrypt: ")
    #         print("Decrypting...")
    #         plaintext_keyword = decryptKeyword(ciphertext_keyword, keyword_keyword)
    #
    #         print(ciphertext_keyword + "\n" + plaintext_keyword)
    #     else:
    #         return
    # elif cipher_choice == "2":
    #     print("Columnar Cipher Chosen")
    #     mode = input("Please select \n [1] Encrypt \n [2] Decrypt \n")
    #     if mode == "1":
    #         keyword_columnar = input("Please provide a keyword: ")
    #         plaintext_columnar = input("Please provide a message to encrypt: ")
    #         print("Encrypting...")
    #         ciphertext_columnar = encryptColumnar(plaintext_columnar, keyword_columnar)
    #
    #         print(plaintext_columnar + "\n" + ciphertext_columnar)
    #     elif mode == "2":
    #         keyword_columnar = input("Please provide a keyword: ")
    #         ciphertext_columnar = input("Please provide a message to decrypt: ")
    #         print("Decyphering...")
    #         plaintext_columnar = decryptColumnar(ciphertext_columnar, keyword_columnar)
    #
    #         print(ciphertext_columnar + '\n' + plaintext_columnar)
    #     else:
    #         return
    # elif cipher_choice == "3":
    #     print("Vigenere Cipher Chosen")
    #     mode = input("Please select \n [1] Encrypt \n [2] Decrypt \n")
    #     if mode == "1":
    #         keyword_vigenere = input("Please provide a keyword: ")
    #         plaintext_vigenere = input("Please provide a message to encrypt: ")
    #         print("Encrypting...")
    #         ciphertext_vingere = encryptVigenere(plaintext_vigenere, keyword_vigenere)
    #
    #         print(plaintext_vigenere + "\n" + ciphertext_vingere)
    #     elif mode == "2":
    #         keyword_vigenere = input("Please provide a keyword: ")
    #         ciphertext_vigenere = input("Please provide a message to decrypt: ")
    #         print("Decrypting...")
    #         plaintext_vingere = decryptVigenere(ciphertext_vigenere, keyword_vigenere)
    #
    #         print(plaintext_vingere + "\n" + ciphertext_vigenere)
    #     else:
    #         return
    # else:
    #     return

main()
