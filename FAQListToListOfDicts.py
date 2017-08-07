"""
Convert a text file input as a list (1 txt line per entry)
into a list of dictionaries with each dictionary representing a single
question/answer.
"""
class FAQListToListOfDicts:

    def __init__(self,faq):
        self.outListOfDicts = self.convert(faq)

    def getListOfDicts(self):
        return self.outListOfDicts

    def convert(self,faq):
        outList = []
        questionIndexes = [i for i in range(len(faq)) if faq[i].find('?')>0]
        for i in range(1,len(questionIndexes)):
            question = faq[questionIndexes[i-1]].rstrip()
            response = ""
            for line in range(questionIndexes[i-1]+1,questionIndexes[i]):
                response += faq[line].replace('\n',' ')
            outDict = {'question':question, 'response':response}
            outList.append(outDict)
        return outList


