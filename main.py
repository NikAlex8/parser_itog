from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import eel


eel.init("web")
@eel.expose
def get_id(login,password,user_link):
    options = webdriver.ChromeOptions()
    options.add_argument("user-agint=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36")
    #options.add_argument('headless')

    url = "https://vk.com/login"

    driver = webdriver.Chrome(
        executable_path="C:\\Users\\fakc6\OneDrive\\Рабочий стол\\parser_itog_2\\chromedriver\\chromedriver.exe",
        options = options
    )


    def scroll_down(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.5)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height



    def friends_info(friends_d, friend_id, driver):
        friends_set = set()
        dict = {}
        driver.get(f"https://vk.com/id{friend_id}")
        time.sleep(1)    
        soup1 = BeautifulSoup(driver.page_source, 'html.parser')
        user_name = soup1.find('div', class_="ProfileInfo").find('h2').text
        driver.get(f"https://vk.com/friends?id={friend_id}&section=all")
        time.sleep(5) 
        scroll_down(driver)
        soup2 = BeautifulSoup(driver.page_source, 'lxml')
        time.sleep(0.5) 
        friends_s = soup2.findAll('div', class_= "friends_user_row--fullRow")
        time.sleep(0.5)  
        for fs in friends_s:
                friends_set.add(fs["id"][16:])
        dict[friend_id] = {
            'user_name' : user_name,
            'friends_ids': list(friends_set)     
        }        
        friends_d.append(dict)
        


    try:
        driver.get(url = url)
        time.sleep(1)

        email_input = driver.find_element(By.ID, "index_email") 
        email_input.clear()
        email_input.send_keys(login)
        time.sleep(2)

        button1 = driver.find_element(By.CLASS_NAME, "FlatButton__in")
        button1.click()
        time.sleep(2)

        password_input = driver.find_element(By.NAME, "password") 
        password_input.clear()
        password_input.send_keys(password)
        time.sleep(2)

        button2 = driver.find_element(By.CLASS_NAME, "vkuiButton__in")
        button2.click()
        time.sleep(2)
    
        driver.get(user_link)
        time.sleep(1)

        body = driver.page_source
        body = body.split('<a href="/albums')[2]
        id = body[0:body.index('"')]

        driver.get(f"https://vk.com/friends?id={id}&section=all")

        time.sleep(2)
        scroll_down(driver)

        soup = BeautifulSoup(driver.page_source, 'lxml')
        time.sleep(2)
        all_friends_id1 = soup.findAll('div', class_= "friends_user_row--fullRow")
        time.sleep(2)
        friend_data = []
        for friend_ids in all_friends_id1:
            friends_id = friend_ids.get('id').split('friends_user_row')
            id_f = friends_id[1]
            friend_data.append(id_f)

        f_d = []
        for friend in friend_data:
            friends_info(f_d, friend, driver)
            with open('friends_info.txt', 'w', encoding="utf-8") as f:
                f.write(f_d.__str__())

        time.sleep(5)
        print('Работа выполнена!')

    
    except Exception as ex:
        print(ex)
    finally:
        driver.close()    
        driver.quit()


eel.start("index.html", size=(500, 600))