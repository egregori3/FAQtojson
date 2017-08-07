"""
FAQ to Json converter - by Eric Gregori.

Usage: FAQtoJ.py -h | --help
       FAQtoJ.py -v | --version
       FAQtoJ.py -i FAQfile
       FAQtoJ.py -i FAQfile -o JSONfile


Options:
  -h,--help             : This help text
  -v,--version          : Version
  -i <FAQfile>          : input FAQ file as text
  -o <JSONfile>         : output JSON file
"""
import sys
import os
import json
from docopt import docopt
import FAQListToListOfDicts

def main(arguments):
    print __doc__.split('.')[0]
#   print arguments
    try:
        inputFilename = arguments['-i']
        outputFilename = arguments['-o']
    except KeyError:
        print "Could not find argument."
        print >> sys.stderr, "Could not find argument."
        return 1

    file_open_error = getattr(__builtins__,'FileNotFoundError', IOError)
#   Open input file
    try:
        faq = open(inputFilename,"r")
    except file_open_error:
        print "Error opening input file"+inputFilename
        print >> sys.stderr, "Error opening file"+inputFilename
        return 1

#   Open output file
#   If no output filename specified, use input filename
    if outputFilename == None:
        outputFilename = inputFilename.rsplit('.', 1)[0]+'.json'
    try:
        JsonOut = open(outputFilename,"w")
    except file_open_error:
        print "Error opening output file"+outputFilename
        print >> sys.stderr, "Error opening file"+outputFilename
        return 1

#   Read file into list
    with faq:
        faqList = faq.readlines()

#   Instantiate converter
    print "Converting: "+inputFilename
    converter = FAQListToListOfDicts.FAQListToListOfDicts(faqList)

#   Write ListOfDicts out as Json
    print "Writing Json: "+outputFilename
    json.dump(converter.getListOfDicts(),JsonOut,ensure_ascii=False,indent=4)

#   cleanup
    faq.close()
    JsonOut.close()
    print "Done"

# NOTE: main() will not be called if doctype catches -v or -h
if __name__ == '__main__':
    sys.exit(main(docopt(__doc__, version='08062017')))