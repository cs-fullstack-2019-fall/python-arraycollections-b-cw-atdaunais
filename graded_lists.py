def main():
    name_list()
    quit_func()
    greater_or_less()


# takes the given list, prints the length, deletes an item, then prints the whole list
def name_list():
    arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]
    print(arrayForProblem2[2])
    print(len(arrayForProblem2))
    del arrayForProblem2[1]
    print(arrayForProblem2[2])


# basic quit function: loops through a prompt until user hits q to escape the function
def quit_func():
    userInput = ""
    while userInput != "q":
        userInput = input("Enter anything. Press 'q' to quit: ")


def greater_or_less():
    hardcode_array = [1, 50, 100, 2000, 35, 9, 250, 15, 9]
    user_input = int(input("Please enter a number: "))
    # setting variables to use in my for in loop to count up each time a condition is met
    greater_than = 0
    less_than = 0
    equal_to = 0

    for eachNum in hardcode_array:
        if user_input > eachNum:
            greater_than += 1 # counts up each time the condition is met in the loop for each element in the array
        elif user_input < eachNum:
            less_than += 1
        else:  # this else handles if the user inputs a number that's in the list
            equal_to += 1
    print(f"Your number is greater than {greater_than} number(s) in this list and less than {less_than} number(s).")
    if equal_to > 0:  # this statement only sends if the count went up meaning their number was found
        print(f"Your number, {user_input}, is in this list {equal_to} time(s).")

# saves each element of the list to a string variable to continue being updated with each loop.
# they save in reverse order, allowing them to be printed in reverse when printing the string
my5Array = [10, 55, 30, 21, 7]
emptyString = ""
for x in my5Array:
    emptyString = f"{str(x)} " + emptyString
print(emptyString)

main()
