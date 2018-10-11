names = ['jia','tiao','miao','wei']

nocome = 'tiao'

print(nocome.title() + " isn't coming.")

#names.remove(nocome)

names[1] = 'mao'

names.insert(0,'gan')

names.insert(2,'yi')

names.append('nai')

print(names)

one = names.pop(0)

print('Sorry ' + one.title() + ',only two.')

print(names[0].title() + ' you in!')

del names[0]

print(names)
