def count_words(sentence):
    word_counts = {}

    # Split(розділити) the sentence into words
    words = sentence.split()

    # Iterate through the words
    for word in words:
        # Remove punctuation
        word = word.strip("+-.,!?")

        # Check if the word is already in the dictionary
        if word in word_counts:
            # If it's in the dictionary, increment the count
            word_counts[word] += 1
        else:
            # If it's not in the dictionary, add it with a count of 1
            word_counts[word] = 1

    return word_counts


random_sentence = input("enter a random sentence: ")

result = count_words(random_sentence)
print(result)
