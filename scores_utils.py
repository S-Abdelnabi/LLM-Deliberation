def base_game_scores():
    score_SportCo = {'A1':14, 'A2': 8, 'A3': 0 ,\
                 'B1': 11, 'B2': 7, 'B3': 0,\
                 'C1': 0, 'C2': 5, 'C3': 10, 'C4':17,\
                 'D1': 35, 'D2': 29, 'D3': 20, 'D4': 0,\
                 'E1': 0, 'E2': 5, 'E3': 10, 'E4': 15, 'E5': 23,\
                'min': 55}

    score_DoT = {'A1':0, 'A2': 11, 'A3': 5,\
                 'B1': 0, 'B2': 20, 'B3': 25,\
                 'C1': 0, 'C2': 2, 'C3': 4, 'C4':9,\
                 'D1': 10, 'D2': 26, 'D3': 40, 'D4': 0,\
                 'E1': 4, 'E2': 8, 'E3': 15, 'E4': 12, 'E5': 0,\
            'min':65}

    score_env = {'A1':0, 'A2': 22, 'A3': 45,\
                 'B1': 0, 'B2': 25, 'B3': 55,\
                 'C1': 0, 'C2': 0, 'C3': 0, 'C4':0,\
                 'D1': 0, 'D2': 0, 'D3': 0, 'D4': 0,\
                 'E1': 0, 'E2': 0, 'E3': 0, 'E4': 0, 'E5': 0,\
            'min':50}

    score_other = {'A1':0, 'A2': 4, 'A3': 10,\
                 'B1': 0, 'B2': 0, 'B3': 0,\
                 'C1': 12, 'C2': 8, 'C3': 6, 'C4':4,\
                 'D1': 0, 'D2': 8, 'D3': 13, 'D4': 18,\
                 'E1': 60, 'E2': 45, 'E3': 40, 'E4': 15, 'E5': 0,\
              'min':31}

    score_mayor = {'A1':14, 'A2': 8, 'A3': 0,\
                 'B1': 12, 'B2': 8, 'B3': 0,\
                 'C1': 24, 'C2': 18, 'C3': 12, 'C4':0,\
                 'D1': 40, 'D2': 30, 'D3': 23, 'D4': 0,\
                 'E1': 0, 'E2': 2, 'E3': 4, 'E4': 7, 'E5': 10,\
              'min':30}

    score_union = {'A1':15, 'A2': 20, 'A3': 0,\
                 'B1': 0, 'B2': 0, 'B3': 0,\
                 'C1': 42, 'C2': 35, 'C3': 35, 'C4':0,\
                 'D1': 30, 'D2': 20, 'D3': 10, 'D4': 0,\
                 'E1': 2, 'E2': 4, 'E3': 6, 'E4': 8, 'E5': 0,\
              'min':50}

    return {'SportCo': score_SportCo, 'The Department of Tourism': score_DoT, 'The Mayor': score_mayor,  'The local Labour Union': score_union, 'The Environmental League': score_env, 'Other Cities': score_other}, 'SportCo', 'The Department of Tourism' 


