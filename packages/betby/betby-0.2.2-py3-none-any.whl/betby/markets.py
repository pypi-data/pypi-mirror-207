import numpy as np
from math import exp, factorial

class Get_markets:
    def __init__(self, avg_1, avg_2, score_1=0, score_2=0, time=0,
                 time_full=93, time_block=90, matrix=None, poisson=False,
                 result=None):
        self.avg_1 = avg_1
        self.avg_2 = avg_2
        self.score_1 = score_1
        self.score_2 = score_2
        self.time = time
        self.time_full = time_full
        self.time_block = time_block
        self.matrix = matrix
        self.poisson = poisson
        self.result = {} if result is None else result

    # округление кэфов
    def kf_round(a, max):
        if a < 3.5:
            a = math.floor(a * 100) / 100
        elif a < 10:
            a = math.floor(a * 10) / 10
        elif a < max:
            a = math.floor(a)
        else:
            a = max
        if a > max:
            a = max
        return a

        # print(kf_round(1.85, 17))

    # расчет маржи, кэфы на победу низкие
    def margin(kf, m=0.075, max=25):

        k_0 = 22 * 0.045 / m  # убывающая прямая
        v_0 = (-m + 0.23 - 0.5 / k_0) / (
                0.23 - 1 / k_0)  # предельная вер
        m_0 = 0.23 * (1 - v_0)
        n_0 = (1.5 - 1 / k_0) / (
                1.5 - 0.23)  # показатель (производная)
        ver = 0.5 + abs(1 / kf - 0.5)
        mar_1 = m - (ver - 0.5) / k_0
        mar_2 = 1.5 * (1 - ver) - (1.5 - 0.23) * (
                1 - v_0) * ((1 - ver) / (1 - v_0)) ** n_0
        if ver >= v_0:
            kf_v = (1 - mar_2) / ver
        else:
            kf_v = (1 - mar_1) / ver
        if 1 / kf >= 0.5:
            kf = kf_round(kf_v, max)
        else:
            kf = kf_round((1 - m) * kf_v / (kf_v - 1 + m), max)
        return kf

    def get_matrix(self):
        avg_1 = self.avg_1 * (time_full - time) / time_full
        avg_2 = self.avg_2 * (time_full - time) / time_full
        if poisson:
            matrix = np.zeros((poisson, poisson))
            for i in range(poisson):
                for j in range(poisson):
                    prob = (exp(-avg_1) * avg_1 ** i / factorial(i)) * (
                                exp(-avg_2) * avg_2 ** j / factorial(j))
                    matrix[i, j] = prob

    def total(mar=0.05, min_prob=0.2, max_odds=25):
        prob = 0
        result.update({'TOTAL': {'outcomes': []}})
        for val in range(2 * poisson):
            for i in range(poisson):
                for j in range(poisson):
                    if i + j < val + 0.5:
                        prob += matrix[i, j]
            if prob >= min_prob and prob <= 1 - min_prob:
                result['TOTAL']['outcomes'].append({
                    'spec_' + str(val + 0.5): str(val + 0.5),
                    'over': {'prob': 1 - prob, 'margin': mar,
                             'ODDS': margin(1 / (1 - prob), mar, max_odds),
                             'block': 0},
                    'under': {'prob': prob, 'margin': mar,
                              'ODDS': margin(1 / prob, mar, max_odds),
                              'block': 0}
                })
            prob = 0

    def handicap(mar=0.05, min_prob=0.2, max_odds=25):
        prob = 0
        result.update({'HANDICAP': {'outcomes': []}})
        for val in range(1 - poisson, poisson):
            for i in range(poisson):
                for j in range(poisson):
                    if j - i > val + 0.5:
                        prob += matrix[i, j]
            if prob >= min_prob and prob <= 1 - min_prob:
                result['HANDICAP']['outcomes'].append({
                    'spec_' + str(val + 0.5): str(val + 0.5),
                    'H1': {'prob': 1 - prob, 'margin': mar,
                           'ODDS': margin(1 / (1 - prob), mar, max_odds),
                           'block': 0},
                    'H2': {'prob': prob, 'margin': mar,
                           'ODDS': margin(1 / prob, mar, max_odds),
                           'block': 0}
                })
            prob = 0

    def home_total(mar=0.05, min_prob=0.2, max_odds=25):
        prob = 0
        result.update({'HOME_TOTAL': {'outcomes': []}})
        for val in range(poisson):
            for i in range(poisson):
                for j in range(poisson):
                    if i < val + 0.5:
                        prob += matrix[i, j]
            if prob >= min_prob and prob <= 1 - min_prob:
                result['HOME_TOTAL']['outcomes'].append({
                    'spec_' + str(val + 0.5): str(val + 0.5),
                    'over': {'prob': 1 - prob, 'margin': mar, 'ODDS':
                        margin(1 / (1 - prob), mar, max_odds), 'block': 0},
                    'under': {'prob': prob, 'margin': mar, 'ODDS': margin(
                        1 / prob, mar, max_odds), 'block': 0}
                })
            prob = 0

    def away_total(mar=0.05, min_prob=0.2, max_odds=25):
        prob = 0
        result.update({'AWAY_TOTAL': {'outcomes': []}})
        for val in range(poisson):
            for i in range(poisson):
                for j in range(poisson):
                    if j < val + 0.5:
                        prob += matrix[i, j]
            if prob >= min_prob and prob <= 1 - min_prob:
                result['AWAY_TOTAL']['outcomes'].append({
                    'spec_' + str(val + 0.5): str(val + 0.5),
                    'over': {'prob': 1 - prob, 'margin': mar,
                             'ODDS': margin(1 / (1 - prob), mar,
                                            max_odds), 'block': 0},
                    'under': {'prob': prob, 'margin': mar,
                              'ODDS': margin(1 / prob, mar, max_odds),
                              'block': 0}
                })
            prob = 0