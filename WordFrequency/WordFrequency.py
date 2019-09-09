from collections import defaultdict
import re, sys

stops = open('stopwords.txt')
stopwords = set(line.rstrip('\n') for line in stops)
stops.close()

def WordFrequency(filename):
    freq_dict = defaultdict(int)
    freq_dict_nostops = defaultdict(int)
    try:
        file = open(filename)
    except:
        print("Exception thrown while trying to open filename: {}".format(filename))
    input_text = file.read()
    file.close()
    input_text_clean = re.sub(r'[^\' a-zA-Z0-9]', ' ', input_text)
    words_list = input_text_clean.split()

    for w in words_list:
        freq_dict[w.lower()] += 1
        if w.lower() not in stopwords:
            freq_dict_nostops[w.lower()] += 1
            

    sorted_words = sorted(freq_dict, key=freq_dict.get, reverse=True)
    word_count = len(words_list)
    percentages = [freq_dict[w]/word_count for w in sorted_words[0:5]]
    print('MOST COMMON WORDS in {} (word - occurences - percentage rounded to 3 decimals):\n'.format(filename))
    print("({} words total in {})".format(word_count, filename))
    for word, freq in zip(sorted_words[0:5], percentages):
        print("{0}\t {1}\t {2:.3f}%".format(word, freq_dict[word], freq*100))

    print('\n\n')

    sorted_words_nostops = sorted(freq_dict_nostops, key=freq_dict_nostops.get, reverse=True)
    percentages_nostops = [freq_dict_nostops[w]/word_count for w in sorted_words_nostops[0:5]]
    print('MOST COMMON WORDS in {} (stopwords removed):\n'.format(filename))
    print("({} words total in {})".format(word_count, filename))
    for word, freq in zip(sorted_words_nostops[0:5], percentages_nostops):
        print("{0}\t {1}\t {2:.3f}%".format(word, freq_dict_nostops[word], freq*100))
    return

if sys.argv[1] is not None:
    WordFrequency(str(sys.argv[1]))
else:
    print("Please specify a .txt filename as a command line argument.")
    quit()