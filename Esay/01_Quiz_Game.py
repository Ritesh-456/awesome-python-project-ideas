def main():
    print("Welcome to my Quiz Mania")

    suggestion = input("Do you Want to guess and play? ").strip().lower()

    if suggestion != "yes":
        quit()

    print("lets start....\nI will ask 6 questions and you need to score at least 5 out of 6")

    questions = [
        {
            "prompt": "Q1: Which animal is known as the 'Ship of the Desert'?: ",
            "answers": ["camel"],
        },
        {
            "prompt": "Q2: How many days are there in a week?: ",
            "answers": ["7", "seven", "7 days", "seven days"],
        },
        {
            "prompt": "Q3: How many hours are there in a day?: ",
            "answers": ["24", "twenty four", "24 hours", "twenty four hours"],
        },
        {
            "prompt": "Q4: Which animal is known as the king of the jungle?: ",
            "answers": ["lion"],
        },
        {
            "prompt": "Q5: Name the National bird of India?: ",
            "answers": ["peacock", "the peacock"],
        },
        {
            "prompt": "Q6: What is the color of the eyes of Ioanna?: ",
            "answers": ["brown"],
        },
    ]

    count = 0

    for q in questions:
        answer = input(q["prompt"]).strip().lower()
        if answer in q["answers"]:
            print("Correct....")
            count += 1
        else:
            print("!! Wrong !!")

    if count >= 5:
        print(f"Congrats YOU WIN !!\nYour score is: {count}")
    else:
        print(f"Better Luck Next Time !!\nYour score is {count}")


if __name__ == "__main__":
    main()
