import jwt

class JWT_Manager:
    def __init__(self, private_key, public_key):
        self.private_key = private_key
        self.public_key = public_key
        self.algorithm = "RS256"

    def encode(self, data):
        try:
            encoded = jwt.encode(data, self.private_key, algorithm=self.algorithm)
            return encoded
        except Exception as e:
            print(e)
            return None

    def decode(self, token):
        try:
            decoded = jwt.decode(token, self.public_key, algorithms=[self.algorithm])
            return decoded
        except Exception as e:
            print(e)
            return None