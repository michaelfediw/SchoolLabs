def getText(sen):
    """ (str) -> list
    Input: This functions takes in a sentence with not punctuation as a string.
    Output: This function returns the sentence as a list of upper case characters.
    """
    
    sen = list(sen.upper())                 #The upper function capitalizes the entire string, list makes it a list
    return sen
    
        
def encryptString(Message, Key):
    """ (list, list) -> list
    Input:This function recieves a Message in upper case letters as a list and a Key as a list of all the the upper case letters and the space character.
    Output: This function returns the encrypted message based upon the key.
    """
    
    alphabet = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    e = []
   
   
    for i in Message:
        a = alphabet.index(i)
        b = Key[a]
        e.append(b)
   
    return e
    
    
        