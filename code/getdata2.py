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
        #print(line)
        line = line.strip()
        line = line.split()
        for word in line:
            #print(word)
            word = cleanstring(word)
            if word != "":
                if word in W:
                    W[word] += 1
                else:
                    W[word] = 1
    return (W)
def findcommon(fName, fname2):
    F = open(fName, "r")
    F2 = open(fname2, "r")
    auc = set()
    
    ftwo = set()
    for line in F2:
        print(line)
        line = line.strip()
        line = line.split()
        for word in line:
            word = cleanstring(word)
            ftwo.add(word)
    for line in F:
        line = line.strip()
        line = line.split()
        for word in line:
            #print(word)
            word = cleanstring(word)
            ftwo.add(word)
    return ftwo

def dofreq(auc, W, W2, fName, fname2):
    F = open(fName, "r")
    F2 = open(fname2, "r")
    RW = {}
    RW2 = {}
    fc=0
    f2c=0
    finlist = [fName]
    small = []
    
    com = set();
    art =set()
    for line in F2:
        #print(line)
        line = line.strip()
        line = line.split()
        for word in line:
            f2c+=1
            word = cleanstring(word)
            com.add(word)
    for line in F:
        line = line.strip()
        line = line.split()
        for word in line:
            fc+=1
            print(fc)
            word = cleanstring(word)
            art.add(word)
            
 
    for word in art:
        for cword in com:
            small.append(word)
            small.append(cword)
            x = W[word]
            y = W2[cword]
            x = x/fc
            y = y/f2c
            z=x/y
            small.append(z)
            print(small)
            finlist.append(small)
                
            
   
    return(finlist)


def main():
 #   fName = input("What file? ")
#    fname2 = input("and the comments are?")
    fName="article"
    fname2="comments"
    ## W is a dictionary with the words as keys and the number of times they are in
    ## the file as a value
    W = makedic(fName)
    W2 = makedic(fname2)
    #now we find common set
    auc = findcommon(fName, fname2)
    #now we want to find the frequency for each word
    done = dofreq(auc, W, W2, fName, fname2)
    #W and W2 are dictionaries for the frequency of the words that the article and comments have in common,
    #now we need to divide these numbers by the universal library and compare
    print(done)
    print("done")
    return

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

