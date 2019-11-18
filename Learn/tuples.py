x = (1,2,3)
print(type(x))
months = ('January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December')
print(months)
y = tuple((4,5,6))
print(dir(x))

#Tules of only element
x = (1,)
print(type(x))
print(x)

#Methods dir
x = (5,4,3,2,1)
print([5])
del x
print(x) #The tuples are unmodifiable

#Tuples with Dictorionies
locations = {
    (35.12312, 39.00000):'Tokio',
    (15.12312, 47.00000):'New York'
}
print(type(locations))