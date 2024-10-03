from mrjob.job import MRJob
import enchant
import re

english_dict = enchant.Dict("en_US")
WORD_RE = re.compile(r"\b\w+\b")

class NonEnglishWordCount(MRJob):

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            word_lower = word.lower()
            if not english_dict.check(word_lower):
                yield word_lower, 1

    def reducer(self, word, counts):
        yield word, sum(counts)

if __name__ == "__main__":
    NonEnglishWordCount.run()