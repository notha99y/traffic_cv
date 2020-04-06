import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime
def read_data():
    df = pd.read_csv('results/combined.csv', names = ['Time', 'CAMERA_ID','LAT','LONG','NUM_OF_VEH'])
    str_format = '%Y-%m-%dT%H:%M:%S'
    df['Time'] = df['Time'].apply(lambda x: datetime.strptime(x, str_format))
    df = df.set_index('Time')
    

    return df

if __name__ == "__main__":
    df = read_data()
    list_of_ts = []
    for i in set(df['CAMERA_ID']):
        list_of_ts.append(df[df['CAMERA_ID'] == i].drop(columns = ['CAMERA_ID','LAT','LONG']))