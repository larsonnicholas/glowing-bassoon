from unidecode import unidecode

with open('wordlisthard_nes2_formatted.txt', 'r') as file:
    for line in file:
        line2 = line.encode('utf-16')
        line2 = unidecode(line)
        print(line2.strip())
