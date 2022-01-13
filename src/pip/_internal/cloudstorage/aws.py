import logging

from pip._internal.utils.misc import display_path
from pip._internal.utils.subprocess import make_command
from pip._internal.cloudstorage.cloudstorage import (
    CloudStorageProvider,
    CloudStorageObjectRef,
    cloudstorage,
)


logger = logging.getLogger(__name__)


class AWSStorage(CloudStorageProvider):
    name = "aws"
    subprocess_cmd = ("aws", "s3")
    scheme = "s3"

    def verify_aws_cli(self):
        self.run_command(["--version"], show_stdout=False, stdout_only=True)

    def download(self, ref: CloudStorageObjectRef, dest: str):
        logger.info("Downloading (with aws s3) %s to %s", ref, display_path(dest))
        self.verify_aws_cli()
        self.run_command(make_command("cp", str(ref), dest))


cloudstorage.register(AWSStorage)
