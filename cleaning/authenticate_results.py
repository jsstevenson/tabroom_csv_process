import sys
import csv


def authenticate_line(line):
    # line is type(list)
    try:
        int(line[0])
    except ValueError:
        print(line)

    elim_names = ['trips', 'dubs', 'octs', 'quarters', 'semis', 'finals']
    if line[2] not in elim_names:
        try:
            int(line[2])
        except ValueError:
            print(line)

    divisions = ['open', 'nov', 'jv', 'FYopen']
    if line[3] not in divisions:
        print(line)
    if len(line) < 11:
        print(line)
    if line[10] != 'BYE':
        if (len(line) - 10) % 6 != 0:
            print(line)
        num_judges = (len(line) - 10) // 6
        for i in range(num_judges):
            name = line[10 + 6 * i]
            if ',' not in name:
                print(line)
            decision = line[11 + 6 * i]
            if decision != 'Aff' and decision != 'Neg':
                print(line)
            for j in range(3):
                points = line[12 + 6 * i + j]
                try:
                    float(points)
                except ValueError:
                    print(line)
    else:
        if len(line) != 15:
            print(line)
        for i in range(11, 15):
            if line[i] != '-1':
                print(line)


def read_file(path):
    with open(path, 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            authenticate_line(line)
    print('all clear')


def main():
    read_file(sys.argv[1])


if __name__ == '__main__':
    main()