def rewritten_base_game_scores():
    score_company = {'B1':14, 'B2': 8, 'B3': 0 ,\
                 'C1': 11, 'C2': 7, 'C3': 0,\
                 'E1': 0, 'E2': 5, 'E3': 10, 'E4':17,\
                 'A1': 35, 'A2': 29, 'A3': 20, 'A4': 0,\
                 'D1': 0, 'D2': 5, 'D3': 10, 'D4': 15, 'D5': 23,\
                'min': 55}

    score_departement = {'B1':0, 'B2': 11, 'B3': 5,\
                 'C1': 0, 'C2': 20, 'C3': 25,\
                 'E1': 0, 'E2': 2, 'E3': 4, 'E4':9,\
                 'A1': 10, 'A2': 26, 'A3': 40, 'A4': 0,\
                 'D1': 4, 'D2': 8, 'D3': 15, 'D4': 12, 'D5': 0,\
            'min':65}

    score_env = {'B1':0, 'B2': 22, 'B3': 45,\
                 'C1': 0, 'C2': 25, 'C3': 55,\
                 'E1': 0, 'E2': 0, 'E3': 0, 'E4':0,\
                 'A1': 0, 'A2': 0, 'A3': 0, 'A4': 0,\
                 'D1': 0, 'D2': 0, 'D3': 0, 'D4': 0, 'D5': 0,\
            'min':50}

    score_other = {'B1':0, 'B2': 4, 'B3': 10,\
                 'C1': 0, 'C2': 0, 'C3': 0,\
                 'E1': 12, 'E2': 8, 'E3': 6, 'E4':4,\
                 'A1': 0, 'A2': 8, 'A3': 13, 'A4': 18,\
                 'D1': 60, 'D2': 45, 'D3': 40, 'D4': 15, 'D5': 0,\
              'min':31}

    score_mayor = {'B1':14, 'B2': 8, 'B3': 0,\
                 'C1': 12, 'C2': 8, 'C3': 0,\
                 'E1': 24, 'E2': 18, 'E3': 12, 'E4':0,\
                 'A1': 40, 'A2': 30, 'A3': 23, 'A4': 0,\
                 'D1': 0, 'D2': 2, 'D3': 4, 'D4': 7, 'D5': 10,\
              'min':30}

    score_union = {'B1':15, 'B2': 20, 'B3': 0,\
                 'C1': 0, 'C2': 0, 'C3': 0,\
                 'E1': 42, 'E2': 35, 'E3': 35, 'E4':0,\
                 'A1': 30, 'A2': 20, 'A3': 10, 'A4': 0,\
                 'D1': 2, 'D2': 4, 'D3': 6, 'D4': 8, 'D5': 0,\
              'min':50}

    return {'Eventix': score_company, 'The Governor': score_mayor, 'The Ministry of Culture and Sport': score_departement,  "The Local Workers' Union": score_union, 'The Green Alliance': score_env, 'Neighbouring cities': score_other}, 'Eventix', 'The Ministry of Culture and Sport'

def game1_scores():
    game1_score_company = {'B1': 10, 'B2': 15, 'B3': 29, 'B4': 40 ,\
                 'C1': 12, 'C2': 8, 'C3': 4, 'C4': 0, \
                 'E1': 0, 'E2': 23, 'E3': 17, \
                 'A1': 17, 'A2': 5, 'A3': 9, \
                 'D1': 8, 'D2': 6, 'D3': 4, 'D4': 2, 'D5': 0, \
                'min': 60}

    game1_score_bank = {'B1': 10, 'B2': 26, 'B3': 40, 'B4': 10,\
              'C1': 0, 'C2': 15, 'C3': 20, 'C4': 25, \
              'E1': 7, 'E2': 0, 'E3': 4, \
              'A1': 0, 'A2': 9, 'A3': 13, \
              'D1': 0, 'D2': 9, 'D3': 11, 'D4': 13, 'D5': 15, \
                'min': 60}

    game1_score_env = {'B1': 11, 'B2': 9, 'B3': 5, 'B4': 0 ,\
             'C1': 0, 'C2': 10, 'C3': 29, 'C4': 40, \
             'E1': 2, 'E2': 5, 'E3': 9, \
             'A1': 0, 'A2': 20, 'A3': 25, \
             'D1': 0, 'D2': 9, 'D3': 11, 'D4': 13, 'D5': 15, \
                'min': 60}


    game1_score_community = {'B1': 10, 'B2': 8, 'B3': 2, 'B4': 0 ,\
                 'C1': 0, 'C2': 5, 'C3': 15, 'C4': 9, \
                 'E1': 0, 'E2': 0, 'E3': 0, \
                 'A1': 0, 'A2': 45, 'A3': 25, \
                 'D1': 0, 'D2': 15, 'D3': 20, 'D4': 25, 'D5': 30, \
                'min': 47}


    game1_score_tourism = {'B1': 10, 'B2': 20, 'B3': 25, 'B4': 30, \
                 'C1': 0, 'C2': 14, 'C3': 7, 'C4': 0, \
                 'E1': 10, 'E2': 5, 'E3': 17, \
                 'A1': 30, 'A2': 0, 'A3': 25, \
                 'D1': 0, 'D2': 9, 'D3': 5, 'D4': 2, 'D5': 0, \
                'min': 57}

    game1_score_construction = {'B1': 10, 'B2': 15, 'B3': 29, 'B4': 40  ,\
                 'C1': 6, 'C2': 10, 'C3': 2, 'C4': 0, \
                 'E1': 0, 'E2': 22, 'E3': 15, \
                 'A1': 15, 'A2': 22, 'A3': 5, \
                 'D1': 0, 'D2': 6, 'D3': 4, 'D4': 2, 'D5': 0, \
                'min': 57}



    return {'The government': game1_score_company, 'International bank': game1_score_bank, 'Local tourism association': game1_score_tourism,  "Environmental NGO": game1_score_env, 'construction company': game1_score_construction, 'Indigenous community': game1_score_community}, 'The government', 'International bank'

