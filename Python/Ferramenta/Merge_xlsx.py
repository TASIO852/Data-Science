import pandas as pd # Unificar planilhas
import csv

def merge_excel(csv_address1, csv_address2):
    
    file1 = open(csv_address1)
    csv_reader1 = csv.reader(file1)
    header = next(csv_reader1)
    
    
    file2 = open(csv_address2)
    csv_reader2 = csv.reader(file2)
    header = next(csv_reader2)
    
    rows = []
    
    for row in csv_reader1:
        rows.append(row)
        df = pd.DataFrame(rows)
        # df.to_csv('myfile.csv')
    file1.close()
    
    rows = []
    
    for row in csv_reader2:
        rows.append(row)
        df2 = pd.DataFrame(rows)
        # df.to_csv('myf.csv')
    file2.close()
    
    df_merge = df.merge(df2, how='outer')
    df_merge.to_csv('contas.csv')