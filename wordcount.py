import plotgraph
wordCounts={}
#This Function takes in a line, and clean it to words with spaces.
#For example some line may be in this format: Hello.dear! Not here?
#Function returns cleaned line.
def CleanLine(line):
    from string import punctuation
    import re
    r= re.compile(r'[{}]'.format(punctuation))
    new_strs=r.sub(' ', line) 
    #This method of printing below can sometime split on unicode or special charaters
    #not very effective for language that use special characters.
    #print("The splitted words using split regex are:", re.split(r'[^0-9A-Za-z]+',line))
    return new_strs

#Return list of words
def SplitLine(line):
    return line.split()

#Promt user for a yes or no; this verifies users input
def YesOrNo(user_input): 
        
    if user_input  == '1':
        print("You choose to overwrite the file...Overwriting started")
        return True
    else:
        print("You Do no want to overwrite the existing file...Appending started")
        return False 
            
#Prints Result to filename
def PrintResultToFile(dictResult, filename):
    import os.path
    if os.path.isfile(filename):
        user_input = input("File Exists, do you want to overwrite it? Press 1 to overwrite and anyother number to append: ")
        print("You typed", user_input)
        if YesOrNo(user_input):
            saveFile = open(filename, 'w')
            for word in dictResult:
                #print("The word " + word + " | Its numbers of occurences: " + str(wordCounts[word]))
                print(word + " : " + str(dictResult[word]))
                saveFile = open(filename, 'a')
                saveFile.write(word + " : " + str(dictResult[word])+"\n")
            print("Overwriting Finished")
        #if VerifyInput(confirmRewrite):
        #    pass #TODO: if users entered yes rewrite file. by first opening file and as w
        else:
            for word in dictResult:
                #print("The word " + word + " | Its numbers of occurences: " + str(wordCounts[word]))
                print(word + " : " + str(dictResult[word]))
                saveFile = open(filename, 'a')
                saveFile.write(word + " : " + str(dictResult[word])+"\n")
    saveFile.close


#This function opens a file and read through the lines.
def CalculateWordFrequencies(filePath):
    counter=0
    file = open(filePath, 'r')
    for line in file:
        counter+=1
        cleanedLine = CleanLine(line)
        words = SplitLine(cleanedLine)
        for word in words:
            if word in wordCounts:
                wordCounts[word]+=1
            else:
                wordCounts[word]=1
        print("\n",line, "\n", "--" * 8) #Print each line.
    print("The Dictionary with Word Counts:",wordCounts)
    PrintResultToFile(wordCounts, "resultTest.txt")
    print("Number of lines found:", counter)
    plotgraph.PlotGraph(wordCounts)

#Verifies if this module is not called from another.
if __name__ == "__main__":
    CalculateWordFrequencies("text.txt")
    print("-"*8)
    print("Done, Now calling the function to list the dictionary values and numbers")
    print("-"*8)
