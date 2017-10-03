class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

# the '_' indicates not to call the methods directly.
    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives can't be negative")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, levels):
        if levels >= 1:
            level_diff = levels - self._level
            self._score += level_diff * 1000
            self._level = levels
        else:
            print("I'm sorry, level has to be 1 or greater!")

    lives = property(_get_lives, _set_lives)

    level = property(_get_level, _set_level)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)
