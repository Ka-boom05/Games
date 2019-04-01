game_run = 0
game = [
    ["-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-"]
]
c = [5,5,5,5,5,5,5]
let = "x"
sum = 0
for row in game:
    print(row[0],row[1],row[2],row[3],row[4],row[5],row[6])

while game_run < 42:
    if sum % 2 == 0:
        let = "x"
    else:
        let = "o"
    sum = sum + 1
    r = int(input("which row would you like to go in"))
    if r <= 6:
        j = c[r]
        c[r] = c[r] - 1
    game[j][r] = let

    for row in game:
        print(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
