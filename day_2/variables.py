# Day 2: 30 Days of python programming

# Level 1

first_name = 'Shawn'
last_name = 'The Sheep'
full_name = 'Shawn The Sheep'
country = 'United Kingdom'
city = 'The Big City'
age = 999
year = 2024
is_married, is_true, is_light_on = False, True, True

# Level 2

print(f'first_name: {type(first_name)}, last_name: {type(last_name)}, full_name: {type(full_name)}')
print('country: ' + str(type(country)) + ', city: ' + str(type(city)))
print(f'age: {type(age)}, year: {type(year)}')
print(f'is_married: {type(is_married)}, is_true: {type(is_true)}, is_light_on: {type(is_light_on)}')

print(len(first_name))
print(len(last_name))
print(len(first_name) == len(last_name))
print(len(first_name) < len(last_name))
print(len(first_name) > len(last_name))

num_one, num_two = 5, 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two
print(num_one, num_two, total, diff, product, division, remainder, exp, floor_division)

radius = 30
area_of_circle = 3.14159 * radius ** 2
print(area_of_circle)

circum_of_circle = 2 * 3.14159 * radius
print(circum_of_circle)

radius = float(input('Enter circle radius: '))
area_of_circle = 3.14159 * radius ** 2
print(area_of_circle)

first_name, last_name, country, age = input('Enter first name: '), input('Enter last name: '), input('Enter country: '), input('Enter age: ')
print(first_name, last_name, country, age)

help('keywords')