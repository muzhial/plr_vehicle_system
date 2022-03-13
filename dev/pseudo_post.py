import json
import requests
import time
import threading
import os

import schedule


POST_URL = 'http://1.117.56.33:8080/admin/measure/save'
COOKIES = {'session': '.eJxtzttOxSAQBdB_4dmHciuFXzHmhDKDkvRyAu3RxPjvIrW1ND7Oysye_UluPmJ6I2aJKz6RWwBiiAXqHYO-s85pbBWX0jMpXCuYsgisAdUjaIus5b13wlnouOOUCSc8L1c981S2WlHtPWvQadEBlXnU0jVeMI4ghQIN1AKjtKMtU1K6fAvSklxkTRi3NjSPd4xjSCnMUyLmORccw2R-Vsxow5QXTmIBakAISy0Rx_mBh93n92vSRueoTaqsjS5hcR6wzipyjipQJRX5L6i8OGiYX02YAD8O8eH6rcj5WwHAAZe_7BFtWuPlcsfz8W5V2x1_C798fQP3PsMz.YiyCNw.CTDrHyqmvSIJXFSa15Ndxl5izbk'}
HEADER = {'Content-type': 'application/json'}


def post_data(data, url):
    headers = HEADER
    cookies = COOKIES
    input_para = {
        'data': data
    }
    resp = requests.post(
        url=url,
        data=json.dumps(input_para),
        headers=headers,
        cookies=cookies)
    # data = json.loads(resp)
    # print(resp.status_code)
    return resp


def read_file(file):
    with open(file, 'r', encoding='GB18030') as f:
        res = f.readlines()
    return res


def to_datetime(str):
    assert len(str) == 17 or len(str) == 20
    recon_str = str[:4] + '-' + str[4:6] + '-' + str[6:8] + ' ' + str[
        8:10] + ':' + str[10:12] + ':' + str[12:14] + '.' + '{:0<6d}'.format(
            int(str[14:]))
    return recon_str


def parse_data(data, measure_addr):
    insert_datas = []
    data_list = [d.split() for d in data[2:]]
    for d in data_list:
        insert_datas.append(
            {
                'measure_time': to_datetime(d[0]),
                'coord_xyz': ' '.join(d[1:]),
                'measure_address': measure_addr
            }
        )
    return insert_datas


def job(measure_dir):
    record_file = os.path.basename(measure_dir) + '.txt'
    records = []
    if os.path.exists(record_file):
        with open(record_file, 'r') as f:
            records = f.readlines()
    red_file = records[-1].strip('\n') if len(records) > 0 else None

    measure_files = os.listdir(measure_dir)
    measure_files.sort(key=lambda fn: os.path.getmtime(
                       os.path.join(measure_dir, fn))
                       if not os.path.isdir(
                           os.path.join(measure_dir, fn)) else 0)
    if red_file in measure_files:
        measure_file_index = measure_files.index(red_file)
        measure_files = measure_files[measure_file_index + 1:]
    try:
        for measure_file in measure_files:
            results = read_file(os.path.join(measure_dir, measure_file))
            results = parse_data(results, measure_dir)
            # res = post_data(results, POST_URL)
            with open(record_file, 'w+') as f:
                f.write(measure_file)

        print(measure_files)

    except Exception as e:
        print(f'{e}\n{measure_files}\n')


def run_threaded(job_func, *args):
    job_thread = threading.Thread(target=job_func, args=(*args, ))
    job_thread.start()


def post_data_schedule(work_dir):
    # schedule.every().hour.do(job)
    # schedule.every().day.at("10:30").do(job)
    # schedule.every().monday.do(job)
    # schedule.every().wednesday.at("13:15").do(job)
    # schedule.every().minute.at(":17").do(job)  # 每分钟的 17 秒时间点运行 job 函数
    measure_dir = [os.path.join(work_dir, i)
                   for i in os.listdir(work_dir) if os.path.isdir(i)]
    for m in measure_dir:
        schedule.every(15).seconds.do(run_threaded, job, m)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    # f = './20220118173256454_displacement_result.txt'
    # results = read_file(f)
    # # print(len(results))
    # insert_datas = parse_data(results)
    # res = post_data(insert_datas[:3], 'http://1.117.56.33:8080/admin/measure/save')
    # print(res.text)

    post_data_schedule('./')
