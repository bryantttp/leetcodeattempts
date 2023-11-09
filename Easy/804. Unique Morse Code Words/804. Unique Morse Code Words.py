class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        # Approach
        # 1) Create an dictionary to store the alphabet as keys and morse code as it value
        # 2) Loop through words and replace each alphabet with morse code -> O(n)
        # 3) For each item in words, change it to morse code and store it in dictionary and add 1 to value for each repetition -> O(n)
        # 4) Count and return no. of keys

        # morse_dict: dict[str,int] = {}
        # morse_code: dict[str,str] = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
        # for i in range(len(words)):
        #     words[i] = morse_code[words[i]]
        # for i in range(len(words)):
        #     if words[i] in morse_dict.keys():
        #         morse_dict[words[i]] += 1
        #     else:
        #         morse_dict[words[i]] = 1
        # return len(morse_dict.keys())

        # Test case:
        # 1) one element in words:
        #    words = ["a"] -> Error
        # 2) same element in words:
        #    words = ["aa","aa","aa"] -> Error

        # Improved Approach
        # 1) Create an dictionary to store the alphabet as keys and morse code as it value
        # 2) Loop through words, replace each alphabet with morse code and input into a new list -> O(n)
        # 3) For each item in new list, store it in dictionary -> O(n)
        # 4) Count and return no. of keys



        morse_dict: dict[str,int] = {}
        morse_code: dict[str,str] = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
        new_words: List[str] = []
        for i in range(len(words)):
            temp_string = ''
            for j in range(len(words[i])):
                temp_string += morse_code[words[i][j]]
            new_words.append(temp_string)
        for i in range(len(new_words)):
            if new_words[i] not in morse_dict.keys():
                morse_dict[new_words[i]] = 1
        return len(morse_dict.keys())
