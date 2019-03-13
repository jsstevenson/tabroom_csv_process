import json


def aff_elim_win_at_nats(year):
    with open("rounds-completed.json", "r") as file:
        data = json.load(file)
        tourneys = data[year]
        results = {'ceda': [0, 0], 'ndt': [0, 0]}
        elims = ['trips', 'dubs', 'octs', 'quarters', 'semis', 'finals']
        for tourney in results.keys():
            if tourney in tourneys:
                rounds = tourneys[tourney]
                if 'open' in rounds.keys():
                    open_rounds = rounds['open']
                    for rd in open_rounds:
                        debates = open_rounds[rd]
                        for debate in debates:
                            decisions = debate['decisions']
                            if decisions != ['BYE']:
                                for judge in decisions:
                                    if rd in elims:
                                        results[tourney][1] += 1
                                        if decisions[judge]['winner'] == 'Aff':
                                            results[tourney][0] += 1

        print(f'\n{year}')

        if results['ceda'][1] > 0:
            cedapct = results['ceda'][0] / results['ceda'][1]
            cedan = results['ceda'][1]
            print(f'CEDA: {cedapct:.3f} n={cedan}')
        if results['ndt'][1] > 0:
            ndtpct = results['ndt'][0] / results['ndt'][1]
            ndtn = results['ndt'][1]
            print(f'NDT: {ndtpct:.3f} n={ndtn}')


def aff_prelim_win_at_nats(year):
    with open("rounds-completed.json", "r") as file:
        data = json.load(file)
        tourneys = data[year]
        results = {'ceda': [0, 0], 'ndt': [0, 0]}
        elims = ['trips', 'dubs', 'octs', 'quarters', 'semis', 'finals']
        for tourney in results.keys():
            if tourney in tourneys:
                rounds = tourneys[tourney]
                if 'open' in rounds.keys():
                    open_rounds = rounds['open']
                    for rd in open_rounds:
                        debates = open_rounds[rd]
                        for debate in debates:
                            decisions = debate['decisions']
                            if decisions != ['BYE']:
                                for judge in decisions:
                                    if rd not in elims:
                                        results[tourney][1] += 1
                                        if decisions[judge]['winner'] == 'Aff':
                                            results[tourney][0] += 1

        print(f'\n{year}')

        if results['ceda'][1] > 0:
            cedapct = results['ceda'][0] / results['ceda'][1]
            cedan = results['ceda'][1]
            print(f'CEDA: {cedapct:.3f} n={cedan}')
        if results['ndt'][1] > 0:
            ndtpct = results['ndt'][0] / results['ndt'][1]
            ndtn = results['ndt'][1]
            print(f'NDT: {ndtpct:.3f} n={ndtn}')


def aff_win_at_nats(year):
    with open("rounds-completed.json", "r") as file:
        data = json.load(file)
        tourneys = data[year]
        results = {'ceda': [0, 0], 'ndt': [0, 0]}
        for tourney in results.keys():
            if tourney in tourneys:
                rounds = tourneys[tourney]
                if 'open' in rounds.keys():
                    open_rounds = rounds['open']
                    for rd in open_rounds:
                        debates = open_rounds[rd]
                        for debate in debates:
                            decisions = debate['decisions']
                            if decisions != ['BYE']:
                                for judge in decisions:
                                    results[tourney][1] += 1
                                    if decisions[judge]['winner'] == 'Aff':
                                        results[tourney][0] += 1

        print(f'\n{year}')

        if results['ceda'][1] > 0:
            cedapct = results['ceda'][0] / results['ceda'][1]
            cedan = results['ceda'][1]
            print(f'CEDA: {cedapct:.3f} n={cedan}')
        if results['ndt'][1] > 0:
            ndtpct = results['ndt'][0] / results['ndt'][1]
            ndtn = results['ndt'][1]
            print(f'NDT: {ndtpct:.3f} n={ndtn}')


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
    print(f'\n{year}')
    for i in elims:
        pct = results[i][1] / results[i][0]
        print(f'{i}: {pct:.3f} n = {results[i][0]}')


def majors(year):
    with open("rounds-completed.json", "r") as file:
        data = json.load(file)
        majors = ['gsu', 'umkc', 'weber', 'ky', 'gonz', 'wake', 'cal1', 'cal2',
                  'tx', 'nu']
        elims = ['dubs', 'octs', 'quarters', 'semis', 'finals']
        tourneys = data[year]
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

        print(f'\n{year}')
        print('Prelim results:')
        print(f'{aff_wins_prelim/total_rds_prelim:.3f}')
        print(f'n = {total_rds_prelim}')
        print('Elim results:')
        print(f'{aff_wins_elim/total_rds_elim:.3f}')
        print(f'n = {total_rds_elim}')
        print('Overall:')
        aff_wins_overall = aff_wins_elim + aff_wins_prelim
        total_rds_overall = total_rds_elim + total_rds_prelim
        print(f'{aff_wins_overall / total_rds_overall:.3f}')
        print(f'n = {total_rds_overall}')


def aff_win_nats_vs_all(year):
    with open("rounds-completed.json", "r") as file:
        data = json.load(file)
        tourneys = data[year]
        results = {'ceda': [0, 0], 'ndt': [0, 0], 'regseason': [0, 0]}
        for tourney in tourneys:
            rounds = tourneys[tourney]
            if 'open' in rounds.keys():
                open_rounds = rounds['open']
                for rd in open_rounds:
                    debates = open_rounds[rd]
                    for debate in debates:
                        decisions = debate['decisions']
                        if decisions != ['BYE']:
                            for judge in decisions:
                                if tourney == 'ceda' or tourney == 'ndt':
                                    results[tourney][1] += 1
                                    if decisions[judge]['winner'] == 'Aff':
                                        results[tourney][0] += 1
                                else:
                                    results['regseason'][1] += 1
                                    if decisions[judge]['winner'] == 'Aff':
                                        results['regseason'][0] += 1

        print(f'\n{year}')

        ceda_pct = results['ceda'][0] / results['ceda'][1]
        ndt_pct = results['ndt'][0] / results['ndt'][1]
        reg_pct = results['regseason'][0] / results['regseason'][1]
        print(f'ndt vs reg season: {ndt_pct - reg_pct:.3f}')
        print(f'ceda vs reg season: {ceda_pct - ndt_pct:.3f}')
        print(f'ceda vs ndt: {ceda_pct - ndt_pct:.3f}')


def main():
    print('\nwin pct @ majors')
    majors('1617')
    majors('1718')
    print('\nwin pct by elim @ majors')
    aff_win_by_elim_majors('1718')
    aff_win_by_elim_majors('1617')
    print('\nnationals aff win pct')
    aff_win_at_nats('1314')
    aff_win_at_nats('1415')
    aff_win_at_nats('1516')
    aff_win_at_nats('1617')
    aff_win_at_nats('1718')
    print('\nnationals prelim aff win pct')
    aff_prelim_win_at_nats('1314')
    aff_prelim_win_at_nats('1415')
    aff_prelim_win_at_nats('1516')
    aff_prelim_win_at_nats('1617')
    aff_prelim_win_at_nats('1718')
    print('\nnationals elim aff win pct')
    aff_elim_win_at_nats('1314')
    aff_elim_win_at_nats('1415')
    aff_elim_win_at_nats('1516')
    aff_elim_win_at_nats('1617')
    aff_elim_win_at_nats('1718')
    print('\naff win pct during season vs nats')
    aff_win_nats_vs_all('1617')
    aff_win_nats_vs_all('1718')


if __name__ == '__main__':
    main()
