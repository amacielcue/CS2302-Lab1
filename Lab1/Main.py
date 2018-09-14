#CS2302 Lab1-C
#By: Alejandra Maciel
#Last Modified: Sept-13-2018
#Instructor: Diego Aguirre
#TA: Manoj  Pravaka  Saha
#The purpose of this code was to create all the possible passwords of 3-7 digits with numbers fromn 0-9 and compare
# every combination hashed with the username's salt value in order to find the username's password.
import hashlib

def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig

def main(str):
    hex_dig = hash_with_sha256(str)
    print(hex_dig)

pswd= [[""],["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]]

#Method: Generates all the possible passwords within the stated number of digits.
def get_pswd(min, max) :
    #Pulls the outside variable pswd to reduce the unnecessary recursion
    global pswd
    if(min < max) :
        #if the minimum digits passwords is not on the list then try with 1 less digit.
        if len(pswd) <= min :
            return get_pswd(min-1, max)
        #else append the list of passwords with 1 more digit
        else :
            r_pass = []
            for i in range(len(pswd[min])) :
                for j in range(0,10) :
                    r_pass.append(pswd[min][i] + str(j))
            pswd.append(r_pass)
            return get_pswd(min+1, max)

#Method: Reads the company's information file and splits all the information into a lists. Also calls the password
# comparisoin method.
def read_file(file_name) :
    f = open(file_name, 'r')
    file = f.read().splitlines()
    for i in range(len(file)) :
        info = file[i].split(",")
        compare_pswd(info[0], info[1], info[2])

#Method: Compares the generated passwords hashed with the username's salt value against the username's stored hashed
#password in order to find their original password.
def compare_pswd(user, s_value, digits) :
    for i in range(len(pswd)) :
        for j in range(len(pswd[i])) :
            if hash_with_sha256(pswd[i][j] + s_value) == digits :
                print(user + "'S PASSWORD IS: " + pswd[i][j])

#Method calls
get_pswd(3,7)
read_file("password_file.txt")