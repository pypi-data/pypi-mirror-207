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

if __name__ == '__main__':
    main2()