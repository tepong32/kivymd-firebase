import firebase_admin
from firebase_admin import storage


def upload_image_to_cloud(image_path):
    bucket = storage.bucket("bocaue-app.appspot.com")
    blob = bucket.blob(image_path)
    blob.upload_from_filename(image_path)

