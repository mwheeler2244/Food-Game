

item = input('What item would you like to buy? ')
cost = float(input('What is the cost? '))
quantity = int(input('How many? '))


total = cost * quantity
print(f'the total is {round(total, 2)}')

tip = input('Do you want to add a tip? ')
if tip.lower() in ('yes', 'yeah', 'ya', 'yea'):
    tip_amount = total *0.2
    print(f'tweenty percent is {round(tip_amount, 2)}')

    new_total = tip_amount+ total
    print(f'The new total is {new_total: .2f}')

