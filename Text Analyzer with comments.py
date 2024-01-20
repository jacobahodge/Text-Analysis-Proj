"""
Step-1 Define a string.
String = "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."
"""

text = ("Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.")

"""
# Step-2 Define the class and its attributes:
# 2.a) Create a class named TextAnalyzer.
# 2.b) Define the constructor __init__ method that takes a text argument.
"""

class TextAnalyzer:
    def __init__(self, text): # The __init__ method initializes the class with a 'text' parameter.

"""
Step-3 Implement a code to Format the text in Lowercase:
Inside the constructor, we will convert the text argument to lowercase using the lower() method.
Then, will Remove punctuation marks (periods, exclamation marks, commas, and question marks) from the text using the replace() method.
At last, we will Assign the formatted text to a new attribute called fmtText.
"""
class TextAnalyzer:
    def __init__(self, text):
        formatted_text = text.replace(',', '').replace('.','').replace('?','').replace('!','') # removing punctuation
        formatted_text = formatted_text.lower()  # making the text lowercase
        self.fmtText = formatted_text

"""
Step-4 Implement a code to count the Frequency of all unique words:
In this step, we will Implement the freqAll() method with the below parameters:
1.) Split the fmtText attribute into individual words using the split() method.
2.) Create an empty dictionary to store the word frequency.
3.) Iterate over the list of words and update the frequency dictionary accordingly.
4.) Use count method for counting the occurence
5.) Return the frequency dictionary.
"""
class TextAnalyzer:
    def __init__(self, text):
        formatted_text = text.replace(',', '').replace('.','').replace('?','').replace('!','') # removing punctuation
        formatted_text = formatted_text.lower()  # making the text lowercase
        self.fmtText = formatted_text  # fmtText is an instance of the class.
      
    def word_count(self):                # new method to create a dict with key of each unique word and the value as the count of the word in the provided text.
        word_list = self.fmtText.split(' ')   # Splitting the formatted text into individual words. 
        word_dict = {}                   # Creating a dictionary to store the words.
        for word in set(word_list):      # For loop to count the individual words in our formatted text. "word" is just a variable and essentially an index. We use a set to remove duplicates. 
            word_dict[word] = word_list.count(word)   # Here we are seting 'word' to be the value in our dictionary "word_dict" and the value for the key is the count of each unique word.
        
        return word_dict
"""
Here ^, wordList is a list of words obtained by splitting the formatted text (self.fmtText). 
Before calculating the frequency, the set(wordList) is used to create a set of unique words. 
This is done because a set only contains unique elements, so any duplicate words in wordList will be removed.
The loop iterates over this set of unique words, and for each word, it counts its occurrences in the original wordList using wordList.count(word). 
The result is then stored in the freqMap dictionary with the word as the key and its frequency as the value.
"""      
"""
Step-5 Implement a code to count the Frequency of a specific word:
In step-5, we have to Implement the freqOf(word) method that takes a word argument:
1.) Create method and pass the word that need to be found
2.) Get the freqAll method for look for count and check if that word is in the list.
3.) Return the count. If the word is not found, the count returned is 0.
"""
    def freqOf(self, word):     # new method to produce the count of a a unique word from thwe given text. Since we are going to provide a word in the function we need to add it as an argument.
        freqDict = self.word_count()    # freqDict calls out previous method word_count and implements an If, Else conditional statement. 
        if word in freqDict:        # if the given word is in the word_count dictionay...
            return freqDict[word]   # then return the value aka the count of that word in the text. 
        else:
            return 0                # Otherwise return 0.

# Consolidated code with no comments. 
text = ("Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.")

class TextAnalyzer:
    def __init__(self, text):
        formatted_text = text.replace(',', '').replace('.','').replace('?','').replace('!','')
        formatted_text = formatted_text.lower()
        self.fmtText = formatted_text
      
    def word_count(self):
        word_list = self.fmtText.split(' ') 
        word_dict = {}
        for word in set(word_list):
            word_dict[word] = word_list.count(word)
        
        return word_dict

    def freqOf(self, word):
        freqDict = self.word_count()
        if word in freqDict:
            return freqDict[word]
        else:
            return 0 

"""
Interacting with our class and methods
"""
# 1.) Create an instance of TextAnalyzer Class
analyzed = TextAnalyzer(some_text) # remember that "text" is a required argument for the TextAnalyzer class so in this case "some_text" is an example of likely a long text string we want to analyze.

# 2.) Convert the text to lower case and remove the punctuation.
print("Formatted text:", analyzed.fmtText)  

# 3.) Call the function that counts the frequency of all unique words from the data.
words_by_count = analyzed.word_count()  # Naming our variable. Using the "word_count" method in our instance "analyzed".
print("Unique words from text by count:")
print(words_by_count)

# 4.) Call the function that counts the frequency of specific word.
print("Frequency of the word, 'lorem' in the provided text:", analyzed.freqOf("lorem"))
  
      
