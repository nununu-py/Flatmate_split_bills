from filestack import Client


class ShareFile:

    def __init__(self, filepath, api_key='AP0Ooi2DVQNa7cvzKgrUsz'):
        self.api_key = api_key
        self.filepath = filepath

    def share_file(self):
        client = Client(self.api_key)
        file_link = client.upload(filepath=self.filepath)
        return file_link.url
