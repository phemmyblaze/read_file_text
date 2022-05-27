# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    file = open("story.txt", "r")
    count = 0
    for line in file:
        words = line.split(" ")
        count += len(words)
    file.close()
    print("Number of words in a Text :", count)

    return "Hello World"


read_file_content("story.txt")

details = input('Enter file: ')
if len(details) < 1:
    details = './story.txt'
hand = open(details)

bi = dict()
for line in hand:
    line = line.rstrip()
    wds = line.split()
    for word in wds:
        bi[word] = bi.get(word, 0) + 1


print(bi)

largest = -1
theword = None
for k, v in bi.items():
    if v > largest:
        largest = v
        theword = k

print('This is the highest occurence word', theword, largest)
