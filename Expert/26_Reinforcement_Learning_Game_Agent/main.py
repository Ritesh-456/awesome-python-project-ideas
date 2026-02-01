from game import TicTacToe
from agent import QLearningAgent

def main():
    game = TicTacToe()
    agent = QLearningAgent()

    print("Reinforcement Learning Tic-Tac-Toe Agent")
    print("The agent uses Q-learning to play Tic-Tac-Toe against you.")
    print()

    while True:
        print("Menu:")
        print("1. Train the agent")
        print("2. Play against the agent")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            episodes = int(input("Enter number of training episodes (default 10000): ") or "10000")
            agent.train(game, episodes)
        elif choice == "2":
            print("You are O, Agent is X. You go second.")
            print("Board positions:")
            print("0 | 1 | 2")
            print("---------")
            print("3 | 4 | 5")
            print("---------")
            print("6 | 7 | 8")
            print()
            agent.play(game)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()