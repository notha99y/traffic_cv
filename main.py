import os.path
import sys
import json
from datetime import datetime, timedelta
from PIL import Image
from tqdm import tqdm
sys.path.append("keras_yolo")

from keras_yolo.yolo import YOLO
from utils import datetime_range, get_data, save_image_from_url


STR_FMT = '%Y-%m-%dT%H:%M:%S'



if __name__ == "__main__":
    start_time_stamp = "2020-03-06T10:40:00"
    end_time_stamp = "2020-03-06T10:50:00"
    refresh_rate = 60
    start = datetime.strptime(start_time_stamp, STR_FMT)
    end = datetime.strptime(end_time_stamp, STR_FMT)

    dts = [
        dt.strftime(STR_FMT)
        for dt in datetime_range(start, end, timedelta(seconds=refresh_rate))
    ]

    od = YOLO()
    # main loop
    with open(os.path.join('results', start_time_stamp + '_to_' + end_time_stamp + '.json'), 'w') as json_file:
        result_dict = {}
        for time_stamp in tqdm(dts):
            with open(os.path.join('results', time_stamp + '.csv') , 'w') as f:
                f.write('CAMERA_ID,LAT,LONG,NUM_OF_VEH\n')
                result_dict[time_stamp] = {}
                print('Time stamp: ',time_stamp)
                res = get_data(time_stamp)
                juicy_bites = res["items"][0]["cameras"]
                for i, jui in enumerate(juicy_bites):
                    print("-" * 88)
                    print("[CAMERA ID]: ", jui["camera_id"])
                    print("[CAMERA LOCATION]: ", jui["location"])
                    print("[CAMERA IMAGE METADATA]: ", jui["image_metadata"])
                    save_name = os.path.join(
                        "data", "{}_{}.jpg".format(jui["camera_id"], time_stamp)
                    )
                    save_image_from_url(jui["image"], save_name)
                    print(save_name)
                    _image = Image.open(save_name)
                    image, detections = od.detect_image(_image)
                    print("[DETECTIONS]: ", len(detections))
                    fname, ext = os.path.splitext(save_name)
                    image.save(fname + "_detection" + ext)

                    f.write('{},{},{},{}\n'.format(jui['camera_id'], jui['location']['latitude'], jui['location']['longitude'], len(detections)))
                    result_dict[time_stamp]['camera_id_{}'.format(i)] = jui['camera_id']
                    result_dict[time_stamp]['latitude_{}'.format(i)] = jui['location']['latitude']
                    result_dict[time_stamp]['longitude_{}'.format(i)] = jui['location']['longitude']
                    result_dict[time_stamp]['num_of_veh_{}'.format(i)] = len(detections)
                    
        json.dump(result_dict, json_file)