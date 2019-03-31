game = [["-","-","-"],["-","-","-"],["-","-","-"]]
game_run = 0
print("player 1 goes first.")
let = "x"
sum = 0
for row in game:
    print(row[0], row[1], row[2])

dsw=0
while game_run < 9:
    c = int(input("What column would you like to go to? "))
    r = int(input("What row would you like to go to? "))
    if game[c][r] == "-":
        if sum % 2 == 0:
            let = "x"
        else:
            let = "o"
        sum = sum + 1
        game[c][r] = let
        print(game)
        game_run = game_run + 1
        for row in game:
            print(row[0], row[1], row[2])
        for l in range (0,3):
            if (game [0][l] == let and game[1][l] == "x" and game[2][l] == "x") or (game [0][l] == "o" and game[1][l] == "o" and game[2][l] == "o"):
                dsw = 1
                break
        if dsw == 0:
            for k in range(0, 3):
                if (game[k][0] == "x" and game[k][1] == "x" and game[k][2] == "x") or (game[k][0] == "o" and game[k][1] == "o" and game[k][2] == "o"):
                    dsw = 1
                    break
        if dsw == 0:
            if (game[0][0] == let and game[1][1] == let and game[2][2] == let) or  (game[2][0] == let and game[1][1] == let and game[0][2] == let):
                dsw = 1

        if dsw == 1:
            game_run = 123456789098765432

    else:
        print("This space is already occupied.")
        print("Pick a new place to move!")

if dsw == 1:
    print("Player " + let + " you win!")
