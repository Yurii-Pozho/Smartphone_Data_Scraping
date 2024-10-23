import pandas as pd
import re

# Завантаження даних
main_df = pd.read_excel(r'phones.xlsx')
android_df = pd.read_csv(r'phones_title_android.csv')
ios_df = pd.read_csv(r"phones_title_os.csv")

# Очищуємо зайві пробіли в назвах

# Створюємо колонку з ОС
main_df['OS'] = 'Other'  # Спочатку ставимо значення 'Other' по замовчуванню

# Проставляємо Android та IOS де знайдено
main_df.loc[main_df['Title'].isin(android_df['Phones Title']), 'OS'] = 'Android'
main_df.loc[main_df['Title'].isin(ios_df['Phones Title']), 'OS'] = 'IOS'

# Конвертація Wish_count в Int64
main_df['Wish_count'] = main_df['Wish_count'].apply(lambda x: int(x) if pd.notna(x) else x).astype('Int64')

# Функція для вилучення категорії з заголовку
def exctract_category(title):
    match = re.search(r'\b([A-Za-z]+)', title)
    return match.group(0) if match else None

main_df['Category'] = main_df['Title'].apply(exctract_category)
main_df['Category'] = main_df['Category'].apply(lambda x: x.capitalize() if x else x)

# Видаляємо кирилицю і залишаємо лише латинські літери та цифри
def clean_title(title):
    return re.sub(r'[^A-Za-z0-9\s]', '', title)

main_df['Title'] = main_df['Title'].apply(clean_title)

android_df['Phones Title'] = android_df['Phones Title'].str.strip()
ios_df['Phones Title'] = ios_df['Phones Title'].str.strip()
main_df['Title'] = main_df['Title'].str.strip()

# Встановлюємо новий порядок колонок
new_order = ['Title','Category','OS','Image','Link','Price','Rating','Wish_count']
main_df = main_df[new_order]

main_df.to_excel('dataset.xlsx', index=False)
