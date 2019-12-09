from selenium import webdriver
import datetime

# 网址
url = "https://cart.taobao.com/cart.htm"

# 加载谷歌浏览器驱动
browser = webdriver.Chrome(executable_path="d:/chromedriver.exe")# 浏览器驱动地址
browser.get(url)
start_time=0

# 扫码全选
while True:
    try:
        if browser.find_element_by_xpath('//*[@id="J_SelectAll1"]/div/label'):
            browser.find_element_by_xpath('//*[@id="J_SelectAll1"]/div/label').click()
            print("已经全选")
            break
    except:
        print("扫码等待ing...")
        continue


while True:
    time1 = datetime.datetime.now().strftime("%H:%M:%S.%f")
    # 判断时间
    if time1 >= '14:44:00':  # 开始时间
        # 点击结算
        browser.find_element_by_id('J_Go').click()
        while True:
            try:
                if  browser.find_element_by_class_name('go-btn'):
                    # 点击提交订单
                    browser.find_element_by_class_name('go-btn').click()
                    while True:
                        try:
                            # print(datetime.datetime.now().strftime("%H:%M:%S.%f"))
                            # break
                            if browser.find_element_by_xpath('// *[ @ id = "payPassword_container"] / div'):
                                # 输入支付 密码
                                browser.find_element_by_xpath('// *[ @ id = "payPassword_container"] / div').send_keys('990607') # 支付密码
                                # 点击支付
                                browser.find_element_by_xpath('//*[@id="J_authSubmit"]').click()
                                break
                        except:
                            continue
            except:
                continue
