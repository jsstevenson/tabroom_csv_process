import sys
import csv
import os


def redundant_team_name(i):
    # generated for ndt 13-14
    i = i.replace('West Georgia - ', '')
    i = i.replace('Nevada Las Vegas - ', '')
    i = i.replace('Central Oklahoma - ', '')
    i = i.replace('Georgetown - ', '')
    i = i.replace('Oklahoma - ', '')
    i = i.replace('North Texas - ', '')
    i = i.replace('Towson - ', '')
    i = i.replace('Fresno State - ', '')
    i = i.replace('Georgia State - ', '')
    i = i.replace('Southern California - ', '')
    i = i.replace('George Mason - ', '')
    i = i.replace('Harvard - ', '')
    i = i.replace('Wake Forest - ', '')
    i = i.replace('Michigan State - ', '')
    i = i.replace('Kansas - ', '')
    i = i.replace('Northwestern - ', '')
    i = i.replace('Houston - ', '')
    i = i.replace('Indiana - ', '')
    i = i.replace('Iowa - ', '')
    i = i.replace('UT Dallas - ', '')
    i = i.replace('Kansas State - ', '')
    i = i.replace('Liberty - ', '')
    i = i.replace('Kentucky - ', '')
    i = i.replace('Vanderbilt - ', '')
    i = i.replace('Wyoming - ', '')
    i = i.replace('San Francisco State\Irvine - ', '')
    i = i.replace('Whitman College - ', '')
    i = i.replace('Georgia - ', '')
    i = i.replace('Weber State - ', '')
    i = i.replace('Trinity - ', '')
    i = i.replace('Arizona State - ', '')
    i = i.replace('Baylor - ', '')
    i = i.replace('Binghamton - ', '')
    i = i.replace('Rutgers-Newark - ', '')
    i = i.replace('Michigan - ', '')
    i = i.replace('Missouri - Kansas City - ', '')
    i = i.replace('Concordia College - ', '')
    i = i.replace('United States Military - ', '')
    i = i.replace('Wayne State - ', '')
    i = i.replace('Texas - ', '')
    i = i.replace('Mary Washington - ', '')
    i = i.replace('Emory - ', '')
    i = i.replace('Vermont - ', '')
    i = i.replace('James Madison - ', '')
    i = i.replace('Minnesota - ', '')
    i = i.replace('Missouri State - ', '')
    i = i.replace('Idaho State - ', '')
    i = i.replace('Berkeley - ', '')
    i = i.replace('Dartmouth College - ', '')
    i = i.replace('Kansas City Kansas CC - ', '')

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
