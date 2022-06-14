from Player import Player

# User Defined Function
# Get user input to fill points received by the players.
def fill_points():
    points = []
    frames = 10

    for i in range(frames):
        print(f'Frame {i + 1} - ')
        col = []

        first_throw = 0
        second_throw = 0
        third_throw = 0
        if i < frames - 1:
            while True:
                first_throw = input("First Throw: ")
                if int(float(first_throw)) <= 10:
                    col.append(int(first_throw))
                    break

            if int(first_throw) != 10:
                while True:
                    second_throw = input("Second Throw: ")
                    if (int(second_throw) + int(first_throw)) <= 10:
                        col.append(int(second_throw))
                        break
        else:
            while True:
                first_throw = input("First Throw: ")
                if int(first_throw) <= 10:
                    col.append(int(first_throw))
                    break
            
            if int(first_throw) < 10:
                while True:
                    second_throw = input("Second Throw: ")
                    if int(second_throw) + int(first_throw) <= 10:
                        col.append(int(second_throw))
                        break
            elif int(first_throw) == 10:
                while True:
                    second_throw = input("Second Throw: ")
                    if int(second_throw) <= 10:
                        col.append(int(second_throw))
                        break

            if int(first_throw) == 10 or int(first_throw) + int(second_throw) == 10:
                while True:
                    third_throw = input("Third Throw: ")
                    if int(third_throw) <= 10:
                        col.append(int(third_throw))
                        break
                    
        points.append(col)
    return points

count = input("Enter number of players: ")
players = []

for i in range(int(count)):
    print(f'\nPlayer {i + 1}')
    name = input("Insert Name: ")
    points = fill_points()

    players.append(Player(name, points))

for i in range(len(players)):
    print(f'\nPlayer {i + 1}: {players[i].name}')
    print(f'Points: {players[i].points}')
    print(f'Total Points: {players[i].calc_totalPoint()}')