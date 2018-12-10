import sys
import csv
import os
import re


def standardize(i):
    # items that need to be first
    i = i.replace('GeoSta', 'GSU')
    i = i.replace('Georgia State', 'GSU')
    i = i.replace('MisSta/Vander', 'Missouri-State/Vanderbilt')
    i = i.replace('Rochester/George Mason', 'Roches/GMU')

    # the rest
    i = i.replace('"', '')
    i = i.replace('Arizona State', 'ASU')
    i = i.replace('Boston College', 'BostonCollege')
    i = i.replace('BosCol', 'BostonCollege')
    i = i.replace('Cal State Fullerton', 'CSUF')
    i = i.replace('Cavanaugh II', 'CavanaughII')
    i = i.replace('CenOkl', 'UCO')
    i = i.replace('Central Oklahoma', 'UCO')
    i = i.replace('Central Florida', 'UCF')
    i = i.replace('City College of San Francisco', 'CCSF')
    i = i.replace('Concor', 'Concordia')
    i = i.replace('Cram Helwich', 'Cram-Helwich')
    i = i.replace('CSU - Northridge', 'CSU-Northridge')
    i = i.replace('CSU Long Beach', 'CSU-Long-Beach')
    i = i.replace('David Michael', 'David-Michael')
    i = i.replace('De Los Santos', 'De-Los-Santos')
    i = i.replace('De La Rosa', 'De-La-Rosa')
    i = i.replace('Dehmlow Dunne', 'Dehmlow-Dunne')
    i = i.replace('EmpSta', 'Emporia-State')
    i = i.replace('Emporia State', 'Emporia-State')
    i = i.replace('Florida State', 'FSU')
    i = i.replace('George Mason', 'GMU')
    i = i.replace('GeoMas', 'GMU')
    i = i.replace('George Washington', 'GWU')
    i = i.replace('Georgi', 'Georgia')
    i = i.replace(' J.', '')
    i = i.replace('James Madison', 'JMU')
    i = i.replace('JohCou', 'JCCC')
    i = i.replace('K-State', 'KSU')
    i = i.replace('Kansas State', 'KSU')
    i = i.replace('Libert ', 'Liberty')
    i = i.replace('LoBuono Gonzalez', 'LoBuono-Gonzalez')
    i = i.replace('Louisv', 'Louisville')
    i = i.replace('Michigan State', 'MSU')
    i = i.replace('Minnes', 'Minnesota')
    i = i.replace('Mis-', 'UMKC')
    i = i.replace('Missouri - Kansas City', 'UMKC')
    i = i.replace('Missouri State', 'Missouri-State')
    i = i.replace('MisSta', 'Missouri-State')
    i = i.replace('Nevada Las Vegas', 'UNLV')
    i = i.replace('Northern Iowa', 'UNI')
    i = i.replace('Oklaho ', 'Oklahoma ')
    i = i.replace('Puget Sound', 'UPS')
    i = i.replace('Rodriguez Salcedo', 'Rodriguez-Salcedo')
    i = i.replace('Samfor', 'Samford')
    i = i.replace('San Diego State', 'SDSU')
    i = i.replace('San Francisco State', 'SFSU')
    i = i.replace('San Francisco', 'SFSU')
    i = i.replace('Southern California', 'USC')
    i = i.replace("St Mary's", "StMarys")
    i = i.replace('UC Berkeley', 'Cal')
    i = i.replace('UTSan', 'UTSA')
    i = i.replace('UT San Antonio', 'UTSA')
    i = i.replace('UT Dallas', 'UTD')
    i = i.replace('United States Military', 'Army')
    i = i.replace('Van Alstine', 'Van-Alstine')
    i = i.replace('Van Buren', 'Van-Buren')
    i = i.replace('Van Luvanee', 'Van-Luvanee')
    i = i.replace('Van Schenck', 'Van-Schenck')
    i = i.replace('Wake Forest', 'Wake')
    i = i.replace('Washto', 'UW')
    i = i.replace('WaySta', 'Wayne-State')
    i = i.replace('Wayne State', 'Wayne-State')
    i = i.replace('West Georgia', 'UWG')
    i = i.replace('West Virginia', 'WVU')
    i = i.replace('WicSta', 'Wichita')
    i = i.replace('Wichita State', 'Wichita')
    i = i.replace('Wisconsin- Madison', 'Wisconsin-Madison')
    i = i.replace('Webster Dunn', 'Webster-Dunn')

    return i


def open_csv(fpath, outfilename='rounds.csv'):
    file = open(fpath, 'r')
    try:
        reader = csv.reader(file)
        outfile = open(outfilename, 'a')
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
            # Eventually getting rid of this and doing brute replacements
            # school_fix_1 = ['George', 'Southern', 'United',
            #                 'James', 'Wichita', 'Michigan', 'Mary',
            #                 'Central', 'West', 'Wake', 'Arizona', 'Emporia',
            #                 'Johnson', 'UT', 'Fresno', 'Cal',
            #                 'Weber', 'States', 'Kansas']
            # school_fix_2 = ['Mason', 'California', 'State',
            #                 'Madison', 'Washington', 'Oklahoma', 'Virginia',
            #                 'Forest', 'Georgia', 'States', 'University',
            #                 'Methodist', 'Dallas', 'San', '-', 'County',
            #                 'Dallas']
            # school_fix_3 = ['Antonio', 'Military', 'Kansas', 'Community']
            # school_fix_4 = ['City']

            # for i in [0, 5]:
            #     if debate[i] in school_fix_1:
            #         if debate[i + 1] in school_fix_2:
            #             if debate[i + 2] in school_fix_3:
            #                 if debate[i + 3] in school_fix_4:
            #                     end = i + 4
            #                 else:
            #                     end = i + 3
            #             else:
            #                 end = i + 2
            #         else:
            #             end = i + 1
            #         debate[i:end] = [' '.join(debate[i:end])]

            # delete punctuation & initials
            initials = re.compile('^[A-Z][A-Z]')
            initials_long = re.compile('^[A-Z][a-z][A-Z][a-z]')
            if initials.match(debate[1]) or initials_long.match(debate[1]):
                del debate[1]
            del debate[2]
            if initials.match(debate[4]) or initials_long.match(debate[4]):
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
                        print(fpath)
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
                debate = [i for i in debate if i not in ['0', '1', '2', '3',
                                                         '4']]
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
            status_check(debate, num_judges, fpath)

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


def status_check(row, num_judges, fpath):
    if num_judges == 0:  # bye
        correct_length = 10 + 5
    else:
        correct_length = 10 + 6 * num_judges
    if len(row) != correct_length:
        print(row)
        print(len(row))
        print(fpath)
        raise Exception('Inconsistent line length -- check raw data')


def open_multiple(path):
    files = [f for f in os.listdir(path) if f.endswith('.csv')]
    for file in files:
        open_csv(path + '/' + file)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        open_multiple(sys.argv[1], sys.argv[2])
    else:
        open_multiple(sys.argv[1])
