letter_score = {'a' : 1, 'e' : 1, 'o' : 1,
                'i' : 1, 'n' : 1, 'r' : 1,
                'l' : 1, 't' : 1, 'l' : 1,
                's' : 1, 'n' : 1, 'd' : 2,
                'u' : 2, 'g' : 2, 'b' : 3,
                'c' : 3, 'm' : 3, 'p' : 3,
                'f' : 4, 'h' : 4, 'v' : 4,
                'w' : 4, 'y' : 4, 'k' : 5,
                'j' : 8, 'x' : 8, 'q' : 10,
                'z' : 10
}


max_word, max_score = '', 0
with open('dictionary.txt') as file:
    for line in file:
        words = line.split()
        for word in words:
            word_value = 0
            if word.isalpha():
                for letter in word:
                    word_value += letter_score[letter]

                if word_value > max_score:
                    max_word = word
                    max_score = word_value

    print("The word from dictionary with the best score is:")
    print(max_score)
    print(max_word)



# returns the scrabble score for a given word
def scrabble_score(word):

    word = input("Please, write the word to see the score: ")
    points = 0
    for letter in word.lower():
        points += letter_score[letter]
    return points
print (scrabble_score("word"))








