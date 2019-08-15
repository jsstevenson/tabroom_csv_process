import sys
import csv
import os
import re
import authenticate_results


def standardize(i):
    # items that need to be first
    i = i.replace('GeoSta', 'GSU')
    i = i.replace('Georgia State', 'GSU')
    i = i.replace('MisSta/Vander', 'Missouri-State/Vanderbilt')
    i = i.replace('Rochester/George Mason', 'Roches/GMU')

    # the rest
    i = i.replace('"', '')
    i = i.replace('Adam R.', 'Adam')
    i = i.replace('Alvarado Fierro', 'AlvaradoFierro')
    i = i.replace('Appalachian State', 'AppState')
    i = i.replace('Arizona State', 'ASU')
    i = i.replace('Arizona Competitive Speech and Debate Club', 'ACSDC')
    i = i.replace('Augustana College', 'Augustana')
    i = i.replace('Augsburg College', 'Augsburg')
    i = i.replace('Bard College', 'Bard')
    i = i.replace('Beth Brooks', 'Brooks')
    i = i.replace('Binghmtn', 'Binghamton')
    i = i.replace('Bockmon Solares', 'BockmonSolares')
    i = i.replace('Boston College', 'BostonCollege')
    i = i.replace('BosCol', 'BostonCollege')
    i = i.replace('Boston Coll', 'BostonCollege')
    i = i.replace('Cal State Fullerton', 'CSUF')
    i = i.replace('California, Berkeley', 'Cal')
    i = i.replace('CalPol ', 'CalPoly ')
    i = i.replace('Cavanaugh II', 'CavanaughII')
    i = i.replace('CenOkl', 'UCO')
    i = i.replace('Central Oklahoma', 'UCO')
    i = i.replace('Central Florida', 'UCF')
    i = i.replace('CenFlo', 'UCF')
    i = i.replace('City College of San Francisco', 'CCSF')
    i = i.replace('Clark Villanueva', 'ClarkVillanueva')
    i = i.replace('Concor ', 'Concordia ')
    i = i.replace('Concordia College', 'Concordia')
    i = i.replace('Cornel ', 'Cornell ')
    i = i.replace('Clario ', 'Clarion ')
    i = i.replace('Cram Helwich', 'Cram-Helwich')
    i = i.replace('CSU - Northridge', 'CSU-Northridge')
    i = i.replace('CSU Long Beach', 'CSULB')
    i = i.replace('CSU Northridge', 'CSUN')
    i = i.replace('CSU-NR', 'CSUN')
    i = i.replace('CSUChi', 'Chico')
    i = i.replace('Dartmo ', 'Dartmouth ')
    i = i.replace('Dartmouth College', 'Dartmouth')
    i = i.replace('David Michael', 'David-Michael')
    i = i.replace('De Los Santos', 'De-Los-Santos')
    i = i.replace('De La Huerta', 'De-La-Huerta')
    i = i.replace('De La Rosa', 'De-La-Rosa')
    i = i.replace('De Leon', 'DeLeon')
    i = i.replace('De Mattheis', 'DeMattheis')
    i = i.replace('De Ruyter', 'De-Ruyter')
    i = i.replace('Dela Cruz', 'Dela-Cruz')
    i = i.replace('De La Cruz', 'DeLaCruz')
    i = i.replace('Del Castillo', 'DelCastillo')
    i = i.replace('Del Rosario', 'Del-Rosario')
    i = i.replace('Dehmlow Dunne', 'Dehmlow-Dunne')
    i = i.replace('Du Rant', 'DuRant')
    i = i.replace('EmpSta', 'Emporia')
    i = i.replace('Emporia State', 'Emporia')
    i = i.replace('Florid ', 'Florida ')
    i = i.replace('UFlori', 'Florida')
    i = i.replace('Florida State', 'FSU')
    i = i.replace('FloSta', 'FSU')
    i = i.replace('Fresno State', 'Fresno')
    i = i.replace('FreSta', 'Fresno')
    i = i.replace('Fullerton Indy', 'CSUF')
    i = i.replace('Fullerton', 'CSUF')
    i = i.replace('Garcia Filkins', 'GarciaFilkins')
    i = i.replace('George Mason', 'GMU')
    i = i.replace('GeoMas', 'GMU')
    i = i.replace('George Washington', 'GWU')
    i = i.replace('Georgi ', 'Georgia ')
    i = i.replace('Housto ', 'Houston ')
    i = i.replace('Idaho State', 'ISU')
    i = i.replace('Illinois College', 'Illinois')
    i = i.replace('IL College', 'Illinois')
    i = i.replace('IllCol', 'Illinois')
    i = i.replace('IllSta', 'IllState')
    i = i.replace('Indian ', 'IU ')
    i = i.replace('Indiana', 'IU')
    i = i.replace('J.V.', 'JV')
    i = i.replace(' J.', '')
    i = i.replace('James Madison', 'JMU')
    i = i.replace('JamMad', 'JMU')
    i = i.replace('John Carroll', 'JohnCarroll')
    i = i.replace('JohCou', 'JCCC')
    i = i.replace('Johnson County Community College', 'JCCC')
    i = i.replace('Johnson County Community', 'JCCC')
    i = i.replace('K-State', 'KSU')
    i = i.replace('Kansas State', 'KSU')
    i = i.replace('KanSta', 'KSU')
    i = i.replace('Kan St', 'KSU')
    i = i.replace('KSU State', 'KSU')
    i = i.replace('KSU EPAW', 'KSU')
    i = i.replace('Kansas City Kansas CC', 'KCKCC')
    i = i.replace('KanCit', 'KCKCC')
    i = i.replace('Kentuc ', 'Kentucky ')
    i = i.replace('Kephart III', 'KephartIII')
    i = i.replace('Lakeland College', 'Lakeland')
    i = i.replace('LCSC - Lewis Cl', 'LCSC')
    i = i.replace('Lee, Jr', 'LeeJr')
    i = i.replace('Libert ', 'Liberty ')
    i = i.replace('LoBuono Gonzalez', 'LoBuono-Gonzalez')
    i = i.replace('Los Rios', 'LosRios')
    i = i.replace('Lville', 'Louisville')
    i = i.replace('Louisv ', 'Louisville ')
    i = i.replace('Loy Jr.', 'LoyJr.')
    i = i.replace('Mary Washington', 'UMW')
    i = i.replace('MarWas', 'UMW')
    i = i.replace('Michig ', 'Michigan ')
    i = i.replace('M-LS', 'MS')  # really Dustin?
    i = i.replace('Michigan State', 'MSU')
    i = i.replace('MicSta', 'MSU')
    i = i.replace('Mich St', 'MSU')
    i = i.replace('Minnes/', 'Minnesota/')
    i = i.replace('Minnes ', 'Minnesota ')
    i = i.replace('Mis-', 'UMKC')
    i = i.replace('Missouri - Kansas City', 'UMKC')
    i = i.replace('Missouri State', 'MoState')
    i = i.replace('Missouri-State/', 'MoState/')
    i = i.replace('MisSta', 'MoState')
    i = i.replace('MoSt ', 'MoState ')
    i = i.replace('MoSt/', 'MoState/')
    i = i.replace('MO State', 'MoState')
    i = i.replace('Monmou ', 'Monmouth ')
    i = i.replace('New York ', 'NYU ')  # resolve before New School
    i = i.replace('NewYor', 'NYU')
    i = i.replace('NewSch ', 'NewSchool ')
    i = i.replace('NewSch/', 'NewSchool/')
    i = i.replace('New School', 'NewSchool')
    i = i.replace('New ', 'NewSchool ')
    i = i.replace('New/', 'NewSchool/')
    i = i.replace('NewSch', 'NewSchool')
    i = i.replace('Nevada Las Vegas', 'UNLV')
    i = i.replace('Northern Iowa', 'UNI')
    i = i.replace('NorIow ', 'UNI ')
    i = i.replace('North Texas', 'UNT')
    i = i.replace('Nwstrn', 'Northwestern')
    i = i.replace('Northw', 'Northwestern')
    i = i.replace('Oklaho ', 'Oklahoma ')
    i = i.replace('Okla ', 'Oklahoma ')
    i = i.replace('Partlow Lefevre', 'Partlow-Lefevre')
    i = i.replace('Pittman III', 'PittmanIII')
    i = i.replace('Puget Sound', 'UPS')
    i = i.replace('Puget ', 'UPS ')
    i = i.replace('PugSou', 'UPS')
    i = i.replace('Puget', 'UPS')
    i = i.replace('Richard Ryan', 'Richard')
    i = i.replace('Rivas Umana', 'RivasUmana')
    i = i.replace('Roberts, Jeff A', 'Roberts, Jeff')
    i = i.replace('Roches ', 'Rochester ')
    i = i.replace('Roches/', 'Rochester/')
    i = i.replace('Rodriguez Salcedo', 'Rodriguez-Salcedo')
    i = i.replace('Rutger ', 'Rutgers ')
    i = i.replace('Rutger/', 'Rutgers/')
    i = i.replace('Rutgers-Newark', 'Rutgers')
    i = i.replace('RutgersNewark', 'Rutgers')
    i = i.replace('Sacramento State', 'SacState')
    i = i.replace('Samfor ', 'Samford ')
    i = i.replace('San Diego State', 'SDSU')
    i = i.replace('San Francisco State', 'SFSU')
    i = i.replace('San Francisco', 'SFSU')
    i = i.replace('SFSU/SFSU', 'SFSU')
    i = i.replace('SanFra', 'SFSU')
    i = i.replace('Sara Beth', 'Sara-Beth')
    i = i.replace(' “;Shooter“;', '')
    i = i.replace('Sjolin Falk', 'SjolinFalk')
    i = i.replace('Southern California', 'USC')
    i = i.replace('Southern Methodist', 'SMU')
    i = i.replace('Southwestern College', 'Southwestern')
    i = i.replace('SouCol', 'Southwestern')
    i = i.replace("St Mary's", "StMarys")
    i = i.replace('St. John', 'StJohn')
    i = i.replace('St John, Hillary', 'StJohn, Hillary')
    i = i.replace('Stone Watt', 'StoneWatt')
    i = i.replace('SUNY Broome', 'Broome')
    i = i.replace('Trinit ', 'Trinity ')
    i = i.replace('UC Berkeley', 'Cal')
    i = i.replace('UNoTex', 'UNT')
    i = i.replace('UTSan', 'UTSA')
    i = i.replace('UT San Antonio', 'UTSA')
    i = i.replace('UT-Ant', 'UTSA')
    i = i.replace('UT Dallas', 'UTD')
    i = i.replace('UTDal', 'UTD')
    i = i.replace('United States Military', 'Army')
    i = i.replace('UniSta', 'Army')
    i = i.replace('Utah State University Eastern', 'USU-E')
    i = i.replace('Van Alstine', 'Van-Alstine')
    i = i.replace('Van Buren', 'Van-Buren')
    i = i.replace('Van Luvanee', 'Van-Luvanee')
    i = i.replace('Van Schenck', 'Van-Schenck')
    i = i.replace('Van Quakebeke', 'Van-Quakebeke')
    i = i.replace('Vander ', 'Vandy ')
    i = i.replace('Vanderbilt ', 'Vandy ')
    i = i.replace('Vanderbilt/', 'Vandy/')
    i = i.replace('Vermon ', 'Vermont ')
    i = i.replace('Wake Forest', 'Wake')
    i = i.replace('WakFor', 'Wake')
    i = i.replace('Washto', 'Washington')
    i = i.replace('WaySta', 'Wayne')
    i = i.replace('Wayne State', 'Wayne')
    i = i.replace('Weber State', 'Weber')
    i = i.replace('WeberSt', 'Weber')
    i = i.replace('WebSta', 'Weber')
    i = i.replace('Western Connecticut State', 'WCSU')
    i = i.replace('WesCon', 'WCSU')
    i = i.replace('Western Connect', 'WCSU')
    i = i.replace('West Georgia', 'UWG')
    i = i.replace('West Ga', 'UWG')
    i = i.replace('WesVir', 'WVU')
    i = i.replace('West Virginia', 'WVU')
    i = i.replace('Whitman College', 'Whitman')
    i = i.replace('WicSta', 'Wichita')
    i = i.replace('Wichita State', 'Wichita')
    i = i.replace('Wisconsin- Madison', 'Wisconsin-Madison')
    i = i.replace('WisMad', 'Wisconsin-Madison')
    i = i.replace('Webster Dunn', 'Webster-Dunn')
    i = i.replace('Wyomin ', 'Wyoming ')

    return i


