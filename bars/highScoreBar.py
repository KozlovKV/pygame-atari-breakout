from bars.baseTextBar import TextBar
from bars.scoreBar import ScoreBar

from constants import MAIN_FONT


class HighScoreTable:
    def __init__(self, screen):
        self.screen = screen
        self.score_strings = list()
        self.read_scores()

    def __del__(self):
        self.write_scores()

    def read_scores(self):
        with open('./data/highscores.txt', 'r') as fin:
            [self.score_strings.append(score.strip().split(' '))
             for score in fin.readlines()]
            for score in self.score_strings:
                score[1] = int(score[1])

    def write_scores(self):
        with open('./data/highscores.txt', 'w') as fout:
            out_strings = [score[0] + ' ' + str(score[1]) + '\n'
                           for score in self.score_strings]
            fout.writelines(out_strings)

    def add_new_score(self, score: str):
        self.score_strings.append([score.split(' ')[0],
                                   int(score.split(' ')[1])])
        self.sort_scores()

    def sort_scores(self):
        for i in range(len(self.score_strings)):
            for j in range(1, len(self.score_strings) - i):
                if self.score_strings[j - 1][1] > self.score_strings[j][1]:
                    self.score_strings[j - 1], self.score_strings[j] = \
                        self.score_strings[j], self.score_strings[j - 1]

    def draw(self):
        pass
