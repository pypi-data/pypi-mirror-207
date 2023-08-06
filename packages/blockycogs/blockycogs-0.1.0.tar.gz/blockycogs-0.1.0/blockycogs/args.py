import sys
import string
import re

def parse(args):
    argstring = args.decode("utf-8")
    stringTokens = argstring.split(",")
    return stringTokens
