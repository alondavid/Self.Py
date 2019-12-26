def sort_anagrams(list_of_strings):
    '''
       Recieve a list of words. return list of lists of anagrams.
       Anagrams - Word with same letters, differrent positions.
       :param list_of_strings: List of words
       :param type: List
       :return: List of list of anagrams
       :rtype: List
       >>> list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated',
       'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled',
       'greatening', 'lasted', 'resmelts'] 
       >>> sort_anagrams(list_of_words) 
      [['deltas', 'desalt', 'slated', 'salted', 'staled', 'lasted'],
      ['retainers', 'ternaries'], ['pants'], ['generating', 'greatening'],
      ['smelters', 'termless', 'resmelts']]
    '''
    returned_list = []
    used = []
    for x in range(0, len(list_of_strings)):
        word = list_of_strings[x]
        if word in used:  #Jump over words we allready used
            continue
        list_of_words = [word]
        used.append(word)
        short_list = list_of_strings[ x + 1:]
        sorted1 = sorted(list(word))
        for word2 in short_list:
            if len(word) != len(word2): #if the word length is diff. we can skip
                continue
            sorted2 = sorted(list(word2))
            if sorted1 == sorted2:
                list_of_words.append(word2)
                used.append(word2)
        returned_list += [list_of_words]
    return returned_list
