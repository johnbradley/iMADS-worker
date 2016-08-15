#!/usr/bin/env python

from __future__ import print_function
import requests
import base64
from multiprocessing import Pool
from worker import PredictionsWorker
import time
import tempfile
import os
from config import Config


class Status(object):
    """
    Status constants for API
    """
    new = 'NEW'
    running = 'RUNNING'
    complete = 'COMPLETE'
    error = 'ERROR'


class PredictionsClient(object):
    claim_interval = 0.5

    def __init__(self, config):
        """
        Initialize a client for running prediction jobs

        """
        self.config = config

    def make_url(self, part):
        return "{}/{}".format(self.config.base_url, part)

    def get_new_jobs(self):
        url = self.make_url("jobs?job_status={}".format(Status.new))
        r = requests.get(url)
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
        _, sequence_file = tempfile.mkstemp(suffix='.fa', prefix='prediction', dir=self.config.output_dir)
        self.write_data(fasta_data, sequence_file)
        model_name = job['model_name']
        worker = PredictionsWorker(self.config)
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
        jobs = self.get_new_jobs()
        if jobs:
            job = jobs[0]
            self.claim_job(job)
            try:
                bed_file_data = self.make_predictions(job)
                self.save_custom_predictions(job, base64.b64encode(bed_file_data))
                self.mark_job_complete(job)
            except Exception as ex:
                self.mark_job_error(job, str(ex))

    def claim_many(self):
        pool = Pool()
        while True:
            pool.apply_async(claim_next_job_async, (self,))
            time.sleep(self.claim_interval)
            # Result is currently discarded


# apply_async does not work on instance methods, so we declare a simple function
def claim_next_job_async(cli):
    return cli.claim_next_job()


if __name__ == '__main__':
    c = Config()
    # Local overrides
    cli = PredictionsClient(c)
    cli.claim_many()
