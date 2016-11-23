# test.py

Class Syllable(object):
    def __init__(self, stress):
        self.stress = stress

W = "ˈ$($($)),$($)ˈ$"
temp = []
n = 0

def getWordStructure(W):
    temp = []
    n = 0
    while n < len(W):
        if W[n] == "(":
            n2 = W.find(")")
            
        if W[n] == "ˈ":
            if W[n+1] == "$":
                temp.append(Syllable("+stress"))
                n += 2
                continue
            else:
                raise Exception ("Malformed input string: stress can only precede syllable.")
        elif W[n] == "$":
            temp.append(Syllable("-stress"))
            n += 1
            continue
