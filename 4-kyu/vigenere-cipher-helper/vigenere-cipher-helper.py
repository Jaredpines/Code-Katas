class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = list(key)
        self.alphabet = list(alphabet)
    
    def encode(self, text):
        position = 0
        encoded = ""
        for char in text:
            if char not in self.alphabet:
                encoded += char
            else:
                move = self.alphabet.index(self.key[position])
                encoded += self.alphabet[(self.alphabet.index(char) + move) % len(self.alphabet)]
            
            position = (position + 1) % len(self.key)
        return encoded
            
            
    
    def decode(self, text):
        position = 0
        decoded = ""
        for char in text:
            if char not in self.alphabet:
                decoded += char
            else:
                move = self.alphabet.index(self.key[position])
                decoded += self.alphabet[(self.alphabet.index(char) - move) % len(self.alphabet)]
            
            position = (position + 1) % len(self.key)
        return decoded
​