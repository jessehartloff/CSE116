import bcrypt
import datetime
import random

if __name__ == '__main__':
    print(bcrypt.gensalt(20))
    password = 'removed'
    token = 'removed'
    print(bcrypt.hashpw(token.encode(), bcrypt.gensalt()))

    l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    print(l)
    random.shuffle(l)
    print(l)
