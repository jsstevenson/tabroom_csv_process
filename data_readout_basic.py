import csv
import matplotlib as mpl
mpl.use('TkAgg')


def points_histo(reader):
    speaks = []
    elim_names = ['dubs', 'octs', 'quarters', 'semis', 'finals']
    for line in reader:
        if line[2] not in elim_names:
            # print(line[:10])
            num_judges = int((len(line) - 10) / 6)
            for i in range(num_judges):
                print(line[10 + 2 * (i + 1):14 + 2 * (i + 1)])


def main():
    rounds = open('rounds-completed.csv')
    reader = csv.reader(rounds)
    points_histo(reader)
    rounds.close()


if __name__ == '__main__':
    main()
