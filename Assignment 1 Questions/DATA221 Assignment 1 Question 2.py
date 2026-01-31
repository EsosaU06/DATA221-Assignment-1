def NestedDictionaryFromStrings(listInput = None):
    if listInput is None or listInput.__class__ != list: # error catching
        return None
    
    wordDictionary = {}
    # creating the dictionary to keep the words the data
    # corresponding to them
    
    for word in listInput:
        # look through every word in the list that was given
        
        wordDictionary[word] = {"length": 0, "parity": "none"}
        # create a dictionary for the word itself
        
        wordDictionary[word]["length"] = len(word)
        # set the value for the "length" key to
        # the length of the word
        
        if len(word) % 2 == 0:
            # check if the word is even by
            # check if the remainder is zero
            wordDictionary[word]["parity"] = "even"
        else:
            wordDictionary[word]["parity"] = "odd"
            
    return wordDictionary

# example code:
# print(NestedDictionaryFromStrings([["This"], ["is"], ["a"], ["test!"]]))