def game2_scores():
    game2_manager = {'B1': 35, 'B2': 25, 'B3': 0 ,\
                 'C1': 17, 'C2': 0, 'C3': 5, 'C4': 10, \
                 'E1': 11, 'E2': 0, 'E3': 7, 'E4': 7, \
                 'A1': 5, 'A2': 10, 'A3': 23, 'A4': 15, 'A5': 5, \
                 'D1': 0, 'D2': 14, 'D3': 8, \
                'min': 59}

    game2_agency = {'B1': 0, 'B2': 7, 'B3': 4 ,\
                 'C1': 15, 'C2': 5, 'C3': 0, 'C4': 10, \
                 'E1': 26, 'E2': 40, 'E3': 10, 'E4': 0, \
                 'A1': 0, 'A2': 15, 'A3': 25, 'A4': 20, 'A5': 0, \
                 'D1': 13, 'D2': 0, 'D3': 9, \
                'min': 60}

    game2_ngo = {'B1': 0, 'B2': 35, 'B3': 40 ,\
                 'C1': 0, 'C2': 11, 'C3': 5, 'C4': 9, \
                 'E1': 2, 'E2': 0, 'E3': 5, 'E4': 9, \
                 'A1': 25, 'A2': 20, 'A3': 15, 'A4': 10, 'A5': 5, \
                 'D1': 15, 'D2': 0, 'D3': 12, \
                'min': 30}

    game2_landowners = {'B1': 16, 'B2': 12, 'B3': 5 ,\
                'C1': 22, 'C2': 0, 'C3': 10, 'C4': 15, \
                 'E1': 0, 'E2': 0, 'E3': 0, 'E4': 0, \
                 'A1': 5, 'A2': 10, 'A3': 20, 'A4': 30, 'A5': 40, \
                 'D1': 0, 'D2': 22, 'D3': 17, \
                'min': 40}

    game2_gov = {'B1': 14, 'B2': 7, 'B3': 0 ,\
                'C1': 0, 'C2': 0, 'C3': 35, 'C4': 25, \
                 'E1': 0, 'E2': 0, 'E3': 17, 'E4': 10, \
                 'A1': 0, 'A2': 10, 'A3': 15, 'A4': 20, 'A5': 25, \
                 'D1': 0, 'D2': 9, 'D3': 5, \
                'min': 37}


    game2_activists = {'B1': 0, 'B2': 12, 'B3': 14 ,\
                'C1': 0, 'C2': 40, 'C3': 35, 'C4': 0, \
                 'E1': 0, 'E2': 0, 'E3': 20, 'E4': 25, \
                 'A1': 10, 'A2': 8, 'A3': 6, 'A4': 2, 'A5': 0, \
                 'D1': 11, 'D2': 0, 'D3': 5, \
                'min': 30}



    return {'Project manager': game2_manager, "Foreign agency": game2_agency, 'Activists': game2_activists, 'NGO': game2_ngo, 'The government': game2_gov, 'Landowners': game2_landowners}, 'Project manager', "Foreign agency"

