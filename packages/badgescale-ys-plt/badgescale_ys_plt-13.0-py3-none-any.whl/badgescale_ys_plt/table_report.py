import os
import pandas as pd
from datetime import datetime
import time

def main():
    df = pd.DataFrame(
        {
            "Name": [],
            "Age": [],
            "Sex": []
        }
    )

    print(df,'\n')

    df.loc['0', 'Name'] = 'n0'

    df.loc['1', 'Name'] = 'n1'
    
    df.loc['1', 'Age'] = 'a1'
    
    df.loc['2', 'Sex'] = 's2'
    
    print(df,'\n')

def main2():
    d1 = datetime.now()
    time.sleep(3)
    d2 = datetime.now()
    print (d2-d1)

def main3():
    report_file = './总体测试报告_2023-05-09T19.35.15.csv'
    df = pd.read_csv(report_file, header=0, dtype='unicode')
    print(df)

    count1 = df.index.size
    criteria = (df[df.columns[1]] == 'Pass') & \
        (df[df.columns[2]] == 'Pass') & \
        (df[df.columns[3]] == 'Pass') & \
        (df[df.columns[4]] == 'Pass') & \
        (df[df.columns[5]] == 'Pass') & \
        (df[df.columns[6]] == 'Pass') & \
        (df[df.columns[7]] == 'Pass') & \
        (df[df.columns[8]] == 'Pass') & \
        (df[df.columns[9]] == 'Pass') & \
        (df[df.columns[10]] == 'Pass')
    #criteria = (df[df.columns[3]] == 'Pass')
    count2 = df[criteria].index.size
    print('total:', count1, ' pass:', count2)

if __name__ == '__main__':
    main3()