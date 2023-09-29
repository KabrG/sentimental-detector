import sys
import os
import nltk
from nltk.tokenize import word_tokenize

# nltk.download('punkt') # Uncomment if download issue
# Filtering Words Packages
# nltk.download("stopwords") # Uncomment if download issue

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from function_file import*

# stop_words = set(stopwords.words("english"))
# additional_stopwords = ["!", ".", ","]
# for word in additional_stopwords:
#     stop_words.add(word)

# Positive reviews
positive_tokens = file_into_tokens('positive_reviews.txt')
negative_tokens = file_into_tokens('negative_reviews.txt')
total_words = len(positive_tokens) + len(negative_tokens)
print("Total words", total_words)

count_words(positive_tokens, 2)
count_words(negative_tokens, 4)

# Import the dictionaries
# Format for JSON files
positive_dict = json.loads(readline('percentages.txt', 2))
negative_dict = json.loads(readline('percentages.txt', 4))

while(1):

    og_phrase = str(input("Give a phrase: "))
    phrase = string_to_token_array(og_phrase)
    print("Phrase:", phrase)

    # Positive Prob.

    p_positive_multiplier_array = []
    p_negative_multiplier_array = []

    # Positive Case
    for token in phrase:
        existence = False # Does it already exist in the data set?
        for i in positive_dict:
            if token == i:
                # Check if the item exists in the dictionary
                p_positive_multiplier_array.append(p_quotient(positive_dict[i], len(positive_tokens)))
                existence = True
                break
        # If after iterating through the entire dictionary there is no word for it, add one artificially
        if not existence:
            p_positive_multiplier_array.append(p_quotient(0.9, len(positive_tokens)))

    # Negative Case
    for token in phrase:
        existence = False # Does it already exist in the data set?
        for i in negative_dict:
            if token == i:
                p_negative_multiplier_array.append(p_quotient(negative_dict[i], len(negative_tokens)))
                print(i, " appeared ", negative_dict[i], " times.")
                existence = True
                break
        # If after iterating through the entire dictionary there is no word for it, add one artificially
        if not existence:
            p_negative_multiplier_array.append(p_quotient(1, len(negative_tokens))) # Artificially adding an instance, "additive smoothing"

    # print(p_positive_multiplier_array)
    # print(p_negative_multiplier_array)

    final_positive_p = p_quotient(len(positive_tokens), total_words) # Probability that it's positive
    final_negative_p = p_quotient(len(negative_tokens), total_words) # Probability that it's negative positive

    print("Probability positive: ", final_positive_p)
    print("Probability negative: ",final_negative_p)

    print("Multiplier Array Positive", p_positive_multiplier_array)
    print("Multiplier Array Negative", p_negative_multiplier_array)


    for i in p_positive_multiplier_array:
        print("Final positive multiplier: ", final_positive_p, " times ", i)
        final_positive_p = final_positive_p*i
    for j in p_negative_multiplier_array:
        print("Final negative multiplier: ", final_negative_p, " times ", j)
        final_negative_p = final_negative_p*j

    print(final_positive_p)
    print(final_negative_p)
    print("Result")
    positive_p_normalized = final_positive_p/(final_negative_p + final_positive_p)
    negative_p_normalized = final_negative_p/(final_negative_p + final_positive_p)

    print("Positive: ", positive_p_normalized)
    print("Negative: ", negative_p_normalized)

    if positive_p_normalized > negative_p_normalized:
        print("Message was positive.")
        if input("Accurate? ").lower() == "n":
            with open("negative_reviews.txt", 'a') as file:
                file.write("\n" + og_phrase)
                print(og_phrase, "written to negative reviews.")

    else:
        print("Message was negative.")
        if input("Accurate? ").lower() == "n":
            with open("positive_reviews.txt", 'a') as file:
                file.write("\n" + og_phrase)
            print(og_phrase, "written to positive reviews.")

