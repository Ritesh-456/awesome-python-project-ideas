import numpy as np
import pickle
import os

class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor
        self.epsilon = epsilon  # Exploration rate
        self.q_table = {}
        self.load_q_table()

    def get_state_key(self, state):
        return tuple(state)

    def get_q_value(self, state, action):
        state_key = self.get_state_key(state)
        if state_key not in self.q_table:
            self.q_table[state_key] = np.zeros(9)
        return self.q_table[state_key][action]

    def set_q_value(self, state, action, value):
        state_key = self.get_state_key(state)
        if state_key not in self.q_table:
            self.q_table[state_key] = np.zeros(9)
        self.q_table[state_key][action] = value

    def choose_action(self, state, available_actions):
        if np.random.random() < self.epsilon:
            return np.random.choice(available_actions)
        else:
            q_values = [self.get_q_value(state, action) for action in available_actions]
            max_q = max(q_values)
            best_actions = [action for action, q in zip(available_actions, q_values) if q == max_q]
            return np.random.choice(best_actions)

    def learn(self, state, action, reward, next_state, next_available_actions, done):
        current_q = self.get_q_value(state, action)

        if done:
            target = reward
        else:
            next_q_values = [self.get_q_value(next_state, next_action) for next_action in next_available_actions]
            max_next_q = max(next_q_values) if next_q_values else 0
            target = reward + self.gamma * max_next_q

        new_q = current_q + self.alpha * (target - current_q)
        self.set_q_value(state, action, new_q)

    def save_q_table(self):
        with open('q_table.pkl', 'wb') as f:
            pickle.dump(self.q_table, f)
        print("Q-table saved.")

    def load_q_table(self):
        if os.path.exists('q_table.pkl'):
            with open('q_table.pkl', 'rb') as f:
                self.q_table = pickle.load(f)
            print("Q-table loaded.")
        else:
            print("No saved Q-table found. Starting fresh.")

    def train(self, game, episodes=10000):
        print("Training the agent...")
        for episode in range(episodes):
            state = game.reset()
            done = False

            while not done:
                available_actions = game.get_available_actions()
                action = self.choose_action(state, available_actions)

                next_state, reward, done = game.make_move(action)
                next_available_actions = game.get_available_actions() if not done else []

                self.learn(state, action, reward, next_state, next_available_actions, done)

                state = next_state

            if (episode + 1) % 1000 == 0:
                print(f"Episode {episode + 1}/{episodes} completed.")

        self.save_q_table()
        print("Training completed!")

    def play(self, game):
        state = game.reset()
        done = False

        while not done:
            available_actions = game.get_available_actions()
            action = self.choose_action(state, available_actions)
            print(f"Agent plays at position {action}")

            next_state, reward, done = game.make_move(action)
            state = next_state
            game.print_board()

            if not done:
                print("\nYour turn:")
                human_action = game.get_human_move()
                next_state, reward, done = game.make_move(human_action)
                state = next_state
                game.print_board()

        game.print_board()
        if game.winner == 1:
            print("Agent wins!")
        elif game.winner == -1:
            print("You win!")
        else:
            print("It's a draw!")