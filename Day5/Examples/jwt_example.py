import jwt
encoded = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')
print('Created Token is ', encoded)
decoded = jwt.decode(encoded, key='secret')
print('Decoded Token is ', decoded )