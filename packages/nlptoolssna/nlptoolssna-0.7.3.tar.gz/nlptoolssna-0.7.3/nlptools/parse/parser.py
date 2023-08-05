import re 

def arStrip(input_str , diacs=True , smallDiacs=False , shaddah=False ,  digit=False, alif=False , specialChars=False ):
    
    """
    This function removes Arabic diacritics, Quranic annotation signs, shaddah, English and Arabic digits, unify alif with hamzah,
    some special characters, spaces, underscore and Arabic tatwelah from the input string.

    Args:
        - input_str (:obj:str): Arabic text to be processed.
        - diacs (:obj:bool): flag to remove Arabic diacretics [ ًٌٍَُِْ] (default is True).
        - smallDiacs (:obj:bool): flag to remove small Quranic annotation signs (default is False).
        - shaddah (:obj:bool): flag to remove shaddah (default is False).
        - digit (:obj:bool): flag to remove English and Arabic digits (default is False).
        - alif (:obj:bool): flag to unify alif with hamzah (default is False).
        - specialChars (:obj:bool): flag to remove some special characters (default is False).

    Returns:
        - :obj:str: processed string with removed diacritics, Quranic annotation signs, shaddah, digits, and special characters.

    Raises:
    None.
    """
    try:
        if input_str: # if the input string is not empty do the following
            #print("in if")
            if diacs == True :
                input_str = re.sub(r'[\u064B-\u0650]+', '',input_str) # Remove all Arabic diacretics [ ًٌٍَُِْ]
                input_str = re.sub(r'[\u0652]+', '',input_str) # Remove SUKUN
            if shaddah == True:
                input_str = re.sub(r'[\u0651]+', '',input_str) # Remove shddah
            if smallDiacs == True:
                input_str = re.sub(r'[\u06D6-\u06ED]+', '',input_str) # Remove all small Quranic annotation signs
            if digit == True:
                input_str = re.sub('[0-9]+', ' ',input_str) # Remove English digits
                input_str = re.sub('[٠-٩]+', ' ',input_str)# Remove Arabic digits
            
            if alif == True:                             # Unify alif with hamzah: 
                input_str = re.sub('ٱ', 'ا',input_str);
                input_str = re.sub('أ', 'ا',input_str);
                input_str = re.sub('إ', 'ا',input_str);
                input_str = re.sub('آ', 'ا',input_str);
            if specialChars == True:
                input_str = re.sub('[?؟!@#$%-]+' , '' , input_str) # Remove some of special chars 

            input_str = re.sub('[\\s]+'," ",input_str) # Remove all spaces
            input_str = input_str.replace("_" , '') #Remove underscore
            input_str = input_str.replace("ـ" , '') # Remove Arabic tatwelah
            input_str = input_str.strip() # Trim input string
    except:
        return input_str
    return input_str
    
def ArabicStrip(input_str, diacs=True, smallDiacs=False, shaddah=False, digit=False, alif=False, specialChars=False):
    """
    Removes diacritics, small Quranic annotation signs, shaddah, English and Arabic digits, alif, special characters, spaces,
    underscore, and Arabic tatwelah from the input string.

    :param input_str: A string to be processed.
    :param diacs: A Boolean value indicating whether to remove diacritics or not.
    :param smallDiacs: A Boolean value indicating whether to remove small Quranic annotation signs or not.
    :param shaddah: A Boolean value indicating whether to remove shaddah or not.
    :param digit: A Boolean value indicating whether to remove English and Arabic digits or not.
    :param alif: A Boolean value indicating whether to unify alif with hamzah or not.
    :param specialChars: A Boolean value indicating whether to remove some special characters or not.
    :return: A processed string without diacritics, small Quranic annotation signs, shaddah, English and Arabic digits,
             alif, special characters, spaces, underscore, and Arabic tatwelah.
    """

    if not input_str:  # if the input string is empty, return it as is
        return input_str

    # Remove diacritics
    if diacs:
        input_str = re.sub(r'[\u064B-\u0650]+', '', input_str)  # Remove all Arabic diacretics [ ًٌٍَُِْ]
        input_str = re.sub(r'[\u0652]+', '', input_str)  # Remove SUKUN

    # Remove shaddah
    if shaddah:
        input_str = re.sub(r'[\u0651]+', '', input_str)

    # Remove small Quranic annotation signs
    if smallDiacs:
        input_str = re.sub(r'[\u06D6-\u06ED]+', '', input_str)

    # Remove English and Arabic digits
    if digit:
        input_str = re.sub('[0-9٠-٩]+', ' ', input_str)

    # Unify alif with hamzah
    if alif:
        input_str = re.sub('[ٱأإآ]', 'ا', input_str)

    # Remove some of special chars
    if specialChars:
        input_str = re.sub('[?؟!@#$%-]+', '', input_str)

    # Remove all spaces, underscore, and Arabic tatwelah
    input_str = re.sub('[\\s_ـ]+', "", input_str)

    # Trim input string
    input_str = input_str.strip()

    return input_str
   
