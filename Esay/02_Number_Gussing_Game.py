import random

while True:
    computer = random.randint(1, 100)
    box = 0
    Chances_left = 10

    print("\n🎮 New Game Started! Guess the number between 1 and 100.")
    
    while True:
        try:
            user = int(input("Enter a number: "))
            if user > computer:
                print("Number is high.")
                box += 1
                Chances_left -= 1
                print(f"You have now {Chances_left} chances left.")

            elif user == computer:
                print("🎉 Correct! You guessed it.")
                box += 1
                print(f"You took {box} attempts.")
                break
            
            elif user < computer:
                print("Number is low.")
                box += 1
                Chances_left -= 1
                print(f"You have now {Chances_left} chances left.")
            
            if Chances_left == 0:
                print(f"\n❌ You’ve used all your chances. The correct number was {computer}.")
                break
        
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay != "yes":
        print("Thanks for playing! 👋")
        break
