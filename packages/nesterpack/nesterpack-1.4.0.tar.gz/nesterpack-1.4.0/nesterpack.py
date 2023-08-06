"""This module "nester.py" contains one function "print_lol" which prints items in a list even if it contains list """
import sys

def print_lol(item_list,indent=False,level=0,fh=sys.stdout): 
    """This function takes one arguement "item_list", which is a list (simple or nested) 
        and prints items in a list even if it contains list. This is acheived using recursion. 
        A second argument "indent" is set to false by default, which when true takes another arguement
        "level" (default to 0) is used to indent by level amount of tabsupon encountering the nested list.
        Finally a fourth arguement is taken which describes the location the output in displayed (defaulted to screen)"""
    for item in item_list:
        if(isinstance(item,list)):
            print_lol(item,indent,level+1,fh)
        else:
            if(indent):
                print("\t"*level, end='',file=fh)
            print(item,file=fh)