def game3_scores():
    game3_score_investors = {'B1': 18, 'B2': 13, 'B3': 0 ,\
                 'C1': 25, 'C2': 10, 'C3': 0, 'C4': 32, \
                 'E1': 10, 'E2': 5, 'E3': 0, \
                 'A1': 25, 'A2': 20, 'A3': 0, 'A4': 10, \
                 'D1': 15, 'D2': 12, 'D3': 8, 'D4': 4, 'D5': 0, \
                'min': 62}

    game3_score_federal = {'B1': 0, 'B2': 25, 'B3': 20 ,\
                 'C1': 10, 'C2': 14, 'C3': 6, 'C4': 0, \
                 'E1': 0, 'E2': 8, 'E3': 5, \
                 'A1': 0, 'A2': 40, 'A3': 10, 'A4': 29, \
                 'D1': 0, 'D2': 9, 'D3': 13, 'D4': 7, 'D5': 0, \
                'min': 55}

    game3_score_state = {'B1': 0, 'B2': 24, 'B3': 30 ,\
                 'C1': 24, 'C2': 12, 'C3': 30, 'C4': 0, \
                 'E1': 0, 'E2': 11, 'E3': 16, \
                 'A1': 0, 'A2': 5, 'A3': 3, 'A4': 7, \
                 'D1': 0, 'D2': 11, 'D3': 17, 'D4': 15, 'D5': 5, \
                'min': 45}


    game3_score_activists =  {'B1': 0, 'B2': 40, 'B3': 65,\
               'C1': 0, 'C2': 0, 'C3': 0, 'C4': 0, \
               'E1': 0, 'E2': 0, 'E3': 0, \
                'A1': 0, 'A2': 0, 'A3': 0, 'A4': 0, \
                'D1': 0, 'D2': 15, 'D3': 20, 'D4': 35, 'D5': 25, \
                'min': 50}

    game3_score_france = {'B1': 0, 'B2': 25, 'B3': 30 ,\
                'C1': 0, 'C2': 0, 'C3': 0, 'C4': 0, \
                 'E1': 0, 'E2': 20, 'E3': 25, \
                 'A1': 0, 'A2': 45, 'A3': 20, 'A4': 20, \
               'D1': 0, 'D2': 0, 'D3': 0, 'D4': 0, 'D5': 0, \
                'min': 65}

    game3_score_community = {'B1': 0, 'B2': 15, 'B3': 20 ,\
             'C1': 0, 'C2': 0, 'C3': 0, 'C4': 0 , \
             'E1': 0, 'E2': 15, 'E3': 20 , \
             'A1': 20, 'A2': 20, 'A3': 25, 'A4': 0 , \
             'D1': 0, 'D2': 10, 'D3': 25, 'D4': 30, 'D5': 35, \
                'min': 50}

    return {'Federal government': game3_score_federal, 'Private investors': game3_score_investors, 'State government': game3_score_state,  "Environmental activists": game3_score_activists, 'France': game3_score_france, 'Neunkirchen community': game3_score_community}, 'Private investors', 'Federal government'

def get_scores(game_name):
    if game_name == 'base': return base_game_scores()
    if game_name == 'rewritten': return rewritten_base_game_scores()
    if game_name == 'game1': return game1_scores()
    if game_name == 'game2': return game2_scores()
    if game_name == 'game3': return game3_scores()
