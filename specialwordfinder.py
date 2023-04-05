from wordfinder import WordFinder
import random

class SpecialWordFinder(WordFinder):
    def __init__(self, location):
        super().__init__(location)
        self.get_filtered_file()
    
    def get_filtered_file(self):
        filter = []
        for line in self.words:
            if "#" not in line and line != "":
                filter.append(line)
        self.filtered = filter

    def filter_random(self):
        print(random.choice(self.filtered))

wf = SpecialWordFinder("words.txt")
wf.filter_random()
wf.filter_random()
wf.filter_random()
