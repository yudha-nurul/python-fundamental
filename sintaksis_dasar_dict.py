print('Dictionary')
user = {
    'id': 1,
    'name': 'Leanne Graham',
    'username': 'Bret',
    'email': 'Sincere@april.biz',
}
print(user)
print('\ntampilkan dengan for in')
for dic in user:
    print(dic)

print('\ntampilkan valuenya dengan print satu2')
print(user['id'])
print(user['name'])
print(user['username'])

# dictionary yang lebih kompleks
print('\n>>> dictionary yang lebih kompleks')
user = {
    'id': 1,
    'name': 'Leanne Graham',
    'username': 'Bret',
    'email': 'Sincere@april.biz',
    'address': {
        'street': 'Kulas Light',
        'suite': 'Apt. 556',
        'city': "Gwenborough",
        'zipcode': '92998-3874',
        'geo': {
            'lat': '-37.3159',
            'lng': '81.1496'
        }
    }
}
print(user)
print(user['id'])
print(user['username'])
print(user['address']['street'])
print(user['address']['geo']['lat'])

