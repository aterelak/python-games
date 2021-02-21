from random import randint

first_number = randint(1, 9)
second_number = randint(1, 9)
third_number = randint(1, 9)
fourth_number = randint(1, 9)

current_code = [first_number, second_number, third_number, fourth_number]

print("········································")
print("···········                  ···········")
print("···········    MASTERMIND    ···········")
print("···········                  ···········")
print("········································")
print("                                        ")


for i in range(100):
    correct_position = 0
    correct_number = 0
    duplicate_current_code = list(current_code)

    x = input("Enter your proposition of code [1-9]: ")
    guess = list((x.split(' ')))

    duplicate_guess = list(guess)

    for j in range(len(current_code)):
        if int(guess[j]) == current_code[j]:
            duplicate_current_code.pop(j-correct_position)
            duplicate_guess.pop(j-correct_position)
            correct_position = correct_position + 1

    if correct_position == len(current_code):
        print("·····································")
        print("Great! The correct code: " + str(current_code))
        print("·····································")
        break

    for j in range(len(duplicate_current_code)):
        for k in range(len(duplicate_current_code)):
            if duplicate_current_code[j] == int(duplicate_guess[k]):
                correct_number = correct_number + 1
                duplicate_guess[k] =- 100
                duplicate_current_code[j] =- 100
                break

    print("                                      ")
    print("            Not exactly...            ")
    print("         --------------------         ")
    print("Correct number and correct position: " + str(correct_position))
    print("Correct number, but wrong position: " + str(correct_number))
    print("______________________________________")
    print("                                      ")
