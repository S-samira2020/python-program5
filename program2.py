# Touple

'''dimension = (200, 50)
print(dimension[0])
print(dimension[1])
print()

# using for loop [ Touple ]

for names in dimension:
    print(names)
print()
'''

dimensions = (200, 50)
print('Original dimensions: ')
for dimension in dimensions:
    print(dimension)
print()

dimensions = (400, 100)
print('modified dimensions: ')
for dimension in dimensions:
    print(dimension)
print()

# 4.13
foods = ('drink', 'ice-cream', 'faluda', 'custard', 'sweets')
print('original menu: ')
for food  in foods:
    print(food)
print()

food = ('drink', 'faluda', 'custard', 'sweets', 'pastries')
print('one item modified menu:  ')
for food in foods:
    print(food)
print()

foods = ('drink', 'ice-cream', 'faluda', 'pastries', 'zera pani')
print('modified menu: ')
for food in foods:
    print(food)
print()