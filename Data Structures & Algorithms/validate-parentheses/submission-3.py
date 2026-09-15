class Solution:
    def isValid(self, s: str) -> bool:
        pilha = []
        for i in range(len(s)):
            if s[i] == "[" or s[i] == "(" or s[i] == "{":
                pilha.append(s[i])
                

            elif s[i] == "]" or s[i] == ")" or s[i] == "}":
                if not pilha:
                    return False
                if (s[i] == "]" and pilha[-1] == "[") or \
                (s[i] == ")" and pilha[-1]=="(") or \
                (s[i] == "}" and pilha[-1]=="{"):
                    pilha.pop()
                else:
                    return False
                    
        
        if not pilha:
            return True
        else:
            return False