from datetime import datetime, timedelta
from utils import datetime_range
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm
from pyramid.arima import auto_arima


STR_FMT = "%Y-%m-%dT%H:%M:%S"

def read_data():
    df = pd.read_csv(
        "results/combined.csv",
        names=["Time", "CAMERA_ID", "LAT", "LONG", "NUM_OF_VEH"],
    )
    
    df["Time"] = df["Time"].apply(lambda x: datetime.strptime(x, STR_FMT))
    df = df.set_index("Time")

    return df


def train_ARIMA(dataset):
    print("Searching for best ARIMA")
    stepwise_model = auto_arima(
        dataset,
        start_p=0,
        start_q=0,
        max_p=2,
        max_q=2,
        m=24,
        start_P=0,
        start_Q=0,
        max_P=2,
        max_Q=2,
        d=1,
        D=1,
        trace=True,
    )
    print("Done!")
    print('Fitting')
    stepwise_model.fit(dataset)
    print('Done!')
    return stepwise_model

if __name__ == "__main__":
    start_time_stamp = "2020-04-06T00:00:00"
    end_time_stamp = "2020-04-21T00:00:00"

    start = datetime.strptime(start_time_stamp, STR_FMT)
    end = datetime.strptime(end_time_stamp, STR_FMT)

    dts = [dt.strftime(STR_FMT) for dt in datetime_range(
        start, end, timedelta(hours=1))]
    df = read_data()
    list_of_time_series = []
    # df.to_csv('test.csv')
    for i in set(df["CAMERA_ID"]):
        list_of_time_series.append(
            df[df["CAMERA_ID"] == i].drop(columns=["CAMERA_ID", "LAT", "LONG"])
        )
    # list_of_models = []
    # predictions = []
    # for time_series in tqdm(list_of_time_series):
    #     model = train_ARIMA(time_series)
    #     list_of_models.append(model) 
    #     predictions.append(model.predict(24))
    
    # time_stamps = sorted(list(set(df.index)))
    # predictions_trans = list(map(list, zip(*predictions)))

    # for i, time_stamp in enumerate(time_stamps):
    #     time_stamp_str = time_stamp.strftime(STR_FMT)
    #     new_df = df[df.index == time_stamp].drop(columns=['NUM_OF_VEH'])
    #     _predictions = pd.Series(predictions_trans[i])
    #     print('Predictions: ', _predictions)
    #     new_df['Predictions'] = _predictions
    #     new_df.to_csv('{}_predictions.csv'.format(dts[i]))


