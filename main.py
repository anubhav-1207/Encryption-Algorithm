import prereq
from prereq.trav import traverse
from prereq.keygen import keygen

def user_input():
    print("NOTE: Your Master Password Must Be A Mix Of Atleast 8 characters In Length, Has Digits, Symbols, Uppercase and Lowercase For Better Security \n")
    
    string = input(">>> ~$ Input Master Password: ")

    print(f"!!! ~$ Please Remember The Master Password, If You Forget This, You Will Lose All your Passwords \n-> {string}")
    return string

string = user_input()
strlist = traverse(string)
keygen(strlist)