# ----------------------------------------------------------------------
# Name:      songstats
# Purpose:   illustrate the use of sets & dictionaries
# Author(s): Shu Sian (Jessie) Lyu, An Tran
# Date: 02/17/2023
# ----------------------------------------------------------------------
"""
implementation of language statistics based on lyrics of two songs

User inputs two text file names that contains the lyrics of songs
For each song, this program compute and print (ignore capitalization):
1. The total number of words in the song.
2. The number of distinct words in the song.
3. The eight most common words in descending order of frequency.
4. The longest word in the song.
5. The words that are 4-letter or longer that appear more than 3
times sorted alphabetically.
Finally, print the words (4-letter or longer) that appear in
both songs, listed alphabetically.
"""
import string


def tally(words):
    """
    Count the words in the word list specified
    :param words: (list of strings) list of lowercase words
    :return: a tally dictionary with items of the form word: count
    """
    words_dic = {}
    for i in words:
        words_dic[i] = words_dic.get(i, 0) + 1

    return words_dic




def most_common(word_count):
    """
    Print the 8 most common words in the dictionary in descending order
    of frequency, with the number of times they appear.

    :param word_count: dictionary with items of the form letter: count
    :return: None
    """
    sorted_word_count = sorted(word_count.items(), key=lambda item: item[1],
                        reverse=True)
    for i in range(8):
        print(f"  {sorted_word_count[i][0]}: appears "
              f"{sorted_word_count[i][1]} times.")

    return None




def repeats(word_count):
    """
    Print the words (4-letter or longer) that appear more than 3
    times alphabetically.
    :param word_count: dictionary with items of the form letter: count
    :return: None
    """
    words = [word for word in word_count if word_count[word] > 3 and len(
        word) >= 4]
    for word in sorted(words):
        print(f"  {word}")

    return None


def get_words(filename):
    """
    Read the file specified, and return a list of all the words,
    converted to lowercase and stripped of punctuation.
    :param filename: (string) Name of the file containing song lyrics
    :return: (list of strings) list of words in lowercase
    """
    with open(filename, "r") as f:
        lyrics = f.read()
        words = [word.lower().strip(string.punctuation) for word in
                 lyrics.split()]

    return words

def get_stats(words):
    """
    Print the statistics corresponding to the list of words specified.
    :param words: (list of strings) list of lowercase words
    :return: None
    """
    # Call the tally function to build the word count dictionary
    # Then call the appropriate functions and print:
    # 1. The eight most common words in the song in descending order of
    #    frequency, with the number of times they appear.
    # 2. The total number of words in the song.
    # 3. The number of distinct words in the song.
    # 4. The words that are 4-letter or longer and that appear more
    #    than 3 times sorted alphabetically.
    # 5. The longest word.
    word_counts = len(words)
    words_dic = tally(words)
    distinct_words = len(words_dic)
    longest = max(words_dic.keys(), key=len)

    print(f"There are {word_counts} words in total in the song.")
    print(f"There are {distinct_words} distinct words in the song.")
    print("The 8 most common words are:")
    most_common(words_dic)
    print(f"The longest word in the song is: {longest}.")
    print("The following (4-letter or longer) words appear more than 3 times:")
    repeats(words_dic)

    return None





def common_words(words1, words2):
    """
    Print the words (4-letter or longer) that appear in both word lists
    in alphabetical order.
    :param words1: (list of stings)
    :param words2: (list of stings)
    :return: None
    """
    if len(words1) >= len(words2):
        commons = set(word for word in words1 if word in words2 and len(word)
                   >= 4)
    else:
        commons = set(word for word in words2 if word in words1 and len(word)
                   >= 4)

    for i in sorted(commons):
        print(i)


def main():
    # Hints:
    # Initialize lists to contain the filenames and the word lists
    # Use a loop to prompt the user for the two filenames
    # and to get the word list corresponding to each file
    # Use a loop to print the statistics corresponding to each song
    # Call common_words to report on the words common to both songs.
    # Enter your code below and take out the pass statement
    filenames = []
    words = []
    for i in range(2):
        filename = input(f"Please enter the filename containing song "
                         f"{i + 1}: ")
        filenames.append(filename)
        words.append(get_words(filenames[i]))

    for i in range(2):
        print(f"Song Statistics: {filenames[i]}")
        get_stats(words[i])
        print("----------------------------------------"
              "----------------------------------------")

    print("The words (4-letter or longer) that appear in both songs:")
    common_words(words[0], words[1])



if __name__ == '__main__':
    main()