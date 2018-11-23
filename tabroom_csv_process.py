import sys
import csv
import os


def open_csv(fpath):
    file = open(fpath, 'r')
    try:
        reader = csv.reader(file)
        outfile = open('rounds.csv', 'a')
        writer = csv.writer(outfile)
        next(reader, None)  # skip header
        meta = os.path.basename(fpath)[:-4].split('-')
        if len(meta) == 3:
            meta.append('open')
        debates = []
        for debate_raw in reader:
            debate = []
            for i in debate_raw:
                debate_split = i.split()
                debate += debate_split

            # handle multi-word school names
            nameFix1 = ['George', 'UC', 'Southern', 'United', 'Wayne', 'James',
                        'Wichita', 'Michigan', 'Missouri', 'Mary', 'Central',
                        'West', 'Wake', 'Arizona', 'Emporia']
            nameFix2 = ['Mason', 'Berkeley', 'California', 'State', 'Madison',
                        'Washington', 'Oklahoma', 'Virginia', 'Forest',
                        'Georgia', 'State']
            nameFix3 = ['States']
            nameFix4 = ['-']

            if debate[0] in nameFix1 and debate[1] in nameFix2:
                debate[0:2] = [' '.join(debate[0:2])]
            elif debate[1] in nameFix3:
                debate[0:3] = [' '.join(debate[0:3])]
            elif debate[1] in nameFix4:
                debate[0:4] = [' '.join(debate[0:4])]
            if debate[5] in nameFix1 and debate[6] in nameFix2:
                debate[5:7] = [' '.join(debate[5:7])]
            elif debate[6] in nameFix3:
                debate[5:8] = [' '.join(debate[5:8])]
            elif debate[6] in nameFix4:
                debate[5:9] = [' '.join(debate[5:9])]

            # delete punctuation
            del debate[1]
            del debate[2]
            del debate[4]
            del debate[5]

            elimNames = ['dubs', 'finals', 'octs', 'quarters', 'semis']
            judgeFix = ['Helwich,']
            possible_decisions = ['Aff', 'Neg']
            if meta[2] in elimNames:
                num_judges = int((len(debate) - 6) / 3)
                for i in range(num_judges):  # join judge names
                    if debate[7 + i] in judgeFix:
                        debate[6 + i:9 + i] = [' '.join(debate[6 + i: 9 + i])]
                    else:
                        debate[6 + i:8 + i] = [' '.join(debate[6 + i: 8 + i])]
                decisions = []
                for i in range(num_judges):
                    decisions.append(debate[6 + i])
                    decisions.append(debate[6 + num_judges + i])
                    if decisions[-1] not in possible_decisions:  # status check
                        print(debate)
                        print(reader.line_num)
                        print(decisions[-1])
                        raise Exception('Decision invalid - check')
                    decisions += [-1, -1, -1, -1]
                debate = debate[:6]
                debate += decisions
                debate = meta + debate
            else:
                # get num judges
                num_judges = 0
                current = 6
                while debate[current] not in possible_decisions:
                    if ',' in debate[current]:
                        num_judges += 1
                    current += 1
                # join judge names
                for i in range(num_judges):
                    if debate[7 + i] in judgeFix:
                        debate[6 + i:9 + i] = [' '.join(debate[6 + i:9 + i])]
                    else:
                        debate[6 + i:8 + i] = [' '.join(debate[6 + i:8 + i])]

                # rearrange decision data
                decisions = []
                dec_start = 6 + num_judges * 2
                for i in range(num_judges):
                    decisions.append(debate[6 + i])
                    decisions.append(debate[6 + num_judges + i])
                    decisions += debate[i + dec_start:i + dec_start + 8:2]
                debate = debate[:6]
                debate += decisions
                debate = meta + debate

                status_check(debate, 28)

            # status check
            # print(debate)

            # add debate to round
            debates.append(debate)
        for debate in debates:
            writer.writerow(debate)
    except UnicodeDecodeError:
        print(f'Error: {fpath}')
    finally:
        file.close()
        outfile.close()
        os.rename(fpath, 'processed/' + os.path.basename(fpath))


def status_check(row, length):
    if len(row) != length:
        print(row)
        print(len(row))
        raise Exception('Inconsistent line length -- check raw data')


def open_multiple(path):
    files = [f for f in os.listdir(path) if f.endswith('.csv')]
    for file in files:
        open_csv(path + '/' + file)


if __name__ == '__main__':
    open_multiple(sys.argv[1])
