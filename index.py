from selenium import webdriver

browser = webdriver.Chrome(executable_path="./chromedriver.exe")
index = 1

url = 'http://zhipin.com'
browser.get(url)
html = browser.page_source
# while index < 5:
#     browser.get(url+str(index))
#     html = browser.page_source
#     # print(html)
#     index += 1
#     print(index)

