import pandas as pd

input_csv = r"phones_data.csv"
output_xlsx = 'phones.xlsx'

df = pd.read_csv(input_csv)

df.to_excel(output_xlsx,index=False)