from setuptools import setup

setup(name='Predict-TF-Binding-Service',
  version='0.0.1',
  description='Command-line tool to run cwl workflows for TF binding predictions.',
  packages=['predict_service'],
  install_requires=['setuptools>=18.5', 'cwltool','PyYAML'],
  test_suite='nose.collector',
  tests_require=['nose'],
  entry_points={
    'console_scripts': ['predict_service=predict_service.main:main'],
  }
)
