from botocore.exceptions import ClientError


def check_album(album: str):
    if album.count("/"):
        raise Exception("album cannot contain '/'")


def get_image_key(album, image):
    return album + '/' + image


def is_album_exist(session, bucket, album):
    list_objects = session.list_objects(
        Bucket=bucket,
        Prefix=album + '/',
        Delimiter='/',
    )
    if "Contents" in list_objects:
        for _ in list_objects["Contents"]:
            return True
    return False


def is_image_exist(session, bucket, album, photo):
    try:
        session.get_object(Bucket=bucket, Key=get_image_key(album, photo))
    except ClientError as error:
        if error.response["Error"]["Code"] != "NoSuchKey":
            raise error
        return False
    return True
