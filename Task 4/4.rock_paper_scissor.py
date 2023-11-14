import random

class RockPaperScissors:
    def __init__(self):
        self.user_choice = None
        self.computer_choice = None
        self.user_score = 0
        self.computer_score = 0

    def get_user_choice(self):
        """Prompts the user to choose rock, paper, or scissors.

        Returns:
            The user's choice, as a string.
        """

        valid_choices = ["rock", "paper", "scissors"]
        while True:
            user_choice = input("Choose rock, paper, or scissors: ")
            if user_choice.lower() in valid_choices:
                return user_choice.lower()
            else:
                print("Invalid choice. Please try again.")

    def generate_computer_choice(self):
        """Generates a random choice (rock, paper, or scissors) for the computer.

        Returns:
            The computer's choice, as a string.
        """

        computer_choice = random.choice(["rock", "paper", "scissors"])
        return computer_choice

    def determine_winner(self):
        """Determines the winner based on the user's choice and the computer's choice.

        Returns:
            A string indicating the winner, or "tie" if the game is a tie.
        """

        if self.user_choice == self.computer_choice:
            return "tie"
        elif self.user_choice == "rock" and self.computer_choice == "scissors":
            return "user"
        elif self.user_choice == "paper" and self.computer_choice == "rock":
            return "user"
        elif self.user_choice == "scissors" and self.computer_choice == "paper":
            return "user"
        else:
            return "computer"

    def update_scores(self,winner):
        """Updates the user's and computer's scores based on the winner of the round.

        Args:
            winner: A string indicating the winner of the round, or "tie".
        """

        if winner == "user":
            self.user_score += 1
        elif winner == "computer":
            self.computer_score += 1

    def display_result(self):
        """Displays the user's choice, the computer's choice, and the winner of the round."""

        print(f"You chose {self.user_choice} and the computer chose {self.computer_choice}.")

        winner = self.determine_winner()
        if winner == "tie":
            print("It's a tie!")
        else:
            print(f"{winner.capitalize()} wins!")

    def play_again(self):
        """Prompts the user if they want to play another round.

        Returns:
            A boolean indicating whether the user wants to play another round.
        """

        while True:
            play_again = input("Do you want to play another round? (y/n): ")
            if play_again.lower() in ["y", "n"]:
                return play_again.lower() == "y"
            else:
                print("Invalid choice. Please try again.")

def main():
    game = RockPaperScissors()

    while True:
        game.user_choice = game.get_user_choice()
        game.computer_choice = game.generate_computer_choice()

        winner=game.determine_winner()
        game.update_scores(winner)
        game.display_result()

        if not game.play_again():
            break

    print(f"Final score: User {game.user_score} - Computer {game.computer_score}")

if __name__ == "__main__":
    main()