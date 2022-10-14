#Парсер HTML социальной сети + интерфейс к нему
---
##Технологии
- BeautifulSoup4
- Selenium
- eeL
---

##Установка технологий
BeautifulSoup4

```bash
pip install beautifulsoup4
```
Selenium
```bash
pip install selenium
```
eeL
```bash
pip install eel
```
Также необходимо установить на компьютер браузер Google Chrome и скачать драйвер для работы с Selenium. Драйвер можно скачать по ссылке https://chromedriver.storage.googleapis.com/index.html
После в самом коде необходимо будет указать полный путь до драйвера.

Пример для ОС Windows
```bash
driver = webdriver.Chrome(
        executable_path="C:\\Users\\fakc6\OneDrive\\Рабочий стол\\parser_itog_2\\chromedriver\\chromedriver.exe",
        options = options
    )
```
---
##После установки
После установки и запуска необходимо ввести логин и пароль от вашего аккаунта в нужные поля. Затем вставить ссылку на нужную страницу профиля Вконтакте.  
####Примечание
У вашего аккаунта не должна быть влючена двухфакторная аутификация аутентификации
