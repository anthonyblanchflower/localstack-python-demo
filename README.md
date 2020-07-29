# localstack-python-demo

## Demonstrating use of localstack for pytest

### Start localstack container and provision localstack edge port

`docker-compose up`

### Running the test

`pytest test.py`

or execute the run_test.sh bash script

### Pre-requisites

This demonstration requires the pytest, boto3 and dataclasses libraries

### Overview of localstack

Originally developed by Atlassian (Confluence, Jira) but now developed independently, localstack helps you emulate AWS cloud services from containers and access them through an edge service on port 4566 (configurable via EDGE_PORT environmental variable) using the AWS core API's i.e. http://0.0.0.0:4566.

Some of the emulated services use existing AWS mocking libraries which are brought together within the localstack framework. For example, Localstack emulates s3 with the moto mocking library.

We can use a localstack image and provision the localstack port from a docker-compose.yml definition.

Localstack has a selection of environment variables that can be defined for the container to configure the emulated AWS services (https://github.com/localstack/localstack) such as EDGE_PORT. A minimum requirement is the SERVICES variable to define which AWS services to emulate (e.g. SERVICES=s3, lambda). Useful variables are DEBUG which displays all logs and DATA_DIR which defines the directory where localstack will save it's internal data.

### Overview of pytest

The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.

Pytest requires Python 3.5+. It can perform auto-discovery of test modules and functions.

Pytest provides modular fixtures for managing test resources (such as localstack resources).

Pytest can run unittest and nose test suites without additional configuration.

Pytest provides detailed information on failing assert statements

Pytest has a large active community and an extensive range of plug-ins is available (http://plugincompat.herokuapp.com/).

### Resources

https://github.com/localstack/localstack

https://hub.docker.com/r/localstack/localstack

https://docs.pytest.org/en/latest/index.html
