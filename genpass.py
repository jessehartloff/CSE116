import bcrypt
import datetime

if __name__ == '__main__':
    print(bcrypt.gensalt(20))
    password = 'removed'
    token = 'removed'
    print(bcrypt.hashpw(token.encode(), bcrypt.gensalt()))
