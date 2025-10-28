from memory_game.back import creat_table_card, creat_table


def game1(size,max_guess):

    state = {"table_card":creat_table_card(size),
             "user_table":creat_table(size),
             "user_card":[],
             "card1": {"row":0,"column":0,"card":None},
             "card2": {"row":0,"column":0,"card":None},
             "user_guess":0,
             "max_guess":max_guess,
             "size":size,
             "guess_card":"card1",
             "not_guess_card":"card2"}
    return state

def check_search(state,num1,num2):

    if state["size"] >= num1 and state["size"] >= num2:
        if 0 <= num1 and 0 <= num2:
            return False
    return True

def check_in_table(state,num1,num2):

    if state["user_table"][num1][num2] != "*":
        return True

    return False

def check_guess(state):

    if state["card1"]["card"] == state["card2"]["card"] :
        corect_guess(state)
    else:
        rong_guess(state)

def corect_guess(state):

    state["user_table"][state["card1"]["row"]] [state["card1"]["column"]] = state["card1"]["card"]
    state["user_table"][state["card2"]["row"]] [state["card2"]["column"]] = state["card2"]["card"]

    state["user_card"].append(state["card1"]["card"])

    if_win(state)

def rong_guess(state):

    state["user_guess"] += 1
    state["user_table"][state[state["guess_card"]]["row"]][state[state["guess_card"]]["column"]] = "*"
    state["user_table"][state[state["not_guess_card"]]["row"]][state[state["not_guess_card"]]["column"]] = "*"
    if_lose(state)

def if_win(state):
    bool1 = True
    for i in range(state["size"]):
        for j in range(state["size"]):
            if state["user_table"][i][j] == "*":
                bool1 = False

    if bool1:
        print("you winnnnnn!!!!!!")
        exit("goodbye")

def if_lose(state):

    if state["user_guess"] == state["max_guess"]:
        print("you lose")
        exit("goodbye")

def guess(state):

    while True:
        try:
            row = int(input(f"enter num row {state["guess_card"]}")) -1
            column = int(input(f"enter num column {state["guess_card"]}")) -1
        except:
            print("enter only number")

        if check_search(state, row, column):
            continue
        if check_in_table(state, row, column):
            continue

        state[state["guess_card"]]["row"] = row
        state[state["guess_card"]]["column"] = column

        state[state["guess_card"]] ["card"] = state["table_card"] [row]  [column]
        state["user_table"] [state[state["guess_card"]] ["row"]] [state[state["guess_card"]] ["column"]] = state [state["guess_card"]] ["card"]

        state["guess_card"],state["not_guess_card"] = state["not_guess_card"],state["guess_card"]

        break
























