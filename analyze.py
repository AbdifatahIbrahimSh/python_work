"""Analyzing text files after reading"""


def count_words(filename):
    try: 
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"file {filename} does'nt exist")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"this file ({filename}) contains {num_words} words")

filenames = ['yow.txt', 'lists.txt', 'names.txt', 'pi_digits.txt']

for filename in filenames:
    count_words(filename)