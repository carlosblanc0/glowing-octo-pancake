# 1 Assign variables, mathematical operations

commute = {
    'Employee A': 15.62,
    'Employee B': 41.85,
    'Employee C': 32.67
}
travels = {
    'Employee A': int(input()),
    'Employee B': int(input()),
    'Employee C': int(input())
}
t_d_t = sum(commute[employee] * travels[employee] for employee in travels)
print(f'Distance: {t_d_t: .2f} miles')

# 2 Assign variables, modulus operator

opp = 16  # Ounces per pound
top = 2000  # Pounds per ton

# Input: Accept the number of ounces as input
ounces = int(input())

# Calculate tons, pounds, and remaining ounces
tons = ounces // (opp * top)  # Calculate the number of tons
ro = ounces % (opp * top)  # Calculate the remaining ounces after removing tons
pounds = ro // opp  # Calculate the number of pounds from the remaining ounces
ro %= opp  # Calculate the remaining ounces after removing pounds

# Output the result
print(f'Tons: {tons}')
print(f'Pounds: {pounds}')
print(f'Ounces: {ro}')

# 3 Formatted output of data type
I_V = int(input())

# Check I_V is a valid index
if - 1 <= I_V < len(various_data_types):
    element = various_data_types[I_V]

    # Get the data type of the element
    D_T_N = str(type(element)).split("'")[1]

    print(f'Element {I_V}: {D_T_N}')

# 4 Data types in formulas
print(f'Trapezoid area: {0.5 * (int(input()) + int(input())) * int(input()):.1f} square meters')

#5 Data type conversion
# Take five integer inputs from the user
inputs = [int(input()) for _ in range(5)]

# Calculate sums
integer_sum = sum(inputs)
float_sum = float(sum(inputs))
string_sum = ''.join(map(str, inputs))

# Print results
print(f'Integer: {integer_sum}')
print(f'Float: {float_sum}')
print(f'String: {string_sum}')

# 6 Convert integer to string
id_num = int(input())

format_id_num = f'{id_num // 1000000}-{(id_num // 10000) % 100}-{id_num % 10000:04d}'

print(format_id_num)

#7 
user = int(input())
greater_than = user > max(predef_list)
print(f'Greater Than Max? {greater_than}')

#8

try:
    index = int(input())
    if 0 <= index < len(frameworks):
        print(frameworks[index])
    else:
        raise ValueError("Error")
except ValueError:
    print("Error")

#9 
temperature = int(input())

if temperature < 33:
    water_state = "Frozen"
    safety_comment = "Watch out for ice!"
elif 33 <= temperature <= 80:
    water_state = "Cold"
    safety_comment = None

if safety_comment:
    print(f"{water_state}\n{safety_comment}")
else:
    print(water_state)

#10
num_shares = int(input())
total_cost = 0.0
for _ in range(num_shares):
    stock_selection = input()
    if stock_selection in stocks:
        total_cost += stocks[stock_selection]

print(f"Total price: ${total_cost:.2f}")

#11 ***
item_name = input()
num_items = int(input())

if num_items < 10:
    total_cost = purchase[item_name] * num_items
elif 10 <= num_items <= 20:
    total_cost = purchase[item_name] * num_items * 0.95
else:
    total_cost = purchase[item_name] * num_items * 0.90

print(f"{item_name} ${total_cost:.2f}")

#12
import math
user_input = int(input())
input_fact = math.factorial(user_input)
is_greater100 = True if input_fact > 100 else False
print(input_fact)
print(is_greater100)

#13
import pigAge
input_pig_age = int(input())
converted_pig_age = pigAge.pigAge_converter(input_pig_age)
print(f'{input_pig_age} is {converted_pig_age} in human years')

