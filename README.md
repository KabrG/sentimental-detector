## sentimental-detector
I created a program that utilizes a machine learning algorithm to detect whether a given phrase has a negative or positive connotation. It uses the formula for conditional probability, which states P(A and B) = P(A)P(B|A). I've included two .txt files of phrases that have been verified as negative/positive (training set). The program first tokenizes the phrases to keep only the essential words with meaning. For example, "the", "a", "might", "would" bring little information about a sentences connotation but "hate", "love", "awful, "delicious" give information. 

# Limitations 
Too large of a .txt file will add to program run time.
