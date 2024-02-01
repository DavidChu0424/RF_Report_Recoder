import os
from os import listdir
from os.path import isfile, isdir 
import sys
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import xml.etree.ElementTree as ET
import xml.sax


TestCase = []
allkwline = ""
kwline = ""
count = 0
f = open('output.xml', encoding="utf8")
for line in f.readlines():

    print(line)
    if ".robot" in line:
        count = 0
        if allkwline != "":
            temp.append(allkwline)
            TestCase.append(temp)
            allkwline = ""
        temp = []
        line = line.replace("<","")
        line = line.replace(">\n","")
        name = line.split("/")
        name = name[-1].replace('"',"")
        name = name.strip(".robot")
        print(name)
        temp.append(name)
    
    if "<kw" in line:
        count = count + 1
        print(line)
        allkwline = allkwline + kwline + "\n"
        kwline = line.strip('<kw name="')
        kwline = kwline.strip('\n"')
        kwline = kwline.replace('>', "")
        kwline = kwline.replace('"', "")
        kwline = kwline.replace('library=bmc_debug', "")
        kwline = kwline.replace('library=String', "")
        kwline = str(count) + ":" + kwline
        print(kwline)
    
    if "<arg>" in line:
        print(line)
        argline = line.strip("<arg>")
        argline = argline.strip("</arg>\n")
        kwline = kwline + " " + argline + " "
        print(kwline)
        
f.close


df_table = pd.DataFrame(TestCase)
df_table.columns = ['ID','Step']
df_table.set_index('ID',inplace = True)
print(df_table)
df_table.to_excel("record.xlsx")












# 從檔案載入並解析 XML 資料
# tree = ET.parse('output.xml')
# root = tree.getroot()
# print(root.tag)


# obj2 = root.findall('suite')
# for i in range(len(obj2)):
#     obj2 = obj2[i].findall('suite')
# # print(obj2.tag)
# for i in range(len(obj2)):
#     obj2 = obj2[i].find('suite')
# # print(obj2.tag)
# for i in range(len(obj2)):
#     obj2 = obj2[i].findall('test')
# ###########################
# obj = root.find('suite')
# print(obj.tag)
# obj = obj.find('suite')
# print(obj.tag)
# obj = obj.find('suite')
# print(obj.tag)
# obj = obj.find('suite')
# print(obj.tag)
# obj = obj.find('test')
# count = root.findall('test')
# print(count)
# testcase = []
# for c in range(len(count)):
#     total = ""
#     print(obj)
#     tag = obj.find('tag')
#     print(obj.tag)
#     obj = obj.findall('kw')
#     print(obj)
#     list = []
#     list.append(tag.text)
#     for i in range(len(obj)):
#         print(obj[i].attrib['name'])
#         obj = obj[i].findall('kw')
#         print(obj)
#         for j in range(len(obj)):
#             print(obj[j].attrib['name'])
#             s1 = (obj[j].attrib['name'])
#             obj2 = obj[j].findall('arg')
#             for k in range(len(obj2)):
#                 print(obj2[k].text)
#                 temp = obj2[k].text
#                 s1 = s1 + " " + temp + " "
#                 print(s1)
#             s1 = str(j+1) + " " + s1
#             total = total + s1 + "\n"
#     list.append(total)
#     # print(list)
# testcase.append(list)
# print(testcase)     




# df_table = pd.DataFrame(testcase)
# df_table.columns = ['ID','Step']
# df_table.set_index('ID',inplace = True)
# print(df_table)
# df_table.to_excel("record.xlsx")


# df_table_All.to_excel("Report_All.xlsx")
# print("Report Output Successfully !!") 

    
    
# print(obj.attrib['name'])


# print(obj)
# obj = obj.find('suite')
# print(obj)




# filepath = os.getcwd()
# # file_path = os.walk(filepath)
# def get_filelist(filepath):
#     Filelist = []
#     for home, dirs, files in os.walk(filepath):
#         for filename in files:
#             if "log.html" in filename:
#                 Filelist.append(os.path.join(home, filename))
#     return Filelist
# print(get_filelist(filepath))
# Filelist = get_filelist(filepath)
# df_table_All = pd.DataFrame()

# for file in range(len(Filelist)):
#     filepath = str(Filelist[file]).replace("\\","/")
#     project = filepath.split("/")
#     print(project[-3])
#     browser = webdriver.Chrome()
#     browser.get('file:///'+ filepath)
#     print(browser)

#     button  = browser.find_element(By.XPATH, '//*[@id="s1"]/div[1]/div[2]').click()
#     time.sleep(10)
#     button  = browser.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/a[1]').click()
#     # Total
#     Telement = browser.find_element_by_xpath('//*[@id="s1"]')
#     # Ttd_content = Telement.find_elements_by_class_name("parent-name")
#     Ttd_content = Telement.find_elements_by_xpath('//*[@id="s1-s1-s1-s1-t1-k1-k6"]/div[1]')
#     print(Ttd_content)
#     Tlst = [] 
#     for td in Ttd_content:
#         Tlst.append(td.text)
#     print(Tlst) 

#     col = len(Telement.find_elements_by_css_selector('tr:nth-child(1) td'))
#     Tlst = [Tlst[i:i + col] for i in range(0, len(Tlst), col)]


#     # Data //*[@id="tag-stats"]
#     element = browser.find_element_by_xpath('//*[@id="tag-stats"]')
#     td_content = element.find_elements_by_tag_name("td")
#     lst = [] 
#     for td in td_content:
#         lst.append(td.text)
#     print(lst) 

#     col = len(element.find_elements_by_css_selector('tr:nth-child(1) td'))
#     lst = [lst[i:i + col] for i in range(0, len(lst), col)]

#     Tlst.reverse()
#     for j in Tlst:
#         lst.insert(0, j)

#     df_table = pd.DataFrame(lst)
#     df_table.columns = ['Name','Total'+ str(file),'Pass'+ str(file), 'Fail'+ str(file), 'Skip'+ str(file), 'Times'+ str(file), str(project[-3])]
#     df_table.set_index('Name',inplace = True)
#     print(df_table)
#     df_table_All = df_table_All.join(df_table, how='outer')
#     print(df_table_All)
#     browser.close()

# df_table_All.to_excel("Report_All.xlsx")
# print("Report Output Successfully !!")