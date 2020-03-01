import json
from datetime import datetime, timedelta
import requests
import shutil


def get_data(time_stamp):
    '''Get LTA realtime traffic data
    time stamp format: YYYY-MM-DD[T]HH:mm:ss (SGT)
    e.g. 2020-02-29T13:00:00
    2020-02-29T13%3A00%3A00
    '''
    date, time = time_stamp.split('T')
    HH, mm, ss = time.split(':')
    API_STRING = 'https://api.data.gov.sg/v1/transport/traffic-images?date_time={}T{}%3A{}%3A{}'.format(
        date, HH, mm, ss)
    print(API_STRING)
    res = requests.get(API_STRING)

    return res.json()


def save_image_from_url(image_url, image_name):
    resp = requests.get(image_url, stream=True)
    local_file = open(image_name, 'wb')
    resp.raw.decode_content = True
    shutil.copyfileobj(resp.raw, local_file)
    del resp


def time_series_images(time_stamp_start, time_stamp_end, camera_id, refresh_rate=60):
    '''Script to saves images to of a given camera id
    '''
    STR_FMT = '%Y-%m-%dT%H:%M:%S'
    start = datetime.strptime(time_stamp_start, STR_FMT)
    end = datetime.strptime(time_stamp_end, STR_FMT)

    def datetime_range(start, end, delta):
        current = start
        while current < end:
            yield current
            current += delta

    dts = [dt.strftime(STR_FMT) for dt in datetime_range(
        start, end, timedelta(seconds=refresh_rate))]

    for time_stamp in dts:
        res = get_data(time_stamp)
        juicy_bites = res['items'][0]['cameras']
        for jui in juicy_bites:
            if jui['camera_id'] == camera_id:
                interested_jui = jui
        save_image_from_url(
            interested_jui['image'], '{}_{}.jpg'.format(camera_id, time_stamp))


if __name__ == "__main__":
    start_time_stamp = '2020-02-29T13:00:00'
    end_time_stamp = '2020-02-29T14:00:00'
    camera_id = '2701'
    time_series_images(start_time_stamp, end_time_stamp, camera_id)
