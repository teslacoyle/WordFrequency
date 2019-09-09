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
        return
    input_text = file.read()
    file.close()
    input_text_clean = re.sub(r'[^\' a-zA-Z0-9]', ' ', input_text)
    words_list = input_text_clean.split()

    for w in words_list:
        freq_dict[w.lower()] += 1
        if w.lower() not in stopwords:
            freq_dict_nostops[w.lower()] += 1
    
    output = []     
    sorted_words = sorted(freq_dict, key=freq_dict.get, reverse=True)
    word_count = len(words_list)
    percentages = [freq_dict[w]/word_count for w in sorted_words[0:5]]
    output.append('MOST COMMON WORDS in {} (word - occurences - percentage rounded to 3 decimals):\n'.format(filename))
    output.append("({} words total in {})\n".format(word_count, filename))
    for word, freq in zip(sorted_words[0:5], percentages):
        output.append("{0}\t {1}\t {2:.3f}%\n".format(word, freq_dict[word], freq*100))

    output.append('\n')

    sorted_words_nostops = sorted(freq_dict_nostops, key=freq_dict_nostops.get, reverse=True)
    percentages_nostops = [freq_dict_nostops[w]/word_count for w in sorted_words_nostops[0:5]]
    output.append('MOST COMMON WORDS in {} (stopwords removed):\n'.format(filename))
    output.append("({} words total in {})\n".format(word_count, filename))
    for word, freq in zip(sorted_words_nostops[0:5], percentages_nostops):
        output.append("{0}\t {1}\t {2:.3f}%\n".format(word, freq_dict_nostops[word], freq*100))
    
    with open('{}_output.txt'.format(filename.split('.')[0]), 'w') as outfile:
        outfile.writelines(output)
    return

if sys.argv[1] is not None:
    WordFrequency(str(sys.argv[1]))
else:
    print("Please specify a .txt filename as a command line argument.")
    quit()