from memory_game import game
from memory_game.back import check_2, check_if_number
from memory_game.game import check_search, guess, corect_guess, check_guess
from memory_game.io import print_status


def play():
    print("welcome to memory game")
    size = check_2()
    max_guess = check_if_number()

    state = game.game1(size,max_guess)

    while True:
        guess(state)
        print_status(state)

        guess(state)
        print_status(state)

        check_guess(state)
        print_status(state)










play()