def removePunctuation( inputString ):
    """
    Removes punctuation marks from the input string.
    
    Args:
    inputString (str): The input string containing punctuation marks.
    
    Returns:
    str: The output string with all punctuation marks removed.
    
    Raises:
    None
    """
    outputString = inputString
    try:
        if inputString:
            # English Punctuation
            outputString = re.sub(r'[\u0021-\u002F]+', '',inputString) # ! " # $ % & ' ( ) * + ,  - . /
            outputString = re.sub(r'[U+060C]+', '',outputString) # ! " # $ % & ' ( ) * + ,  - . /
            outputString = re.sub(r'[\u003A-\u0040]+', '',outputString) # : ; < = > ? @ 
            outputString = re.sub(r'[\u005B-\u0060]+', '',outputString) # [ \ ] ^ _ `
            outputString = re.sub(r'[\u007B-\u007E]+', '',outputString) # { | } ~
            # Arabic Punctuation
            outputString = re.sub(r'[\u060C]+', '',outputString) # ،
            outputString = re.sub(r'[\u061B]+', '',outputString) # ؛
            outputString = re.sub(r'[\u061E]+', '',outputString) # ؞
            outputString = re.sub(r'[\u061F]+', '',outputString) # ؟
            outputString = re.sub(r'[\u0640]+', '',outputString) # ـ
            outputString = re.sub(r'[\u0653]+', '',outputString) # ٓ
            outputString = re.sub(r'[\u065C]+', '',outputString) #  ٬
            outputString = re.sub(r'[\u066C]+', '',outputString) #  ٜ 
            outputString = re.sub(r'[\u066A]+', '',outputString) # ٪
            outputString = re.sub(r'["}"]+', '',outputString) 
            outputString = re.sub(r'["{"]+', '',outputString) 
            # outputString = re.sub(r'[\u066B]+', '',outputString) # ٫ 
            # outputString = re.sub(r'[\u066D ]+','',outputString) # ٭
            # outputString = re.sub(r'[\u06D4 ]+','',outputString) # ۔
    except:
        return inputString
    # print(outputString)
    return outputString
def removePunctuation_Mod(inputString):
    """
    Removes punctuation marks from the input string.
    
    Args:
    inputString (str): The input string containing punctuation marks.
    
    Returns:
    str: The output string with all punctuation marks removed.
    
    Raises:
    None
    """
    try:
        if inputString:
            punctuation_marks = [r'[\u0021-\u002F]+', r'[U+060C]+', r'[\u003A-\u0040]+',
                                 r'[\u005B-\u0060]+', r'[\u007B-\u007E]+', r'[\u060C]+',
                                 r'[\u061B]+', r'[\u061E]+', r'[\u061F]+', r'[\u0640]+',
                                 r'[\u0653]+', r'[\u065C]+', r'[\u066C]+', r'[\u066A]+',
                                 r'["}"]+', r'["{"]+']
            outputString = inputString
            for p in punctuation_marks:
                outputString = re.sub(p, '', outputString)
    except:
        return inputString
    return outputString

def removeEnglish( inputString ):
    """
    Removes all English characters from the input string.

    Args:
    - inputString (str): The string to remove English characters from.

    Returns:
    - outputString (str): The input string with all English characters removed.
    If an error occurs during processing, the original input string is returned.
    """
    try:
        if inputString:
            inputString = re.sub('[a-zA-Z]+', ' ',inputString)
    except:
        return inputString
    return inputString

def remove_latin(input_string):
    """
    Removes all Latin characters from the input string.

    Args:
        input_string (str): The string to remove Latin characters from.

    Returns:
        str: The input string with all Latin characters removed.
        If an error occurs during processing, the original input string is returned.
    """
    try:
        if input_string:
            input_string = re.sub('[a-zA-Z]+', ' ', input_string)
    except:
        return input_string
    return input_string
# print(removeEnglish("miojkdujhvaj1546545spkdpoqfoiehwv nWEQFGWERHERTJETAWIKUYFC"))
# print(removePunctuation("te!@#،$%%؟st") )
# Example
# print(arStrip( " مَحًمٌٍُِ" ,True ,True ,True ,True ,False , True ))

