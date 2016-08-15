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

class Status(object):
    # Status constants
    new = 'NEW'
    running = 'RUNNING'
    complete = 'COMPLETE'
    error = 'ERROR'


class PredictionsClient(object):

    def __init__(self, base_url, output_dir, model_files_dir, config_file):
        """
        Initialize a client for running prediction jobs
        Parameters
        ----------
        base_url: URL to the tf-dna-predictions webserver API
        output_dir: Writable directory for generated predictions
        model_files_dir: Readable directory where .model files are stored
        config_file: Path to the tracks.yaml config file providing metadata for model files

        """
        self.base_url = base_url
        self.output_dir = output_dir
        self.model_files_dir = model_files_dir
        self.config_file = config_file

    def make_url(self, part):
        return "{}/{}".format(self.base_url, part)

    def get_new_jobs(self):
        r = requests.get(self.make_url("jobs?job_status={}".format(Status.new)))
        return r.json()['result']

    def claim_job(self, job):
        url = self.make_url("jobs/{}".format(job['id']))
        data = {'job_status': Status.running}
        r = requests.put(url, json=data)
        r.raise_for_status()

    def mark_job_complete(self, job):
        url = self.make_url("jobs/{}".format(job['id']))
        data = {'job_status': Status.complete}
        r = requests.put(url, json=data)
        r.raise_for_status()

    def mark_job_error(self, job, message):
        url = self.make_url("jobs/{}".format(job['id']))
        data = {'job_status': Status.error, 'error_message': message}
        r = requests.put(url, json=data)
        r.raise_for_status()

    def get_sequence(self, job):
        url = self.make_url("sequences/{}".format(job['sequence_list']))
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()['data']
        return base64.b64decode(data)

    def save_custom_predictions(self, job, bed_file_data):
        url = self.make_url("custom_predictions")
        r = requests.post(url, json={
            'job_id': job['id'],
            'model_name': job['model_name'],
            'bed_data': bed_file_data,
        })
        r.raise_for_status()

    @staticmethod
    def write_data(data, filename):
        with open(filename, 'w') as f:
            f.write(data)

    @staticmethod
    def read_data(filename):
        with open(filename, 'r') as f:
            return f.read()

    def make_predictions(self, job):
        # Write the fasta data to a local file
        fasta_data = self.get_sequence(job)
        _, sequence_file = tempfile.mkstemp(suffix='.fa', prefix='prediction')
        self.write_data(fasta_data, sequence_file)
        model_name = job['model_name']
        worker = PredictionsWorker('prediction_config.json')
        bed_file = worker.run(sequence_file, model_name)
        os.unlink(sequence_file)
        return self.read_data(bed_file)


    def list_jobs(self):
        print("NEW JOBS")
        for job in self.get_new_jobs():
            print('id:', job['id'])
            print('     model:', job['model_name'], ' type:', job['type'], 'sequence:', job['sequence_list'])
        print()


    def claim_next_job(self):
        print('Claiming job')
        jobs = self.get_new_jobs()
        if not jobs:
            print("No jobs available to claim.")
        else:
            job = jobs[0]
            self.claim_job(job)
            try:
                bed_file_data = make_predictions(job)
                self.save_custom_predictions(job, base64.b64encode(bed_file_data))
                self.mark_job_complete(job)
            except Exception as ex:
                self.mark_job_error(job, str(ex))


    def claim_many(self):
        pool = Pool()
        while True:
            try:
                self.claim_next_job()
            except Exception as ex:
                print('Exception claiming job', ex)
            time.sleep(0.5)


if __name__ == '__main__':
    base_url = 'http://152.3.173.232:5000/api/v1/'
    output_dir = "/Users/dcl9/Data/scratch/predictor-output"
    model_files_dir = "/Users/dcl9/Data/scratch/predictor-testdata"
    config_file = "/Users/dcl9/Data/scratch/predictor-testdata/tracks.yaml"
    client = PredictionsClient(base_url, output_dir, model_files_dir, config_file)
    client.claim_many()
