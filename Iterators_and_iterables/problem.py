# my_sentence = Sentence("This is a test")

# for word in my_sentence:
#     print(word)
#
# This should have the following output:
# This
# is
# a
# test

# class approach
class Sentence:
    def __init__(self, sentence):
        self.current = 0
        self.words = sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= len(self.words):
            raise StopIteration
        val = self.current
        self.current += 1
        return self.words[val]


my_sentence = Sentence("This is a test")
print("class:")
for word in my_sentence:
    print(word)

# generator approach
def sentence(words):
    # words = words.split()
    # current = 0
    # while current <= len(words):
    #     yield words[current]
    #     current += 1

    # even better
    for word in words.split():
        yield word


my_sentence = Sentence("This is a test")
print("\ngenerator:")
for word in my_sentence:
    print(word)
