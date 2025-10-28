from memory_game import game
from memory_game.game import check_search, guess, corect_guess, check_guess
from memory_game.io import print_status


def play():

    print("welcome to memory game")
    size = int(input("enter size table"))
    max_guess = int(input("enter how meny guess you have"))


    state = game.game1(size,max_guess)
    print(state)
    while True:
        guess(state)
        print_status(state)

        guess(state)
        print_status(state)

        check_guess(state)
        print_status(state)










play()








