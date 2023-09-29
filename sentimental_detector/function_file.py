from nltk.tokenize import word_tokenize

# nltk.download('punkt') # Uncomment if download issue
# Filtering Words Packages
# nltk.download("stopwords") # Uncomment if download issue

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from function_file import*
import json

# Declare Stopwords
stop_words = set(stopwords.words("english"))
additional_stopwords = ["!", ".", ",", "'s", "\"", "\'"]
for word in additional_stopwords:
    stop_words.add(word)

def lower_case_array(array):
    for i in range(len(array)):
        array[i] = array[i].lower()
    return array

def string_to_token_array(string):
    string_array = lower_case_array(word_tokenize(string))
    token_array = []
    # print("reached")
    for token in string_array:
        repeated = False
        for stop_word in stop_words:
            if stop_word == token:
                repeated = True
                break
        if repeated is False:
            token_array.append(token)
            # print(file_word)
    return token_array

def file_into_tokens(filename):
    # Reading Files
    file_txt = open(filename, 'r') # Open file
    file_string = file_txt.read() # Reading the entire file
    file_txt.close()

    token_array = string_to_token_array(file_string)

    return token_array

def count_words(token_set, line):
    word_dictionary = {"word": 1}

    unique_words = []
    for token in token_set:
        existing_word = False
        for dictionary in word_dictionary:
            if dictionary == token:
                word_dictionary[dictionary] = word_dictionary[dictionary] + 1
                existing_word = True
        if not existing_word:
            word_dictionary[token] = 1
            unique_words.append(token)
    write_to_file("percentages.txt", line, str(json.dumps(word_dictionary)))

# def write_to_file(filename, message):
#     with open(filename, 'w') as file:
#         file.write(message)

def write_to_file(filename, line, message):
    # Source: https://stackoverflow.com/questions/4719438/editing-specific-line-in-text-file-in-python
    with open(filename, 'r') as file: # Read lines in the file
        data = file.readlines()

    data[line-1] = message + "\n" # Replace the line

    # and write everything back
    with open(filename, 'w') as file:
        file.writelines(data)

def readline(file, line):
    file = open(file)
    r = file.readlines()
    # print(r[line-1])
    return r[line-1]

def p_quotient(occurrence, total):
    p = float(occurrence / total)
    # print(p)
    return p


