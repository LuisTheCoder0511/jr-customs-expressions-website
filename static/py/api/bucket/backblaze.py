import os

from b2sdk.v2 import InMemoryAccountInfo
from b2sdk.v2 import B2Api


class BackBlaze:
    def __init__(self):
        self._bucket_name = "blaze-luisthecoder-images"

    def __authenticate__(self):
        self._key_id = os.getenv("BLAZE_KEY_ID")
        self._key_app = os.getenv("BLAZE_KEY_APP")
        info = InMemoryAccountInfo()
        self._b2_api = B2Api(info)
        self._b2_api.authorize_account("production", self._key_id, self._key_app)
        self._connect()

    def _connect(self):
        self._bucket = self._b2_api.get_bucket_by_name(self._bucket_name)

    def __upload__(self, file, filename):
        try:
            self._bucket.upload_bytes(file.read(), filename)
        except Exception as e:
            print(e)
            return False
        return True

    def __download__(self, global_filename):
        return self._bucket.get_file_info_by_name(global_filename).file_info['b2FileName']

    def __get_url__(self, global_filename):
        token = self._bucket.get_download_authorization(global_filename, 60)
        download_url = f"{self._bucket.get_download_url(global_filename)}?Authorization={token}"
        return download_url

    def __delete__(self, global_filename):
        try:
            file_list = self._bucket.list_file_versions(global_filename, 1)
            file_id = file_list[0]
            self._bucket.delete_file_version(file_id, global_filename)
        except Exception as e:
            print(e)
            return False
        return True


backblaze = BackBlaze()