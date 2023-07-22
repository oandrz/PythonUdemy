import pandas


class DataManager:

    def __init__(self, path):
        self.path = path

    def get_words(self):
        try:
            return pandas.read_csv("./data/words_to_learn.csv").to_dict(orient="records")
        except (pandas.errors.EmptyDataError, FileNotFoundError):
            return pandas.read_csv(self.path).to_dict(orient="records")

    def save_remaining_words(self, words):
        to_save = pandas.DataFrame(words)
        to_save.to_csv("./data/words_to_learn.csv", index=False) # set to false to not add index number when save to csv
