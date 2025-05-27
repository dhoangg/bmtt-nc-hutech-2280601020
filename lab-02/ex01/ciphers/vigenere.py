class VigenereCipher:
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def extend_key(self, text, key):
        key = key.upper()
        extended_key = (key * (len(text) // len(key) + 1))[:len(text)]
        return extended_key

    def encrypt(self, text, key):
        text = text.upper()
        key = self.extend_key(text, key)
        encrypted = ""
        for t, k in zip(text, key):
            if t.isalpha():
                t_idx = self.alphabet.index(t)
                k_idx = self.alphabet.index(k)
                encrypted += self.alphabet[(t_idx + k_idx) % 26]
            else:
                encrypted += t
        return encrypted

    def decrypt(self, text, key):
        text = text.upper()
        key = self.extend_key(text, key)
        decrypted = ""
        for t, k in zip(text, key):
            if t.isalpha():
                t_idx = self.alphabet.index(t)
                k_idx = self.alphabet.index(k)
                decrypted += self.alphabet[(t_idx - k_idx) % 26]
            else:
                decrypted += t
        return decrypted