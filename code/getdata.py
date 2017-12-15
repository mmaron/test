#matana, david article code
def cleanstring(s):
    s = s.strip(""".,"';:-!?(){}[]""")
    s = s.lower()
    return s


def CommonWords(L, n, commonList):
    for entry in L[:n]:
        commonList.append(entry[1])

def makedic(fName):
    W = {}
    F = open(fName, "r")
    for line in F:
        line = line.strip()
        line = line.split()
        for word in line:
            word = cleanstring(word)
            if word != "":
                if word in W:
                    W[word] += 1
                else:
                    W[word] = 1
    return (W, F)
def findcommon(F, F2):
    auc = set()
    ftwo = set()
    for line in F2:
        line = line.strip()
        line = line.split()
        for word in line:
            word = cleanstring(word)
            ftwo.append(word)
    for line in F:
        line = line.strip()
        line = line.split()
        for word in line:
            word = cleanstring(word)
            if word in ftwo:
                auc.append(word)
    return auc

def dofreq(auc, W, W2, F, F2):
    RW = {}
    RW2 = {}
    fc=0
    f2c=0
    for line in F:
        for word in line:
            fc+=1
    for line in F2:
        for word in line:
            f2c+=1
    for word in auc:
        x = W[word]
        y = W2[word]
        x = x/fc
        y = y/f2c
        RW[word]=x
        RW2[word]=y
    return(RW, RW2)


def main():
    fName = input("What file? ")
    fname2 = input("and the comments are?")

    ## W is a dictionary with the words as keys and the number of times they are in
    ## the file as a value
    W, F = makedic(fName)
    W2, F2 = makedic(fname2)
    #now we find common set
    auc = findcommon(F, F2)
    #now we want to find the frequency for each word
    W, W2 = dofreq(auc, W, W2, F, F2)
    #W and W2 are dictionaries for the frequency of the words that the article and comments have in common,
    #now we need to divide these numbers by the universal library and compare


    ## L is list of pairs of words and they number of times they appear
    """
    F = open(fName, "r")
    for line in F:
        wordCount = 0  ## This count is just to know to capitalize or not
        line = line.strip()
        line = line.split()
        for word in line:
            cleanWord = cleanstring(word)
            if cleanWord not in commonList:
                if wordCount == 0:
                    word = word.capitalize()
                print(word, end=" ")
                wordCount += 1
        print()
"""

main()

