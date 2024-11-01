import pandas as pd

def LoadData():
    data = pd.read_csv("data/cs_data.csv", encoding = 'utf-8', index_col = 0)
    data.columns = [col.lower() for col in data.columns] # columns 소문자 변경