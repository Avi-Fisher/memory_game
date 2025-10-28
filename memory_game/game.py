from memory_game.back import creat_table_card, creat_table


def game(size,max_guess):

    state = {"table_card":creat_table_card(size),
             "user_table":creat_table(size),
             "user_card":[],
             "max_guess":max_guess}


    return state

def check_search(state,num1,num2):
    if state["size"] >= num1 and state["size"] >= num2:
        if 0 <= num1 and 0 <= num2:
            return True
    return False

def check_in_table(state,num1,num2):

    if state["table_card"][num1][num2] != "*":
        return True

def corect_guess(state,card):

    return None

def rong_guess(state,num1,num2):

    return  None

def if_win(state):
    exit()

def if_lose(state):
    exit()



























