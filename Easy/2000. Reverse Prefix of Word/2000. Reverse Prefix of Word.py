#141223 Submission
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        # Approach
        # 1) Initialize output to store answer
        # 2) Initialize temporary string to store prefix
        # 3) if ch in word, loop through word. Initialize a counter to prevent reversing the string with duplicates of ch. if iteration == ch, output += iteration and reverse output. else, output += iteration. return word
        # 4) if ch not in word, return word

        output: str = ""
        temp_string: str = ""

        if ch in word:
            counter: int = 0
            for i in word:
                if i == ch and counter == 0:
                    output += i
                    output = output [::-1]
                    counter += 1
                else:
                    output += i
            return output
        else:
            return word

        # Test cases
        # 1) ch is not in prefix of wrod
        #    word = "abcd", ch = "z" -> Returns "abcd"
        # 2) ch is in prefix of word
        #    word = "abcdefd", ch = "d" -> Returns "dcbaefd"

        # Runtime = 40ms, beats 43% of users
        # Memory = 16.23MB, beats 56.84% of users
