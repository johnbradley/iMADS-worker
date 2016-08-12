"""
Command line utility to test out jobs portion of the API.
"""

from __future__ import print_function
import sys
import requests
import base64
from multiprocessing import Pool
from worker import PredictionsWorker
import time
import tempfile
import os


BASE_URL = "http://localhost:5000/api/v1"
TEST_SEQUENCE_FILE = '/Users/dcl9/Data/scratch/predictor-testdata/sequence.fa'

def make_url(part):
    return "{}/{}".format(BASE_URL, part)


def get_new_jobs():
    r = requests.get(make_url("jobs?job_status=NEW"))
    return r.json()['result']


def claim_job(job):
    url = make_url("jobs/{}".format(job['id']))
    data = {'job_status':'RUNNING'}
    r = requests.put(url, json=data)
    r.raise_for_status()


def mark_job_complete(job):
    url = make_url("jobs/{}".format(job['id']))
    data = {'job_status':'COMPLETE'}
    r = requests.put(url, json=data)
    r.raise_for_status()


def mark_job_error(job, message):
    url = make_url("jobs/{}".format(job['id']))
    data = {'job_status':'ERROR', 'error_message': message}
    r = requests.put(url, json=data)
    r.raise_for_status()


def get_sequence(job):
    url = make_url("sequences/{}".format(job['sequence_list']))
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()['data']
    return base64.b64decode(data)


def save_custom_predictions(job, bed_file_data):
    url = make_url("custom_predictions")
    r = requests.post(url, json={
        'job_id': job['id'],
        'model_name': job['model_name'],
        'bed_data': bed_file_data,
    })
    r.raise_for_status()


def write_data(data, filename):
    with open(filename, 'w') as f:
        f.write(data)


def read_data(filename):
    with open(filename, 'r') as f:
        return f.read()


def make_predictions(job):
    # Write the fasta data to a local file
    fasta_data = get_sequence(job)
    _, sequence_file = tempfile.mkstemp(suffix='.fa', prefix='prediction', dir='/Users/dcl9/Data/')
    write_data(fasta_data, sequence_file)
    model_name = job['model_name']
    worker = PredictionsWorker('prediction_config.json')
    bed_file = worker.run(sequence_file, model_name)
    os.unlink(sequence_file)
    return read_data(bed_file)


def list_jobs():
    print("NEW JOBS")
    for job in get_new_jobs():
        print('id:', job['id'])
        print('     model:', job['model_name'], ' type:', job['type'], 'sequence:', job['sequence_list'])
    print()


def claim_next_job():
    jobs = get_new_jobs()
    if not jobs:
        print("No jobs available to claim.")
    else:
        job = jobs[0]
        claim_job(job)
        try:
            bed_file_data = make_predictions(job)
            save_custom_predictions(job, base64.b64encode(bed_file_data))
            mark_job_complete(job)
        except Exception as ex:
            mark_job_error(job, str(ex))


def claim_many():
    pool = Pool()
    while True:
        pool.apply_async(claim_next_job)
        time.sleep(0.5)


def error_next_job():
    jobs = get_new_jobs()
    if not jobs:
        print("No jobs available to claim.")
    else:
        job = jobs[0]
    mark_job_error(job, "Processing failed with error DAN-8.")

def create_job():
    # upload sequence
    url = make_url("sequences")
    sequence_data = read_data(TEST_SEQUENCE_FILE)
    data = {'data': base64.b64encode(sequence_data)}
    r = requests.post(url, json=data)
    r.raise_for_status()
    sequence_id = r.json()['id']

    # make new job
    url = make_url("jobs")
    data = {
        'job_type': 'PREDICTION',
        'sequence_id': sequence_id,
        'model_name': 'HisMadMax_0007(NS)'
    }
    r = requests.post(url, json=data)
    r.raise_for_status()
    print("Job ID:", r.json()['id'])



COMMANDS = {
    "list": list_jobs,
    "claim": claim_next_job,
    "error": error_next_job,
    "loop": claim_many,
    "makejob": create_job
}


def usage():
    print("python {} {}".format(sys.argv[0], '|'.join(COMMANDS.keys())))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    else:
        func = COMMANDS.get(sys.argv[1])
        if func:
            func()
        else:
            usage()

