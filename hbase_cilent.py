from pathlib import Path
import csv
import happybase
import json
import time

batch_size = 88
host = "cloudera"
file_path = Path('.') / 'results' / '2020-03-06T10:40:00_to_2020-03-06T10:50:00.json'
namespace = "traffic_cv"
row_count = 0
start_time = time.time()
table_name = "2020-03-06T10:40:00"


class HappyBase:
    '''Class that connects to Hbase using Happy base api
    '''
    def __init__(self, host, namespace):
        print('Establishing connection to host: {}, namespace: {}'.format(host, namespace))
        self.conn = happybase.Connection(host = host,
            table_prefix = namespace,
            table_prefix_separator = ":")
        # print('Tables:')
        # print(self.conn.tables())
        self.conn.open()

    def insert_file(self, file_path):
        """ Insert a file into HBase.
        Rows have the following schema:
            [  CAMERA_ID,LAT,LONG,NUM_OF_VEH ]
        """
        with open(file_path, 'r') as json_file:
            json_data = json.load(json_file)
        file_name = file_path.stem
        table = self.conn.table(str(file_name))
        print('Adding data into table {}'.format(table))
        for ts in json_data:
            new_dict = dict()
            for k,v in json_data[ts].items():
                new_dict[k] = str(v)
            print('Inserting {}'.format(ts))
            table.put(row=ts, data=new_dict)


    def read_csv():
        csvfile = open(file_path, "r")
        csvreader = csv.reader(csvfile)
        return csvreader, csvfile

if __name__ == "__main__":
    happibase = HappyBase(host, namespace)

    # After everything has been defined, run the script.
    # conn, batch = connect_to_hbase()
    # print("Connect to HBase. table name: {}".format(table_name))
    # csvreader, csvfile = read_csv()
    # print("Connected to file. name: {}".format(file_path))

    # try:
    #     # Loop through the rows. The first row contains column headers, so skip that
    #     # row. Insert all remaining rows into the database.
    #     for row in csvreader:
    #         row_count += 1
    #         if row_count == 1:
    #             pass
    #         else:
    #             insert_row(batch, row)

    #     # If there are any leftover rows in the batch, send them now.
    #     batch.send()
    # finally:
    #     # No matter what happens, close the file handle.
    #     csvfile.close()
    #     conn.close()

    # duration = time.time() - start_time
    # print("Done. row count: {}, duration: {}3f s".format(row_count, duration))