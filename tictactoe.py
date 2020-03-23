def new_playground():
    lst = []  
    for i in range(3):
        lst.append([])
        for j in range(3):
            lst[i].append('')
    return(lst)

def playground(lst, count_turn):
    print()
    for i in range(3):
        print(lst[i])

    print()
    if(count_turn > 5):
        is_winner(lst, count_turn)
    else:
        count_turn += 1
        player(lst, count_turn)

def is_winner(lst, count_turn):
    for i in range(3):
        if((lst[i][0] == lst[i][1] == lst[i][2]) and (lst[i][0] != '' and lst[i][1] != '' and lst[i][2] != '')):
            print("Vitaz je hrac c." + str(lst[i][0]))
            return

        elif((lst[0][i] == lst[1][i] == lst[2][i]) and (lst[0][i] != '' and lst[1][i] != '' and lst[2][i] != '')):
            print("Vitaz je hrac c." + str(lst[0][i]))
            return
            
        elif((lst[0][0] == lst[1][1] == lst[2][2]) and (lst[0][0] != '' and lst[1][1] != '' and lst[2][2] != '')):
            print("Vitaz je hrac c." + str(lst[i][i]))
            return
    
        elif((lst[0][2] == lst[1][1] == lst[2][0]) and (lst[0][2] != '' and lst[1][1] != '' and lst[2][0] != '')):
            print("Vitaz je hrac c." + str(lst[2][0]))
            return

    if(lst[0][0] != '' and lst[0][1] != '' and lst[0][2] != '' and lst[1][0] != '' and lst[1][1] != '' and lst[1][2] != '' and lst[2][0] != '' and lst[2][1] != '' and lst[2][2] != ''):
        print("Je to remiza.")
        return

    count_turn += 1
    player(lst, count_turn)

def player(lst, count_turn):
    if(count_turn % 2 == 0):
        num = 1        

    elif(count_turn % 2 == 1):
        num = 2

    turn = input("Hrac c." + str(num) + " je na tahu: ").split()

    if(lst[int(turn[0]) - 1][int(turn[1]) - 1] != ''):
        print("Na danom mieste uz nieco je!!!")
        player(lst, count_turn)
    
    lst[int(turn[0]) - 1][int(turn[1]) - 1] = num
    playground(lst, count_turn)

def game():
    count_turn = 1
    lst = new_playground()
    playground(lst, count_turn)

game()
