import pickle
from nlptools.morphology import settings 
import re
from nlptools.morphology.tokenizers_words import simple_word_tokenize
from nlptools.utils.parser import arStrip
import os.path
from nlptools.DataDownload import downloader

def load_ALMA_dic():
   # Open the Pickle file in binary mode
    filename = 'ALMA27012000.pickle'
    path =downloader.get_appdatadir()
    file_path = os.path.join(path, filename)
    

    with open(file_path, 'rb') as f:
       #Load the serialized data from the file
       ALMA_dic = pickle.load(f)
       #print(ALMA_dic)
       return ALMA_dic

def tag(token, language, task):
    """
    Given a token, this method retrives the morphological solutions [token, lemma, pos, frequency, task and language] filterd by spesific language and task.
          
    Args:
        - token (:obj:`str`): The Arabic token to be morphologcaly tagged.
        - language (:obj:`str`): The language to filter the results by [MSA, Pal, Lebanese, Iraqi, Libyan, Syrian, Sudanese, Yemeni]. The defualt task if not specisifd is `MSA`.
        - task (:obj:`str`): The task to filter the results by [lemmatizer, pos, full]. The defualt task if not specisifd is `full`.

    Returns:
        list (:obj:`list`): A list of [token, lemma, pos_ar, lemma_freq, language, task], where:
            - token: the original input token
            - lemma: the lemma of the token
            - pos_ar: the part of speech of the token in Arabic
            - lemma_freq: the frequency of the lemma in the dictionary
            - language: the input language 
            - task: the input task 

            If no sloution is found for this token, an empty list is returned.
    """
    if token in settings.div_dic.keys():

        soluation =settings.div_dic[token][1]
        if task =='full' and soluation[-2] == language:
            return  [token, soluation[3], soluation[2],  soluation[-2], soluation[-1]]
        elif soluation[-2] == language and soluation[-1] ==task:
            return [token, soluation[3], soluation[2],  soluation[-2], soluation[-1]]
        return []
    else:
        return []

def analyze_morphology(text ,language, task):
   """
    This method takes a text as input and returns a morphological solution for each token in this text, Based on the input language and task, such that,
    if:
         - the task is lemmatizer, then the morphological soltuion is only the lemma.
         - the task is pos, then the morphological soltuion is only the pos.
         - the task is full, the the morphological soltuion is both the lemma and the pos.
     
    The language argument helps the morphological analysis to return more accurate solutions based on the specific variety of Arabic used in the input text, including MSA and various dialects such as Pal, Lebanese, Iraqi, Libyan, Syrian, Sudanese, and Yemeni. 

    Args:
         - text (:obj:`str`): The input text to be morphologicaly analyzed.
         - language (:obj:`str`): The language of the input text including MSA and various dialects such as Pal, Lebanese, Iraqi, Libyan, Syrian, Sudanese, and Yemeni.
         - task (:obj:`str`): The type of task being performed (e.g., `lemmatizer`, `pos`, or `full`).
         
    Returns:
          - output_list (:obj:`list`): A list of morphological solution for each token in the input text.
    """

   output_list = []
   # tokenize sentence into words
   tokens = simple_word_tokenize(text)

   # for each token 
   for token in tokens:
         result_token =[]
         # Trim spaces 
         token = token.strip()
         # Remove smallDiac
         token = arStrip(token , False , True , False , False , False , False) 
         # Unify ٱ 
         token = re.sub('[ٱ]','ﺍ',token)

         # Initialize solution [token, lemma, pos]
         solution =[token, token+"_0", 0,  "", ""]
         
         # if token is digit, update pos to be digit 
         if token.isdigit():
            solution[2] = "digit"

         # if token is english, update pos to be ENGLISH
         elif re.match("^[a-zA-Z]*$", token):
            solution[2] = "ENGLISH"

         else:
            # search for a token (as is) in the dictionary   
            result_token = tag(token,language, task)
            
            if len(re.sub(r'^[ﻝ]','',re.sub(r'^[ﺍ]','',token))) > 5 and result_token == []:
               # try with remove AL
               result_token = tag(re.sub(r'^[ﻝ]','',re.sub(r'^[ﺍ]','',token)), language, task)

            if result_token == []:
              # try with replace ﻩ with ﺓ
               result_token = tag(re.sub(r'[ﻩ]$','ﺓ',token), language, task)

            if result_token == []:
               # try with unify Alef
               word_with_unify_alef = arStrip(token , False , False , False , False , True , False) # Unify Alef
               result_token = tag(word_with_unify_alef, language, task)
            
            if result_token == []:
               # try with remove diac
               word_undiac = arStrip(token , True , False , True , True , False , False) # remove diacs, shaddah ,  digit
               result_token = tag(word_undiac, language, task)

            if result_token == []:
               # try with remove diac and unify alef
               word_undiac = arStrip(token , True , True , True , False, True , False) # diacs , smallDiacs , shaddah ,  alif
               result_token = tag(word_undiac, language, task)

         if result_token != []:
               output_list.append(result_token)
         else:
            # if no solution is found
            output_list.append(solution)

   return output_list               
        
def tagger(text: str, task = 'full', language = 'MSA'):

    """
    This method takes an Arabic text as input, tokenize it into tokens and calles the morphological tagger to return the morpological solution for each token in this text.
    There is no limit for the text size, but one should be resonable based on the available resources (computational power).
    
        Args:
            - text (:obj:`str`): The input Arabic text to be morphologically analyzed and tagged.
            - task (:obj:`str`): The type of morphological analysis and tagging to be performed (the default is `full`).
            - language (:obj:`str`): The language of the input text (the default is 'MSA' (Modern Standard Arabic)).
        
    Returns:
           - output_list list(:obj:`list`): A list of lists, where each sublist contains information about a token in the input text, including the original token, its lemma, its part of speech (POS) tag, its lemma frequency, the task and the language.

    **Example:**

    .. highlight:: python
    .. code-block:: python

         from nlptools.morph import morph_tagger
      
         # Return the morpological solution for each token in this text
         morph_tagger.tagger('ذهب الولد الى المدرسة')

         # the output
            [['ذهب', 349890, 'فعل', 'MSA'],
            ['الولد', 320244, 'اسم', 'MSA'],
            ['الى', 20215999, 'كلمة وظيفية', 'MSA'],
            ['المدرسة', 561184, 'اسم', 'MSA']]
    """
    
    # Check if the ALMA dictionary has been loaded
    if settings.flag == True:
        settings.flag = False
        settings.div_dic = load_ALMA_dic()
   
    
    # Perform morphological tagging for the input text
    output_list = analyze_morphology(text,language, task)
    
    # Return a list of morphological solution for each token in the input text
    return output_list

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    
    
    
    
    
