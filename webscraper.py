with open('nintendogames.txt', 'r') as file:
    for line in file:
        if "games/nes/" in line.strip():
            print(line.strip())
