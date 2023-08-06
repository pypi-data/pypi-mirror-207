"""This module "nester.py" contains one function "print_lol" which prints items in a list even if it contains list """
def print_lol(item_list,indent=False,level=0): 
    """This function takes one arguement "item_list", which is a list (simple or nested) 
        and prints items in a list even if it contains list. This is acheived using recursion. 
        A second argument "indent" is set to false by default, which when true takes another arguement
        "level" (default to 0) is used to indent by level amount of tabsupon encountering the nested list."""
    for item in item_list:
        if(isinstance(item,list)):
            print_lol(item,indent,level+1)
        else:
            if(indent):
                print("\t"*level, end='')
            print(item)
