print("Welcome to my Quiz Menia")

suggestion = input("Do you Want to guess and play? ").lower()
count = 0
wrong = 0
if suggestion == "yes":
    print("lets start....\nI will ask 5 questions and you need to score at least 4 out of 5")
    question1 = input("Q1: Which animal is known as the 'Ship of the Desert'?: ").lower()

    if question1 == "camel":
        print("Correct....")
        count += 1
    else:
        print("!! Wrong !!")
        wrong += 1

    question2 = input("Q2: How many days are there in a week?: ").lower()

    if question2 == "7" or question2 == "seven" or question2 == "7 days" or question2 == "seven days":
        print("Correct....")
        count += 1
    else:
        print("!! Wrong !!")
        wrong += 1

    question3 = input("Q3: How many hours are there in a day?: ").lower()

    if question3 == "24" or question3 == "twenty four" or question3 == "24 hours" or question3 == "twenty four hours":
        print("Correct....")
        count += 1
    else:
        print("!! Wrong !!")
        wrong += 1

    question4 = input("Q4: Which animal is known as the king of the jungle?: ").lower()

    if question4 == "lion":
        print("Correct....")
        count += 1
    else:
        print("!! Wrong !!")
        wrong += 1

    question5 = input("Q5: Name the National bird of India?: ").lower()

    if question5 == "peacock" or question5 == "the peacock":
        print("Correct....")
        count += 1
    else:
        print("!! Wrong !!")
        wrong += 1

    if count >= 4:
        print(f"Congrats YOU WIN !!\nYour score is: {count}")
    else:
        print(f"Better Luck Next Time !!\nYour score is {count}")

else:
    print("Thank you")
