import sys
import csv
import os


def redundant_team_name(i):
    # generated for ceda 12-13
    i = i.replace('CL		', 'Dartmouth CL')
    i = i.replace('127', 'UNLV ZZ')
    i = i.replace('120', 'CSUF ZZ')
    i = i.replace('130', 'UNLV ZZ')
    i = i.replace('128', 'UNLV ZZ')
    i = i.replace('125', 'CalPoly ZZ')
    i = i.replace('132', 'Wyoming ZZ')
    i = i.replace('119', 'CSUF ZZ')
    i = i.replace('134', 'Wyoming ZZ')
    i = i.replace('135', 'Vermont ZZ')
    i = i.replace('122', 'ISU ZZ')
    i = i.replace('123', 'ISU ZZ')
    i = i.replace('139', 'Whitman ZZ')
    i = i.replace('109', 'Bard ZZ')
    i = i.replace('100', 'UWG ZZ')
    i = i.replace('KT				', 'USC KT')
    i = i.replace('137', 'Whitman ZZ')
    i = i.replace('116', 'Louisville ZZ')
    i = i.replace('CK																				Che', 'Dartmouth CK       Che')
    i = i.replace('114', 'Louisville ZZ')
    i = i.replace('Donnely', 'Barsky')
    i = i.replace('103', 'Augustana ZZ')
    i = i.replace('118', 'CSUF ZZ')
    i = i.replace('117', 'Louisville ZZ')
    i = i.replace('131', 'Wyoming ZZ')
    i = i.replace('133', 'Wyoming ZZ')
    i = i.replace('129', 'UNLV ZZ')
    i = i.replace('138', 'Whitman ZZ')
    i = i.replace('124', 'UNT ZZ')
    i = i.replace('126', 'CalPoly ZZ')
    i = i.replace('121', 'CSUF ZZ')
    i = i.replace('OP																				Ove', 'USC OP           Ove')
    i = i.replace('108', 'Bard ZZ')
    return i


if __name__ == '__main__':
    folder = sys.argv[1]
    files = [f for f in os.listdir(folder) if f.endswith('.csv')]
    for file in files:
        newrows = []
        with open(folder + '/' + file) as f:
            reader = csv.reader(f)
            for row in reader:
                debate = []
                for item in row:
                    debate.append(redundant_team_name(item))
                newrows.append(debate)
        with open('to-process/cleaned/' + file, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(newrows)
