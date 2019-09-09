from collections import defaultdict
import re, sys

def WordFrequency(filename):
    freq_dict = defaultdict(int)
    try:
        file = open(filename)
    except:
        print("Excepotion thrown while trying to open filename: {}".format(filename))
    input_text = file.read()
    file.close()
    input_text_clean = re.sub(r'[^\' a-zA-Z0-9]', ' ', input_text)
    words_list = input_text_clean.split()

    for w in words_list:
        # if w not in stop_words (indent lower line):
        freq_dict[w.lower()] += 1

    sorted_words = sorted(freq_dict, key=freq_dict.get, reverse=True)
    word_count = len(words_list)
    percentages = [freq_dict[w]/word_count for w in sorted_words[0:5]]
    print('MOST COMMON WORDS in {} (word - occurences - percentage rounded to 3 decimals):\n'.format(filename))
    print("({} words total in {})".format(word_count, filename))
    for word, freq in zip(sorted_words[0:5], percentages):
        print("{0}\t {1}\t {2:.3f}%".format(word, freq_dict[word], freq*100))
    return

# (read and split the list of stopwords that you download from the internet)
# stop_words = open("./input_text.txt").read().split("\n")

if sys.argv[0] is not None:
    WordFrequency(str(sys.argv[0]))
else:
    print("Please specify a .txt filename as a command line argument.")
    quit()