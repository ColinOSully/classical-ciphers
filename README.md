# Cipher Encryption & Decryption Toolkit

This Python project provides implementations of three classic encryption methods: **Keyword Cipher, Columnar Cipher, and Vigenère Cipher**. These ciphers allow for secure text encoding and decoding using specified keywords.

## Features

- **Keyword Cipher**: Substitutes letters based on a keyword-derived alphabet.
- **Columnar Transposition Cipher**: Rearranges text in a column-based pattern using a keyword.
- **Vigenère Cipher**: Implements polyalphabetic substitution encryption with a repeating keyword.

## Usage

### Encryption
Each cipher has a function to encrypt a plaintext message using a provided keyword:
- `encryptKeyword(plaintext, keyword)`
- `encryptColumnar(plaintext, keyword)`
- `encryptVigenere(plaintext, keyword)`

### Decryption
Corresponding functions are available for decryption:
- `decryptKeyword(ciphertext, keyword)`
- `decryptColumnar(ciphertext, keyword)`
- `decryptVigenere(ciphertext, keyword)`

### Example
```python
from osullivanProject1 import encryptVigenere, decryptVigenere

ciphertext = encryptVigenere("Hello World", "key")
print(ciphertext)  # Encrypted text

plaintext = decryptVigenere(ciphertext, "key")
print(plaintext)  # "Hello World"
```

## Running the Program
The script includes a `main()` function that, when executed, allows users to interactively choose a cipher, input text, and apply encryption or decryption.

```sh
python osullivanProject1.py
```

## Future Improvements
- Adding a user-friendly command-line interface
- Implementing additional cipher methods
- Improving input validation

---

Would you like any additional modifications, such as installation instructions or an example CLI usage?
