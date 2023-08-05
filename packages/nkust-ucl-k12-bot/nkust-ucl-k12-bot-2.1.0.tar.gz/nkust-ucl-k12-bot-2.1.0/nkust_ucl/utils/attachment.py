import requests
import os
from io import BytesIO


class Attachment:
    def __init__(self, attachment_path):
        self.attachment_path = attachment_path

    def get_attachment(self):
        if self.attachment_path.startswith("http"):
            response = requests.get(self.attachment_path)
            content_type = response.headers.get("content-type")
            if content_type and "image" not in content_type:
                raise ValueError("URL does not point to an image")
            return BytesIO(response.content).read()
        elif os.path.isfile(self.attachment_path):
            with open(self.attachment_path, "rb") as f:
                return f.read()
        else:
            raise ValueError("Invalid attachment path")
