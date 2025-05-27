class CaesarCipher:
    def encrypt_text(self, text, key):
        encrypted = ""
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                encrypted += chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            else:
                encrypted += char
        return encrypted

    def decrypt_text(self, text, key):
        return self.encrypt_text(text, -key)