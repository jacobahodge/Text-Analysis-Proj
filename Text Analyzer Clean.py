class TextAnalyzer:
    def __init__(self, text):
        formatted_text = formatted_text.lower()
        formatted_text = text.replace(',', '').replace('.','').replace('?','').replace('!','')
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
