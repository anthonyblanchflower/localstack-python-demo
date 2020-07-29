from dataclasses import dataclass
import json
import boto3

S3_BUCKET = "example-bucket"


def get_s3():
    return boto3.client("s3")


@dataclass
class ExampleClass:
    name: str
    message: str

    @classmethod
    def get_by_name(cls, name: str):
        response = get_s3().get_object(Bucket=S3_BUCKET, Key=name)
        response = json.loads(response["Body"].read())
        return cls(response["name"], response["message"])

    def to_json(self):
        return json.dumps({"name": self.name, "message": self.message})

    def put_object(self):
        serialized_message = self.to_json().encode("utf-8")
        get_s3().put_object(Bucket=S3_BUCKET, Key=self.name, Body=serialized_message)
