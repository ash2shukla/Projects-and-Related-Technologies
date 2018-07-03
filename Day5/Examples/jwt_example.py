import jwt
encoded = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')
print('Created Token is ', encoded)
decoded = jwt.decode(encoded, key='asd')
print('Decoded Token is ', decoded )