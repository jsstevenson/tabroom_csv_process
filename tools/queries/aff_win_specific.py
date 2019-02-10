import json


def aff_win_by_elim_majors(year):
    with open("rounds-completed.json", "r") as file:
        data = json.load(file)
        majors = ['gsu', 'umkc', 'weber', 'ky', 'gonz', 'wake', 'cal1', 'cal2',
                  'tx', 'nu']
        elims = ['dubs', 'octs', 'quarters', 'semis', 'finals']
        tourneys = data[year]
        results = {'dubs': [0, 0], 'octs': [0, 0], 'quarters': [0, 0], 
                   'semis': [0, 0], 'finals': [0, 0]}
        for tourney in majors:
            if tourney in tourneys:
                rounds = tourneys[tourney]
                open_rounds = rounds['open']
                for rd in open_rounds:
                    if rd in elims:
                        debates = open_rounds[rd]
                        for debate in debates:
                            decisions = debate['decisions']
                            if decisions != ['BYE']:
                                for judge in decisions:
                                    results[rd][0] += 1
                                    if decisions[judge]['winner'] == 'Aff':
                                        results[rd][1] += 1
    print(f'\nresults for year {year}')
    for i in elims:
        pct = results[i][1] / results[i][0]
        print(f'{i}: {pct:.3f} n = {results[i][0]}')


def majors_1718():
    with open("rounds-completed.json", "r") as file:
        data = json.load(file)
        majors = ['gsu', 'umkc', 'weber', 'ky', 'gonz', 'wake', 'cal1', 'cal2',
                  'tx', 'nu']
        elims = ['dubs', 'octs', 'quarters', 'semis', 'finals']
        tourneys = data['1718']
        aff_wins_prelim = 0
        total_rds_prelim = 0
        aff_wins_elim = 0
        total_rds_elim = 0
        for tourney in majors:
            if tourney in tourneys:
                rounds = tourneys[tourney]
                open_rounds = rounds['open']
                for rd in open_rounds:
                    debates = open_rounds[rd]
                    for debate in debates:
                        decisions = debate['decisions']
                        if decisions != ['BYE']:
                            for judge in decisions:
                                if rd not in elims:
                                    total_rds_prelim += 1
                                elif rd in elims:
                                    total_rds_elim += 1
                                if decisions[judge]['winner'] == 'Aff':
                                    if rd not in elims:
                                        aff_wins_prelim += 1
                                    elif rd in elims:
                                        aff_wins_elim += 1

        print('\n2017-18 aff win data')
        print('Prelim results:')
        print(aff_wins_prelim/total_rds_prelim)
        print(f'n = {total_rds_prelim}')
        print('\nElim results:')
        print(aff_wins_elim/total_rds_elim)
        print(f'n = {total_rds_elim}')
        print('\nOverall:')
        aff_wins_overall = aff_wins_elim + aff_wins_prelim
        total_rds_overall = total_rds_elim + total_rds_prelim
        print(aff_wins_overall / total_rds_overall)
        print(f'n = {total_rds_overall}')


def majors_1617():
    with open("rounds-completed.json", "r") as file:
        data = json.load(file)
        majors = ['gsu', 'umkc', 'weber', 'ky', 'gonz', 'wake', 'cal1', 'cal2',
                  'tx', 'nu']
        elims = ['dubs', 'octs', 'quarters', 'semis', 'finals']
        tourneys = data['1617']
        aff_wins_prelim = 0
        total_rds_prelim = 0
        aff_wins_elim = 0
        total_rds_elim = 0
        for tourney in majors:
            if tourney in tourneys:
                rounds = tourneys[tourney]
                open_rounds = rounds['open']
                for rd in open_rounds:
                    debates = open_rounds[rd]
                    for debate in debates:
                        decisions = debate['decisions']
                        if decisions != ['BYE']:
                            for judge in decisions:
                                if rd not in elims:
                                    total_rds_prelim += 1
                                elif rd in elims:
                                    total_rds_elim += 1
                                if decisions[judge]['winner'] == 'Aff':
                                    if rd not in elims:
                                        aff_wins_prelim += 1
                                    elif rd in elims:
                                        aff_wins_elim += 1

        print('2016-17 aff win data')
        print('Prelim results:')
        print(aff_wins_prelim/total_rds_prelim)
        print(f'n = {total_rds_prelim}')
        print('\nElim results:')
        print(aff_wins_elim/total_rds_elim)
        print(f'n = {total_rds_elim}')
        print('\nOverall:')
        aff_wins_overall = aff_wins_elim + aff_wins_prelim
        total_rds_overall = total_rds_elim + total_rds_prelim
        print(aff_wins_overall / total_rds_overall)
        print(f'n = {total_rds_overall}')


def main():
    majors_1617()
    majors_1718()
    aff_win_by_elim_majors('1718')
    aff_win_by_elim_majors('1617')


if __name__ == '__main__':
    main()
