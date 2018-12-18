import csv
import matplotlib as mpl
import sys
mpl.use('TkAgg')  # seems necessary to run matploblib on Mac OS from Bash?


def points_histo(reader):
    speaks = []
    elim_names = ['dubs', 'octs', 'quarters', 'semis', 'finals']
    for line in reader:
        if line[2] not in elim_names:
            # print(line[:10])
            num_judges = int((len(line) - 10) / 6)
            for i in range(num_judges):
                print(line[10 + 2 * (i + 1):14 + 2 * (i + 1)])


def aff_wins_vs_total(file, division=None):
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
    nov_results = aff_wins_vs_total(file, 'nov')
    print(f'novice: {nov_results[0]/nov_results[1]}')
    jv_results = aff_wins_vs_total(file, 'jv')
    print(f'jv: {jv_results[0]/jv_results[1]}')
    open_results = aff_wins_vs_total(file, 'open')
    print(f'open: {open_results[0]/open_results[1]}')


def main():
    rounds = open(sys.argv[1])
    # run calculations
    aff_win_by_division(rounds)
    rounds.close()


if __name__ == '__main__':
    main()
