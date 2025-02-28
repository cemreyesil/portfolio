from django.conf import settings
from django.core.files.storage import FileSystemStorage


class MediaStorage(FileSystemStorage):
    file_overwrite = False
    default_acl = 'public-read'


class DocumentStorage(FileSystemStorage):
    file_overwrite = False
    default_acl = 'public-read'


class ImageSettingStorage(FileSystemStorage):
    file_overwrite = False
    default_acl = 'public-read'
