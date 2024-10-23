from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
import csv

# Налаштування драйвера
chrome_options = Options()
chrome_options.add_argument('--headless')  # Запуск в headless режимі
chrome_options.add_argument('--ignore-certificate-errors')  # Ігнорування помилок SSL
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36')

service = Service(r"C:\Users\user\Desktop\chromedriver.exe")  # Вкажіть шлях до chromedriver

# Запуск драйвера
driver = webdriver.Chrome(service=service, options=chrome_options)

# Відкриття CSV файлу для запису
csv_file = 'phones_data.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Записуємо заголовки
    writer.writerow(['Link', 'Title', 'Image', 'Price', 'Rating', 'Wish_count'])

    # Цикл для перебору сторінок каталогу
    for page in range(1, 68): 
        url = f"https://rozetka.com.ua/ua/mobile-phones/c80003/page={page}/"
        driver.get(url)

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'stars__rating'))
            )
            
            # Отримуємо HTML-код після завантаження
            html = driver.page_source
            soup = BeautifulSoup(html, 'lxml')

            phones = soup.findAll("div", class_="goods-tile")

            data = []  # Очищуємо дані перед обробкою нової сторінки
            for phone in phones:
                # Отримуємо посилання та іншу інформацію про телефон
                link = phone.find("a", class_="product-link goods-tile__picture").get('href')
                title = phone.find('img').get('alt')
                img = phone.find('img').get('src')

                price_tag = phone.find("span", class_="goods-tile__price-value")
                price_numeric = re.sub(r'\D', '', price_tag.get_text()) if price_tag else "N/A"

                rating_div = phone.find('div', class_='stars__rating')
                if rating_div:
                    style = rating_div['style']
                    percent_value = float(style.split('(')[1].split('%')[0])
                    rating = round((percent_value / 100) * 5, 2)
                else:
                    rating = "N/A"
                
                # Переходимо на сторінку товару для збору кількості бажань
                driver.get(link)
                try:
                    wishlist_count_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'wishlist-count-text'))
                    )
                    wishlist_count = wishlist_count_element.text
                except Exception as e:
                    wishlist_count = "N/A"

                # Додаємо зібрані дані до списку
                data.append([link, title, img, price_numeric, rating, wishlist_count])

                # Повертаємося на сторінку каталогу
                driver.back()

            # Записуємо дані для поточної сторінки в CSV файл
            writer.writerows(data)
            print(f"Дані з сторінки {page} успішно збережено.")

        except Exception as e:
            print(f'Сталася помилка на сторінці {page}: {e}')

# Закриваємо драйвер
driver.quit()
print(f"Дані успішно збережені у {csv_file}")
