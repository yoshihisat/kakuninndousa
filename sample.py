from diaries.AbstractDiary import AbstractDiary


class DiarySample(AbstractDiary):

    def get_date(self):
        return "2020-12-2"

    def get_summary(self):
        return "久しぶりにランチを食べた．"

    def get_author(self):
        return "good"