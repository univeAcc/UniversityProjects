import random

numbers = []
run = True

rand = random.randint(1,100)

while run:
    inp = int(input("\nEnter a number between 1 to 100: "))
    if inp == rand:
        numbers.append(inp)
        print(f"Exelent thats the correct number")
        run=False
    elif inp < 1 or inp > 100:
        print("enter a number between 10 to 100")
        numbers.append(inp)
    elif inp < rand:
        print("Wrong. enter a bigger number")
        numbers.append(inp)
    elif inp > rand:
        print("Wrong. enter a smaller number")
        numbers.append(inp)

print("\nThe correct number: ",rand)
print("Numbers you entered: ",numbers)
print(f"you geussed the number in {len(numbers)} tries")
