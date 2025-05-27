class RailFenceCipher:
    def encrypt(self, text, key):
        if key <= 0:
            return text
        rail = [''] * key
        row, step = 0, 1
        for char in text:
            rail[row] += char
            if row == 0:
                step = 1
            elif row == key - 1:
                step = -1
            row += step
        return ''.join(rail)

    def decrypt(self, text, key):
        if key <= 0:
            return text
        n = len(text)
        rail = [['\n'] * n for _ in range(key)]
        idx, step = 0, 1
        for row in range(key):
            step = 1 if row == 0 else -1
            col = 0
            r = row
            while col < n and 0 <= r < key:
                rail[r][col] = '*'
                if r == 0:
                    step = 1
                elif r == key - 1:
                    step = -1
                r += step
                col += 1

        pos = 0
        for r in range(key):
            for c in range(n):
                if rail[r][c] == '*' and pos < n:
                    rail[r][c] = text[pos]
                    pos += 1

        result = []
        row, step = 0, 1
        for i in range(n):
            result.append(rail[row][i])
            if row == 0:
                step = 1
            elif row == key - 1:
                step = -1
            row += step
        return ''.join(result)