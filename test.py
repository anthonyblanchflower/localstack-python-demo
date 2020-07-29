from unittest.mock import patch

import boto3
import pytest

from app import ExampleClass, S3_BUCKET

# mock get_s3 and replace it with an s3 client connected to localstack edge service


@pytest.fixture
def s3_localstack():
    s3 = boto3.client("s3", endpoint_url="http://0.0.0.0:4566")
    s3.create_bucket(Bucket=S3_BUCKET)
    with patch("app.get_s3", return_value=s3):
        yield s3

# with mock in place, run the test


def test_create_and_get(s3_localstack):
    ExampleClass(name="example_name", message="This is an example message").put_object()

    example = ExampleClass.get_by_name("example_name")
    assert example.name == "example_name"
    assert example.message == "This is an example message"
