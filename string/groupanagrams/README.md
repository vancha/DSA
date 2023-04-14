#49. Group Anagrams

## Given an array of strings strs, group the anagrams together. You can return the answer in any order. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Solution:
We can check if one word is an anagram of another word, by treating a string as an iterable. Turning a string in to a sorted version of itself makes it easy to compare one word to another, if they're anagrams, they're the same sorted string.
Using this sorted string as a key to a dictionary makes it easy for us to keep track of which words have the same "sorted" representation, see below for a better explanation of the code.

First, create the dictionary that will hold the sorted strings:
`word_list = {}`

then, loop over every word in the input:
`for word in strs:`

for every word, turn them in to their sorted representation like so:
  `srted = "".join(sorted(word))`

check if this sorted representation has already been added to the dictionary once:
   `if srted in word_list:` 

if so, add this word under there as well (the actual word, not the sorted representation):
    `word_list[srted].append(word)`

if not, add this word under a new key, the new key being the sorted representation of this word:
    `else:
        word_list[srted] = [word]`

finally, create a list, and within that list, have a list for each word under the keys in our previously created dictionary:
` return [word_list[key] for key in word_list]`
 
