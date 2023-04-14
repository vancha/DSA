def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    word_list = {}
    for word in strs:
        srted = "".join(sorted(word)) 
        if srted in word_list:
            word_list[srted].append(word)
        else:
            word_list[srted] = [word]

    return [word_list[key] for key in word_list]
