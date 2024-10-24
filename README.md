# Rozetka Smartphone Data Scraping

This project is designed for scraping smartphones from the Rozetka website, processing the data, and performing analysis. The collected data can be used to analyze the relationships between price, rating, and the number of wishes, as well as to display phone brands by category.

## File Descriptions

- **`rozetka.py`**  
  This script scrapes all smartphones from the Rozetka website, including information such as price, rating, number of wishes, and other characteristics.

- **`android_os.py`**  
  Scrapes smartphones running on the Android operating system. These data can be used to compare Android devices with others.

- **`ios_os.py`**  
  Scrapes smartphones running on the iOS operating system. The collected data allows analysis of iOS phones.

- **`dataset.py`**  
  Cleans the scraped data and generates a **`dataset.xlsx`** file for further analysis and visualization.

## Analysis and Visualization

In this project, the following analyses were conducted:
- Price-to-rating relationship.
- Number of user wishes for each smartphone model.
- Grouping smartphones by brand with clickable hyperlinks to the products on the Rozetka website.

The visualizations help to better understand trends in the relationships between price, rating, and the number of wishes.

## Results

This project helped to explore and compare different smartphones across popular categories, creating insightful charts and tables for further analysis.

You can view the interactive dashboard with the results of the analysis here:  
[Tableau Dashboard](https://public.tableau.com/app/profile/yurii.pozho/viz/Phonesbyrozetka/Dashboard1?publish=yes)

## How to Use

1. Run `rozetka.py` to scrape data on all smartphones.
2. Use `android_os.py` or `ios_os.py` to scrape smartphones with specific operating systems.
3. Run `dataset.py` to clean the data and generate the `dataset.xlsx` file for further analysis.

