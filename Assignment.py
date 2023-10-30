from selenium import webdriver
from selenium.webdriver.common.by import By
import json

#creating the json file

mySample = [{"name" : "Bob", "age" : 20, "gender": "male"}, {"name": "George", "age" : 42, "gender": "male"}, {"name":
"Sara", "age" : 42, "gender": "female"}, {"name": "Conor", "age" : 40, "gender": "male"}, {"name":
"Jennifer", "age" : 42, "gender": "female"}]

json_object = json.dumps(mySample, indent=3)

with open("sample.json", "w") as outfile:
    outfile.write(json_object)                      
    

driver = webdriver.Chrome()

driver.get('https://testpages.herokuapp.com/styled/tag/dynamic-table.html')

#Finding the input area
tab_1 = driver.find_element(By.XPATH,'/html/body/div/div[3]/details').click() 

#input data from the json file
tab_2 = driver.find_element(By.XPATH,'//*[@id="jsondata"]')
with open('sample.json', 'w') as file:
    json.dump(tab_2.text, file)         


#clicking on the refresh to reflect the changes visibly
refresh_tab = driver.find_element(By.XPATH, '//*[@id="refreshtable"]').click()      


#adding assertion
names_1 = driver.find_elements(By.ID, "name")
assert(names_1).__contains__('Bob', 'George', 'sara', 'conor', 'Jennifer')

age_2 = driver. find_elements(By.ID, 'age')
assert(age_2).__contains__('20','42', '42', '40','42')

gender_3 = driver.find_elements(By.ID, "gender")
assert(gender_3).__contains__('male','male','female','male','female')

