import csv


def print_schools(reader):
    schools = []
    for line in reader:
        for team in [4, 7]:
            if line[team] not in schools:
                schools.append(line[team])
    schools.sort()
    for school in schools:
        print(school)


def main():
    rounds = open('rounds-completed.csv')
    reader = csv.reader(rounds)
    print_schools(reader)
    rounds.close()


if __name__ == '__main__':
    main()
