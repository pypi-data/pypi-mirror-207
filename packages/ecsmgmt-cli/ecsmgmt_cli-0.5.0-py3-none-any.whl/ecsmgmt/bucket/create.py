import click
from ecsclient.common.exceptions import ECSClientException

from .._util.echo import success
from .._util.exceptions import EcsmgmtClickException


@click.command()
@click.argument('bucket-name', type=click.STRING)
@click.pass_obj
def cli(obj: dict, bucket_name: str):
    """Create bucket
    """
    client = obj['client']
    namespace = obj['namespace']

    if len(bucket_name) > 255:
        raise EcsmgmtClickException('Bucket name too long. Maximum allowed length is 255 chars.')
    if not all(x.isalnum() or x == '.' or x == '-' or x == '_' for x in bucket_name):
        raise EcsmgmtClickException('Bucket name contains invalid characters. Only alphanumeric, ".", "-" or "_" is allowed.')

    try:
        client.bucket.create(bucket_name=bucket_name, namespace=namespace)
        success(f'created bucket "{bucket_name}" in namespace "{namespace}"')
    except ECSClientException as e:
        raise EcsmgmtClickException(e.message)
