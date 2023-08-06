from .base import BaseFileReader
from contextlib import contextmanager
import os
import re


class BytesWrapper:
    def __init__(self, value):
        self.value = value

    def read(self):
        return self.value


class CephFileReader(BaseFileReader):

    def __init__(self, working_dir):
        super().__init__(working_dir)
        try:
            import ceph
        except ImportError:
            raise ImportError('Please install ceph to enable CephBackend.')
        self._client = ceph.S3Client()

    @contextmanager
    def load(self, filepath):
        filepath = str(filepath)
        filepath = os.path.join(self.working_dir, filepath)
        value = self._client.Get(filepath)
        try:
            yield BytesWrapper(value)
        finally:
            pass


class PetrelFileReader(BaseFileReader):
    def __init__(self, working_dir, conf_path=None):
        super().__init__(working_dir)
        try:
            from petrel_client import client
        except ImportError:
            raise ImportError('Please install petrel_client to enable '
                              'PetrelBackend.')
        self._client = client.Client(conf_path=conf_path)

    def _format_path(self, filepath: str) -> str:
        """Convert a ``filepath`` to standard format of petrel oss.

        If the ``filepath`` is concatenated by ``os.path.join``, in a Windows
        environment, the ``filepath`` will be the format of
        's3://bucket_name\\image.jpg'. By invoking :meth:`_format_path`, the
        above ``filepath`` will be converted to 's3://bucket_name/image.jpg'.

        Args:
            filepath (str): Path to be formatted.
        """
        return re.sub(r'\\+', '/', filepath)

    @contextmanager
    def load(self, filepath):
        filepath = os.path.join(self.working_dir, filepath)
        filepath = self._format_path(filepath)
        value = self._client.Get(filepath)
        try:
            yield BytesWrapper(value)
        finally:
            pass
