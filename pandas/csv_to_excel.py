import pandas as pd

csv_file=pd.read_csv(r'C:\Users\Aswani\PycharmProjects\pythonDecember\fileIO\covid_19_india.csv')
csv_file.to_excel(r'F:\demo_works\file.xlsx',index=None,header=True)