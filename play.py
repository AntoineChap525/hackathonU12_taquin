def print_taquin(taquin):
    for row in taquin:
        print(" ".join(map(str, row)))

def move_taquin(taquin, direction):
    i, j = get_empty_position(taquin)
    print(direction)
    if direction == "Z" and i > 0:
        taquin[i][j], taquin[i - 1][j] = taquin[i - 1][j], taquin[i][j]
    elif direction == "S" and i < len(taquin) - 1:
        taquin[i][j], taquin[i + 1][j] = taquin[i + 1][j], taquin[i][j]
    elif direction == "Q" and j > 0:
        taquin[i][j], taquin[i][j - 1] = taquin[i][j - 1], taquin[i][j]
    elif direction == "D" and j < len(taquin[0]) - 1:
        taquin[i][j], taquin[i][j + 1] = taquin[i][j + 1], taquin[i][j]
    else:
        print("quelque chose s'est mal passé...")

def get_empty_position(taquin):
    for i, row in enumerate(taquin):
        for j, value in enumerate(row):
            if value == 0:
                return i, j

def main():
    taquin = [[0, 2, 3],
              [4, 5, 6],
              [7, 8, 1]]

    while True:
        print_taquin(taquin)

        direction = input("Entrez la direction (z/q/s/d) ou 'x' pour quitter : ").upper()

        if direction == 'X':
            break
        elif direction in ["Z", "Q", "S", "D"]:
            move_taquin(taquin, direction)
        else:
            print("Direction non valide. Utilisez U, D, L, R ou X pour quitter.")

if __name__ == "__main__":
    main()
