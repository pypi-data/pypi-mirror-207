import logging
from pathlib import Path
from typing import BinaryIO, Dict, Mapping

import requests

from kognic.base_clients.cloud_storage.upload_spec import UploadSpec, UploadableData
from kognic.base_clients.retry_support import request_with_retry

log = logging.getLogger(__name__)


class UploadHandler:

    def __init__(self, max_retry_attempts: int = 23, max_retry_wait_time: int = 60, timeout: int = 60) -> None:
        """
        :param max_retry_attempts: Max number of attempts to retry uploading a file to GCS.
        :param max_retry_wait_time:  Max with time before retrying an upload to GCS.
        :param timeout: Max time to wait for response from server.
        """
        self.max_num_retries = max_retry_attempts
        self.max_retry_wait_time = max_retry_wait_time  # seconds
        self.timeout = timeout  # seconds

    #  Using similar retry strategy as gsutil
    #  https://cloud.google.com/storage/docs/gsutil/addlhelp/RetryHandlingStrategy
    def _upload_file(self, upload_url: str, file: UploadableData, headers: Dict[str, str]) -> None:
        """
        Upload the file to GCS, retries if the upload fails with some specific status codes or timeouts.
        """
        request_with_retry(requests.put,
                           self.max_num_retries,
                           self.max_retry_wait_time,
                           url=upload_url,
                           data=file,
                           headers=headers)

    def upload_files(self, upload_specs: Mapping[str, UploadSpec]) -> None:
        """
        Upload all files to cloud storage

        :param upload_specs: map between filename and details of what to upload where
        """
        for (resource_id, upload_spec) in upload_specs.items():
            if upload_spec.data is None and upload_spec.callback is None:
                self._upload_from_local_file(upload_spec)
            elif upload_spec.data is not None:
                self._upload_from_blob(upload_spec)
            elif upload_spec.callback is not None:
                self._upload_from_callback(upload_spec)

    def upload_file(self, file: BinaryIO, url: str) -> None:
        headers = {"Content-Type": "application/json"}
        self._upload_file(url, file, headers)

    def _upload(self, upload_spec: UploadSpec, data: UploadableData):
        headers = {"Content-Type": upload_spec.content_type}
        self._upload_file(upload_spec.destination, data, headers)

    def _upload_from_blob(self, upload_spec: UploadSpec):
        log.debug(f"Blob upload for filename={upload_spec.filename}")
        self._upload(upload_spec, upload_spec.data)

    def _upload_from_local_file(self, upload_spec: UploadSpec):
        log.debug(f"Upload from local file for filename={upload_spec.filename}")
        file = Path(upload_spec.filename).expanduser().open('rb')
        self._upload(upload_spec, file)

    def _upload_from_callback(self, upload_spec: UploadSpec):
        log.debug(f"Upload from callback for filename={upload_spec.filename}")
        try:
            data = upload_spec.callback(upload_spec.filename)
            self._upload(upload_spec, data)
        except Exception as e:
            raise Exception("Failed to upload file: callback failed", e)
        pass
