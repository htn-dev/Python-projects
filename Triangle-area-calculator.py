print('Please enter the values of the three sides of the triangle: ')
# Take inputs from the user

a = float(input('Enter first side value: '))
b = float(input('Enter second side value: '))
c = float(input('Enter third side value: '))
# calculate the semi-perimeter
s = (a + b + c) / 2
# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)
