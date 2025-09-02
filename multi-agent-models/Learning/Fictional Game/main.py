import fictional
import utils

def vs_human():
    agent = fictional.Agent()

    finished = False
    while not finished:
        winner = 0
        while winner == 0:
            print("Valid moves: Scissors(0), Paper(1), Rock(2)")
            human = utils.integer_input_between("Your move? ", 0, 2)

            computer = agent.choose_move()

            winner = utils.who_won(human, computer)
            
            print (f"Player has selected", utils.translate_move(human))
            print (f"Computer has selected", utils.translate_move(computer))
            if winner == -1:
                print(f"Player won this round\n")
            elif winner == 0:
                print ("It's a draw!\n")
            else:
                print("Computer won this round\n")
            agent.update_move(human)

        again = utils.integer_input_between("\nDo you want to continue? (0 - No, 1 - Yes) ", 0, 1)
        finished = True if again == 0 else False

if __name__ == "__main__":
    vs_human()