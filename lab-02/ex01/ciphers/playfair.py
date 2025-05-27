class PlayfairCipher:
    def __init__(self):
        self.matrix = []
        self.alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # Omit J

    def create_matrix(self, key):
        key = key.upper().replace('J', 'I')
        key = ''.join(dict.fromkeys(key))  # Remove duplicates
        matrix = []
        for char in key:
            if char in self.alphabet and char not in matrix:
                matrix.append(char)
        for char in self.alphabet:
            if char not in matrix:
                matrix.append(char)
        self.matrix = [matrix[i:i + 5] for i in range(0, 25, 5)]

    def find_position(self, char):
        for i in range(5):
            for j in range(5):
                if self.matrix[i][j] == char:
                    return i, j
        return None

    def prepare_text(self, text):
        text = text.upper().replace('J', 'I')
        text = ''.join(c for c in text if c.isalpha())
        prepared = ""
        i = 0
        while i < len(text):
            prepared += text[i]
            if i + 1 < len(text):
                if text[i] == text[i + 1]:
                    prepared += 'X'
                else:
                    prepared += text[i + 1]
                    i += 1
            else:
                prepared += 'X'
            i += 1
        return prepared

    def encrypt(self, text, key):
        self.create_matrix(key)
        text = self.prepare_text(text)
        encrypted = ""
        for i in range(0, len(text), 2):
            a, b = text[i], text[i + 1]
            row1, col1 = self.find_position(a)
            row2, col2 = self.find_position(b)
            if row1 == row2:
                encrypted += self.matrix[row1][(col1 + 1) % 5] + self.matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted += self.matrix[(row1 + 1) % 5][col1] + self.matrix[(row2 + 1) % 5][col2]
            else:
                encrypted += self.matrix[row1][col2] + self.matrix[row2][col1]
        return encrypted

    def decrypt(self, text, key):
        self.create_matrix(key)
        decrypted = ""
        for i in range(0, len(text), 2):
            a, b = text[i], text[i + 1]
            row1, col1 = self.find_position(a)
            row2, col2 = self.find_position(b)
            if row1 == row2:
                decrypted += self.matrix[row1][(col1 - 1) % 5] + self.matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted += self.matrix[(row1 - 1) % 5][col1] + self.matrix[(row2 - 1) % 5][col2]
            else:
                decrypted += self.matrix[row1][col2] + self.matrix[row2][col1]
        return decrypted