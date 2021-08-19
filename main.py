# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

billAmt = 0
if size == "S":
    billAmt = 15
    if add_pepperoni == "Y":
        billAmt += 3
elif size == "M":
    billAmt = 20
    if add_pepperoni == "Y":
        billAmt += 3
elif size == "L":
    billAmt = 25
    if add_pepperoni == "Y":
        billAmt += 3
else:
    billAmt

if extra_cheese == "Y":
    billAmt += 1

print(f"Your final bill is: ${billAmt}.")