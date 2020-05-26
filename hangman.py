import random

def hangman(word):
    wrong = 0
    stages = ["",
              "_____     ",
              "|         ",
              "|    |    ",
              "|    0    ",
              "|   /|\   ",
              "|   / \   ",
             ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
#    print(rletters)
#    print(board)
#    print(len(stages))

    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字入力してください:"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝利です！")
            print(" ".join(board))
            win = True
            break
    if not win:
#        print("\n".join(stages[0:wrong+1]))
        print("あなたの敗北です！正解は {}.".format(word))

if __name__ == "__main__":
    ans_list = ["cat",
                "dog",
                "pig",
                "mouse"]
    hangman(ans_list[random.randint(0,3)])

