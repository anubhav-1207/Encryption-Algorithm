import time
import prereq
import alg
import colorama
from colorama import Fore,init
from prereq.trav import traverse
from prereq.keygen import keygen
from prereq.shuffle import sequence,seqmix
from alg.prepalgo import diffusion
from alg import algorithm
from alg.algorithm import algorithm

init(autoreset=True)

def user_input():
    print(Fore.YELLOW+"\nNOTE: Your Master Password Must Be A Mix Of Atleast 8 characters In Length, Has Digits, Symbols, Uppercase and Lowercase For Better Security \n")

    time.sleep(0.5)
    
    string = input(Fore.WHITE+">>> ~$ Input Master Password: "+Fore.GREEN)


    print(Fore.RED+f"\n!!! ~$ Please Remember The Master Password, If You Forget This, You Will Lose All your Passwords \n-> {string}\n")

    time.sleep(0.5)

    site = input(Fore.YELLOW +"Enter The Site You're Logging In To ->"+Fore.BLUE+ " EXAMPLE: youtube.com ->" +Fore.YELLOW+" Then Enter"+Fore.BLUE+ " 'youtube': "+Fore.RESET)

    return string,site

string,site = user_input()
strlist = traverse(string)
dummylist = []
keylist = keygen(strlist,dummylist)
seqlist = sequence(keylist) #returns the list after apllying the weird array[i+1] += array[i] -> final var that stores the password
keylist = seqmix(keylist)
sitel = [] #stores chars of site
primechl = [] #sotres final ord of site in list
primechl = diffusion(seqlist,site,sitel,primechl) # encrypts the site ord
finalPassword = ""
algorithm(primechl,keylist,finalPassword)
