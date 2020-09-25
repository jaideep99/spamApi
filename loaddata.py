import numpy as np
import pandas as pd
import re

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




    
