import numpy as np
import pandas as pd
# import nltk
import re
# from nltk.corpus import stopwords
# from nltk import PorterStemmer,word_tokenize

# stopwords = stopwords.words('english')
# stemmer = PorterStemmer()

# total_words = 0
# def ir_trim(messages):
#     for i in range(len(messages)):
#         text = messages[i]
#         tokens = word_tokenize(text)
#         tokens = [x for x in tokens if x not in stopwords and len(x)>2]
#         tokens = [stemmer.stem(x) for x in tokens]
#         tokens = ' '.join(tokens)
#         messages[i] = tokens

#     return messages

def normalise_data(text):

    for i in range(len(text)):
        message = text[i]
        message.lower()
        message = message.replace('&','and')
        message = message.replace('e - mail','email')
        message = message.replace('Subject','')
        message = re.sub('([(] )?\d{3}( [)])? (- )?\d{3} - \d{4}','phonenumber',message)
        message = re.sub('[a-zA-Z0-9._ ]+ @ \w+ \. [a-zA-z]+','emailaddr',message)
        message = re.sub('(https? : / / )?(www \. )[a-zA-Z0-9]+ \. ([a-zA-Z0-9]+ \. )?\w{2,3} (/ [a-zA-Z0-9]+ )*',' url ',message)
        message = re.sub(r'[^\w\s]',' ',message)
        message = re.sub(r'\_',' ',message)
        message = re.sub('[\[\]\(\)\{\}]',' ',message)
        message = message.replace('!','exclamation')
        message = re.sub('\d+','',message)
        message = re.sub(' \w ',' ',message)
        message = re.sub('  +',' ',message)
        
        text[i] = message

    return text

def get_normalisedData():
    dt = pd.read_csv(path)
    data = dt.to_dict()
    data['text'] = normalise_data(data['text'])

    data = pd.DataFrame(data)
    data = data[:2736]
    return data




    
