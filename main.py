# BY.xxx指定在某类型标签中寻找名为value的标签
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

# 输入账号密码
id_text = "202000460122"
password_text = "wzc87752190"

# 火狐不对外提供API，需要一个额外的exe
pathd = Service(r'./geckodriver.exe')
driver = webdriver.Firefox(service=pathd)

# 通过get请求打开网页
driver.get("https://www.bkjx.sdu.edu.cn/")

# 等待页面加载
time.sleep(1.5)

# 在页面中寻找带有链接的文本元素
Balance = driver.find_element(by=By.LINK_TEXT, value="智慧教学服务平台")
Balance.click()
print(driver.title)
time.sleep(10)

# 获取窗口的标签集和
allhands = driver.window_handles

# 不会自动切换网页，需要指定切换到新打开的网页
driver.switch_to.window(allhands[-1])

# 打印网页标题
print(driver.title)

# 找到对应输入id的框
login_name = driver.find_element(by=By.ID, value="un")

# 把id直接填到网页里
login_name.send_keys(id_text)

# 找到对应输入password的框
password = driver.find_element(by=By.ID, value="pd")

# 把密码直接填到网页里
password.send_keys(password_text)

# 找到登录按钮
button = driver.find_element(by=By.CLASS_NAME, value="landing_btn_bg")
button.click()
# 进入选课界面
time.sleep(10)
enter = driver.find_element(by=By.LINK_TEXT, value="进入选课")
enter.click()
time.sleep(1)
# 疯狂刷新选课轮次界面
while True:
    try:
        enter2 = driver.find_element(by=By.TAG_NAME, value="span")
        break
    except:
        time.sleep(0.5)
        driver.refresh()


enter2.click()
time.sleep(4)

# 整个框架里还有一个框架用来选课，叫做selectBottom
driver.switch_to.frame("selectBottom")
# 各种类型课的标签
title = driver.find_elements(by=By.TAG_NAME, value="li")
limit_select = title[2]
print(limit_select.text)
limit_select.click()
time.sleep(2)
driver.switch_to.frame("selectTable")
table = driver.find_element(by=By.CLASS_NAME, value="mainTable")
course_list = table.find_elements(by=By.TAG_NAME, value="tr")

# 寻找后量子密码学
for course in course_list:
    if ("后量子" in course[0]) or ("后量子" in course[1]) or ("后量子" in course[2]):
        target_course = course
        break

info_block = target_course.find_elements(by=By.TAG_NAME, value="td")
# 课余量
Balance = int(info_block[12].text)
print(Balance)
buts = info_block[14].find_elements(by=By.XPATH, value="/*")
for but in buts:
    try:
        but.click()
        break
    except:
        None

# while True:
#     driver.switch_to.parent_frame()
#     # 对应按钮
#     title = driver.find_elements(by=By.TAG_NAME, value="li")
#     limit_select = title[2]
#     print(limit_select.text)
#     # 切换到限选，同时刷新课容量
#     limit_select.click()
#     time.sleep(1)
#     driver.switch_to.frame("selectTable")
#     table = driver.find_element(by=By.CLASS_NAME, value="mainTable")
#     target_course = table.find_elements(by=By.TAG_NAME, value="tr")[2]
#     info_block = target_course.find_elements(by=By.TAG_NAME, value="td")
#     Balance = int(info_block[12].text)
#     print(Balance)
#     Takeit = info_block[14].find_element(by=By.ID, value="div_2022202311777")
#     if Balance != 0:
#         Takeit.click()
#         break