def open_csv(fpath, outfilename='rounds.csv'):
    # print(fpath)
    file = open(fpath, 'r')
    try:
        reader = csv.reader(file)
        outfile = open(outfilename, 'a')
        writer = csv.writer(outfile)
        next(reader, None)  # skip header
        meta = os.path.basename(fpath)[:-4].split('-')
        year = meta[0]
        tourney = meta[1]
        div = meta[2]
        try:
            rd = meta[3]
        except IndexError:
            print(meta)
            raise IndexError
        meta = [year, tourney, rd, div]
        if 'v' in sys.argv[2]:
            print(meta)
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

            # delete punctuation & initials
            initials = re.compile('^[A-Z][A-Z|a-z]')
            initials_long = re.compile('^[A-Z][a-z][A-Z][a-z]')
            if initials.fullmatch(debate[1]) or \
                    initials_long.fullmatch(debate[1]):
                del debate[1]
            else:
                for i in range(3):
                    del debate[1]
            del debate[2]
            if initials.fullmatch(debate[4]) or \
                    initials_long.fullmatch(debate[4]):
                del debate[4]
            else:
                for i in range(3):
                    del debate[4]
            del debate[5]
            if 'v' in sys.argv[2]:
                print(debate)

            elim_names = ['trips', 'dubs', 'finals', 'octs', 'quarters',
                          'semis']
            possible_decisions = ['Aff', 'Neg']
            num_judges = 0
            if debate[6] == 'BYE':
                debate[7:] = [-1, -1, -1, -1]
            elif meta[2] in elim_names:
                num_judges = int((len(debate) - 6) / 3)
                for i in range(num_judges):  # join judge names
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
                    debate[6 + i:8 + i] = [' '.join(debate[6 + i:8 + i])]
                # clear out ranks (ranks???? why???)
                # need to be careful about interaction w/ zero speaker points
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
            # status_check(debate, num_judges, fpath)

            # add debate to round
            debates.append(debate)
        for debate in debates:
            writer.writerow(debate)
    except UnicodeDecodeError:
        print(f'Error: {fpath}')
    finally:
        file.close()
        outfile.close()
        if len(sys.argv) == 3:
            if 'm' in sys.argv[2]:
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
    with open('rounds.csv', 'r+') as out:
        out.truncate(0)  # clear outfile
    open_multiple(sys.argv[1])
    authenticate_results.read_file('rounds.csv')
