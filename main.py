from pprint import pprint
# for i in range(1,10):
#     if i % 2 == 0:
#         print(i)
#         i= i+1
# num = 100
# while True:
#     if num>0 and num <10:
#         print("Kofo is awesome")
#         num=num+1

# def multiply(*numbers):
#     total = 1
#     print(total)
#     for number in numbers:
#         total *=number
#         print(total)
#     return total
# multiply(4,5,6,7,6)

# def fizz_buzz(div):
#     if (div %3 ==0) and (div % 5 == 0):
#         print (f"Fizz Buzz")
#     elif div % 3 ==0:
#         print (f"Fizz")
#     elif div % 5 ==0:
#         print (f"Buzz")
#     else:
#         print(div)
#
# fizz_buzz(50)

# items = [
#     ('name', 'kofo', 'age', 75), ('name','kofoworola','age', 30)
# ]
# def sort_item(item):
#     return item[3]
#
# items.sort(key=sort_item)
# items.sort(key=lambda item:item[3])
# print(items)
# products_for_sale = [
#     ('milk',1), ('sugar', 2),('garri', 100)
# ]
# price= list( map(lambda item:item[1],products_for_sale))
# print(price)
# filtered_option = list(filter (lambda item:item[1]>= 10,products_for_sale))
# print(filtered_option)

#list comprehension expression

# price = [item[1] for item in products_for_sale]
# pprint(price)
#
# sentence = "This is a common interview question"
# def most_common():
#     items=list([x for x in sentence])
#     most_common = 0
#     item = items[0]
#     for x in items:
#         currency_frequency = sentence.count(x)
#         if currency_frequency >most_common:
#             most_common = currency_frequency
#             item = x
#     pprint(item)
# most_common()


# try:
#     with open("test.py") as file:
#         print ("file opened.")
    # email = int(input("Phone Number: "))
# except ValueError:
#     print("You didn't enter a valid number")
# except FileNotFoundError:
#     print('File not found')
# else:
#     print("number saved")

def calculate_loan():
    age = int(input("age: "))
    amount = float(input("Amount requested: "))
    interest = float(input("Interest rate: "))
    if age >18 :
        rate_owed = (interest*amount)/100
        amount_repaid = amount +rate_owed
        print (f"You will owe {amount_repaid}")
    else:
        print("We do not give loans to children")




calculate_loan()
