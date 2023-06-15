class DiaryEntry():
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        pass

    def count_words(self):
        return len(self.contents.split())

