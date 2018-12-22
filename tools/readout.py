import csv
import matplotlib as mpl
import sys
mpl.use('TkAgg')  # seems necessary to run matploblib on Mac OS from Bash?


def points_histo(reader):
    speaks = []
    elim_names = ['dubs', 'octs', 'quarters', 'semis', 'finals', 'trips']
    for line in reader:
        if line[2] not in elim_names:
            # print(line[:10])
            num_judges = int((len(line) - 10) / 6)
            for i in range(num_judges):
                print(line[10 + 2 * (i + 1):14 + 2 * (i + 1)])


def aff_win(file, division=None):
    file.seek(0)
    reader = csv.reader(file)
    aff_wins = 0
    total_ballots = 0
    for line in reader:
        if (not division) or (line[3] == division):
            if len(line) > 14:
                current = 11
                while current < len(line):
                    total_ballots += 1
                    if line[current] == 'Aff':
                        aff_wins += 1
                    current += 6
    return (aff_wins, total_ballots)


def aff_win_by_division(file):
    nov_results = aff_win(file, 'nov')
    print(f'novice: {nov_results[0]/nov_results[1]}')
    jv_results = aff_win(file, 'jv')
    print(f'jv: {jv_results[0]/jv_results[1]}')
    open_results = aff_win(file, 'open')
    print(f'open: {open_results[0]/open_results[1]}')
    aff_total = nov_results[0] + jv_results[0] + open_results[0]
    all_total = nov_results[1] + jv_results[1] + open_results[1]
    print(f'overall: {aff_total/all_total}')


def tourneys_by_aff_win(file):
    tournaments = get_tournament_list(file)
    for tournament in tournaments:
        results = aff_win_at_tournament(file, tournament)
        if results[1] > 50:
            print(f'{tournament}:')
            print(f'{results[0]/results[1]}')


def get_tournament_list(file):
    file.seek(0)
    reader = csv.reader(file)
    tournaments = []
    for line in reader:
        if line[1] not in tournaments:
            tournaments.append(line[1])
    return tournaments


def aff_win_at_tournament(file, tournament):
    file.seek(0)
    reader = csv.reader(file)
    aff = 0
    total = 0
    for line in reader:
        if line[1] == tournament:
            if len(line) > 14:
                current = 11
                while current < len(line):
                    total += 1
                    if line[current] == 'Aff':
                        aff += 1
                    current += 6
    return (aff, total)


def main():
    rounds = open(sys.argv[1])
    # run calculations
    # aff_win_by_division(rounds)
    # aff_win_at_tournament(rounds, 'ceda')
    tourneys_by_aff_win(rounds)
    rounds.close()


if __name__ == '__main__':
    main()
