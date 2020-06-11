import os
import sys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


# driver.implicitly_wait(timeout)
new_repo = input("Enter the directory name: ")
username = "nasr-edine"

driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
driver.get("https://github.com/new")

timeout = 30
WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="login_field"]'))).send_keys('')

WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys('')


WebDriverWait(driver, timeout).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/main/div/form/div[4]/input[9]'))).click()
driver.implicitly_wait(timeout)


WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="repository_name"]'))).send_keys(new_repo)

WebDriverWait(driver, timeout).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/main/div/form/div[3]/button'))).click()
driver.implicitly_wait(timeout)
driver.close()

path = os.path.expanduser("~/github/" + new_repo)
os.system("mkdir " + path)
os.chdir(path)
os.system("git init")
os.system("touch README.md")
os.system("touch .gitignore")
os.system("touch Makefile")
os.system("touch auteur")
os.system("touch main.c")

f = open("auteur", "a")
f.write("ndrai")
f.close()

f = open("main.c", "a")
f.write(
    """#include <stdio.h>\n\nint main(int argc, char const *argv[])\n{\n\tprintf("str: %s\\n", "Hello World");\n\treturn 0;\n}""")
f.close()

os.system("git add *")
os.system("git add .gitignore")
os.system('git commit -m "initial commit"')
os.system("ls -a")


os.system("code .")
print(f"git remote add origin https://github.com/{username}/{new_repo}.git")
# os.system(f"git remote add origin git@github.com:{username}/{new_repo}")
os.system(
    f"git remote add origin https://github.com/{username}/{new_repo}.git")

os.system("git push -u origin master")


# os.system("rm -r " + path)
