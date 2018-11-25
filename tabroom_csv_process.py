import sys
import csv
import os


def standardize(i):
    i = i.replace('"', '')
    i = i.replace('Van Buren', 'Van-Buren')
    i = i.replace('De Los Santos', 'De-Los-Santos')
    i = i.replace('Nevada Las Vegas', 'UNLV')
    i = i.replace('Mis-', 'Missouri - Kansas City')
    i = i.replace('Minnes', 'Minnesota')
    i = i.replace('MisSta', 'Missouri State')
    i = i.replace('Concor', 'Concordia')
    i = i.replace('EmpSta', 'Emporia State')
    i = i.replace(' J.', '')
    i = i.replace('Cram Helwich', 'Cram-Helwich')
    i = i.replace('David Michael', 'David-Michael')
    return i


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
        if len(meta) != 4:
            print(meta)
            raise Exception('File named wrong?')
        debates = []
        for debate_raw in reader:
            debate = []

            for i in debate_raw:
                j = standardize(i)
                debate_split = j.split()
                debate += debate_split

            # handle multi-word school names
            school_fix_1 = ['George', 'UC', 'Southern', 'United', 'Wayne',
                            'James', 'Wichita', 'Michigan', 'Missouri', 'Mary',
                            'Central', 'West', 'Wake', 'Arizona', 'Emporia',
                            'Johnson', 'UT', 'Fresno', 'Cal',
                            'Weber', 'States', 'Kansas']
            school_fix_2 = ['Mason', 'Berkeley', 'California', 'State',
                            'Madison', 'Washington', 'Oklahoma', 'Virginia',
                            'Forest', 'Georgia', 'States', 'University',
                            'Methodist', 'Dallas', 'San', '-', 'County',
                            'Dallas']
            school_fix_3 = ['Antonio', 'Military', 'Kansas', 'Community',
                            'Fullerton']
            school_fix_4 = ['City']

            for i in [0, 5]:
                if debate[i] in school_fix_1:
                    if debate[i + 1] in school_fix_2:
                        if debate[i + 2] in school_fix_3:
                            if debate[i + 3] in school_fix_4:
                                end = i + 4
                            else:
                                end = i + 3
                        else:
                            end = i + 2
                    else:
                        end = i + 1
                    debate[i:end] = [' '.join(debate[i:end])]

            # delete punctuation
            del debate[1]
            del debate[2]
            del debate[4]
            del debate[5]

            elim_names = ['dubs', 'finals', 'octs', 'quarters', 'semis']
            judge_fix = ['Helwich,']
            possible_decisions = ['Aff', 'Neg']
            num_judges = 0
            if debate[6] == 'BYE':
                debate[7:] = [-1, -1, -1, -1]
            elif meta[2] in elim_names:
                num_judges = int((len(debate) - 6) / 3)
                for i in range(num_judges):  # join judge names
                    if debate[7 + i] in judge_fix:
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
                    if debate[7 + i] in judge_fix:
                        debate[6 + i:9 + i] = [' '.join(debate[6 + i:9 + i])]
                    else:
                        debate[6 + i:8 + i] = [' '.join(debate[6 + i:8 + i])]
                # clear out ranks (ranks???? why???)
                debate = [i for i in debate if i not in ['1', '2', '3', '4']]
                # rearrange decision data
                decisions = []
                dec_start = 6 + num_judges * 2
                for i in range(num_judges):
                    decisions.append(debate[6 + i])
                    decisions.append(debate[6 + num_judges + i])
                    this_dec_start = dec_start + 6 * i
                    this_dec_end = dec_start + 8 + 6 * i
                    decisions += debate[this_dec_start:this_dec_end:2]
                debate = debate[:6]
                debate += decisions
            debate = meta + debate

            # status check
            # print(debate)
            status_check(debate, num_judges)

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


def status_check(row, num_judges):
    if num_judges == 0:  # bye
        correct_length = 10 + 5
    else:
        correct_length = 10 + 6 * num_judges
    if len(row) != correct_length:
        print(row)
        print(len(row))
        raise Exception('Inconsistent line length -- check raw data')


def open_multiple(path):
    files = [f for f in os.listdir(path) if f.endswith('.csv')]
    for file in files:
        open_csv(path + '/' + file)


if __name__ == '__main__':
    open_multiple(sys.argv[1])
