from docker import Client
import json

class WorkerException(Exception):
    pass

class PredictionsWorker(object):

    @staticmethod
    def load_config(config_path):
        with open(config_path, 'r') as f:
            return json.load(f)

    def __init__(self, config_path):
        self.config = PredictionsWorker.load_config(config_path)

    def _make_prediction_job(self, sequence_file, model_identifier):
        job = dict(self.config)
        job['input_sequence_file'] = sequence_file
        job['model_identifier'] = model_identifier
        return job

    def _create_container(self, cli, **kwargs):
        # Since the container will run other containers, we must bind-mount docker.sock
        docker_sock = '/var/run/docker.sock'
        # CWL uses /tmp to exchange files, so we must mount that too.
        tmp = '/tmp'

        command = ['main.py',
                   '--sequence-file', kwargs.get('input_sequence_file'),
                   '--model-identifier', kwargs.get('model_identifier'),
                  '--config-file-path', kwargs.get('config_file_path'),
                   '--model-files-directory', kwargs.get('model_files_directory'),
                  '--output-directory', kwargs.get('output_directory')]

        # Volumes are specified in a list and backed up by a host config
        volumes = [kwargs.get(x) for x in ['input_sequence_file', 'config_file_path', 'model_files_directory','output_directory']]
        volumes.extend([docker_sock, tmp])
        binds = dict()
        for v in volumes:
            mode = 'rw' if v == kwargs.get('output_directory') else 'rw'
            binds[v] = {'bind': v, 'mode': mode}
        host_config = cli.create_host_config(binds=binds)

        container = cli.create_container(kwargs.get('image_name'), command, volumes=volumes, host_config=host_config)
        return container

    @staticmethod
    def _extract_output(cli, container):
        # Docker image is configured to return the output file
        output_filename = cli.logs(container, tail=1).strip()
        return output_filename

    def run(self, sequence_file, model_identifier):
        job = self._make_prediction_job(sequence_file, model_identifier)
        client = Client(version='auto')
        container = self._create_container(client, **job)
        print 'Started container: {}'.format(container)
        response = client.start(container)
        if response is not None:
            raise(WorkerException('Unable to start container', response))
        # Container is started and will exit with a result code when completed
        result = client.wait(container)
        if result == 0:
            output = self._extract_output(client, container)
            client.remove_container(container)
            return output
        else:
            logs = client.logs(container)
            client.remove_container(container)
            raise(WorkerException('Container returned nonzero', {'result': result, 'logs': logs}))
