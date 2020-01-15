foods = ['pears', 'apples', 'milk', 'rice', 'bread']
for food in foods:
    print('\n'+food)
    if food == 'milk':
        print('your can to boy this')
        
print('\n'+'New list with break:')
for food in foods:
    if food == 'milk':
        break
    print(food)

print('\n'+'New list with continue:')
for food in foods:
    if food == 'milk':
        continue
    print(food)
    
for numbers in range(1,8):
    print('')
    print(numbers)

print('')
for letters in 'El Pinche Pastel':
    print(letters)

print('')
count = 1   
while count <= 10:
    print(count)
    count = count + 2