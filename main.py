import prereq
import alg
from prereq.trav import traverse
from prereq.keygen import keygen
from prereq.shuffle import sequence
from alg.algo import algorithm

def user_input():
    print("NOTE: Your Master Password Must Be A Mix Of Atleast 8 characters In Length, Has Digits, Symbols, Uppercase and Lowercase For Better Security \n")
    
    string = input(">>> ~$ Input Master Password: ")

    print(f"!!! ~$ Please Remember The Master Password, If You Forget This, You Will Lose All your Passwords \n-> {string}")

    site = input("Enter The Site You're Logging In To -> EXAMPLE: youtube.com -> Then Enter 'youtube': ")

    return string,site

string,site = user_input()
strlist = traverse(string)
dummylist = [ ]
keylist = keygen(strlist,dummylist)
seqlist = sequence(keylist)
sitel = []
algorithm(seqlist,site,sitel)