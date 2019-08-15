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


def print_tournaments(reader):
    tournaments = []
    for line in reader:
        if line[1] not in tournaments:
            tournaments.append(line[1])
    tournaments.sort()
    for tournament in tournaments:
        print(tournament)


def main():
    rounds = open('rounds-completed.csv')
    reader = csv.reader(rounds)
    print_schools(reader)
    print_tournaments(reader)
    rounds.close()


if __name__ == '__main__':
    main()
