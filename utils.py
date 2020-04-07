import json
from pathlib import Path
from datetime import datetime, timedelta
import requests
import shutil
from tqdm import tqdm

STR_FMT = '%Y-%m-%dT%H:%M:%S'


def get_data(time_stamp):
    '''Get LTA realtime traffic data
    time stamp format: YYYY-MM-DD[T]HH:mm:ss (SGT)
    e.g. 2020-02-29T13:00:00
    2020-02-29T13%3A00%3A00
    '''
    res = ''
    while res == '':
        try:
            date, time = time_stamp.split('T')
            HH, mm, ss = time.split(':')
            API_STRING = 'https://api.data.gov.sg/v1/transport/traffic-images?date_time={}T{}%3A{}%3A{}'.format(
                date, HH, mm, ss)
            print(API_STRING)
            res = requests.get(API_STRING)
        except Exception as e:
            print(e)
            continue
    return res.json()

def get_camera_info(time_stamp):
    res = get_data(time_stamp)
    camera_info = dict()
    for cam in tqdm(res['items'][0]['cameras']):
        camera_info[cam['camera_id']] = {
            'location':cam['location'],
            'image_metadata':cam['image_metadata']
        }

    with open('camera_info.json', 'w') as outfile:
        json.dump(camera_info, outfile)

def save_image_from_url(image_url, image_name):
    resp = requests.get(image_url, stream=True)
    local_file = open(image_name, 'wb')
    resp.raw.decode_content = True
    shutil.copyfileobj(resp.raw, local_file)
    del resp

def datetime_range(start, end, delta):
        current = start
        while current < end:
            yield current
            current += delta
            
def time_series_images(time_stamp_start, time_stamp_end, camera_id, refresh_rate=60):
    '''Script to saves images to of a given camera id
    '''
    start = datetime.strptime(time_stamp_start, STR_FMT)
    end = datetime.strptime(time_stamp_end, STR_FMT)

    

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

def combine_csv(dir):
    '''Takes the folder dir and get all the csv and combine them to one big ass csv
    '''
    csv_files = Path(dir).glob('*.csv')
    with open('combined.csv', 'w') as f:
        for csv_f in csv_files:
            with open(csv_f, 'r') as ref:
                lines = ref.readlines()[1:]
            
            for line in lines:
                f.write('{},{}'.format(csv_f.stem,line))


if __name__ == "__main__":
    # start_time_stamp = '2020-03-06T10:40:00'
    # end_time_stamp = '2020-03-06T11:10:00'
    # camera_id = '2702'
    # time_series_images(start_time_stamp, end_time_stamp, camera_id)
    # res = get_data(start_time_stamp)
    # get_camera_info(start_time_stamp)
    pass