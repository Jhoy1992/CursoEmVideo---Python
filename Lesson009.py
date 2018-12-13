someText = '   Hello world!'
print(len(someText))
print(someText.find('world'))

if 'world' in someText:
    print('Yes, I have.')

someText = someText.replace('world', 'sunshine')

if not 'world' in someText:
    print('OMG, thy stole the word.')

someText = someText.upper()

print(someText)

someText = someText.strip()

print(someText)

#