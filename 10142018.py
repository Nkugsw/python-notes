travel = ['kuwait','langkawi','ny','japan','vienam']

#print('The first three items in the list are:')
#print(travel[:3])

#print('Three items from the middle of the list are:')
#print(travel[1:4])

#print('The last three items in the list are:')
#print(travel[-3:])

friendpizza = travel[:]
friendpizza.append('cannoli')

print('\nMy favourite pizza are:')
for mp in travel:
    print(mp)

print('\nMy friend favourite pizza are:')
for fp in friendpizza:
    print(fp)
