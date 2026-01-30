def NestedDictionaryFromStrings(listInput = None):
    if listInput is None or listInput.__class__ != list: # error catching
        return None
    
    wordDictionary = {}
    # creating the dictionary to keep the words the data
    # corresponding to them
    
    for word in listInput:
        # look through every word in the list that was given
        
        wordDictionary[word] = {"length": 0, "parity": "none"}
        # creating a key-value pait for the word
        
        wordDictionary[word]["length"] = len(word)
        
        if len(word) % 2 == 0:
            # check if the word is even by
            # checking if the remainder is zero
            wordDictionary[word]["parity"] = "even"
        else:
            wordDictionary[word]["parity"] = "odd"
            
    return wordDictionary

# print(NestedDictionaryFromStrings(["This", "is", "a", "test!"]))