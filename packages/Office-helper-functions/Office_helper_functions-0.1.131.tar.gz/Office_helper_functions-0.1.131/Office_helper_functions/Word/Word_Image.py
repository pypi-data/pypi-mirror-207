import zipfile
import io
def add_image_to_word_file(word_file, icon_file, imagepath):
    """Adds an icon to a word file by first unzipping it, replacing an icon png file with a bytes object. returns a compressed BytesIO. No further processing is necessary to use as a document.

    Args:
        word_file (Bytes): Word file as a Bytes - object.
        icon_file (Bytes): Image object to be passed to the placeholder.
        image_path (String): Path to the image inside the Word file. To find this, change the file ending to .zip and locate the filename in /word/media

    Returns:
        BytesIO: BytesIO object to be opened or saved for word-document processing.
    """
    with zipfile.ZipFile(io.BytesIO(word_file), mode='r') as zf:

        files = {x: zf.read(x) for x in zf.namelist()}
        files[imagepath] = icon_file

    # Create a new in-memory ZipFile object
    new_word_file = io.BytesIO()
    with zipfile.ZipFile(new_word_file, mode='w') as zkf:
        for name, file in files.items():
            # Add each file to the new zipfile
            zkf.writestr(name, file)

    # Reset the output_zip's file pointer to the beginning
    new_word_file.seek(0)
    return new_word_file


def compress_doc(word_file, icon_file, imagepath):
    """Adds an icon to a word file by first unzipping it, replacing an icon png file with a bytes object. returns a compressed BytesIO. No further processing is necessary to use as a document.

    Args:
        word_file (Bytes): Word file as a Bytes - object.
        icon_file (Bytes): Image object to be passed to the placeholder.
        image_path (String): Path to the image inside the Word file. To find this, change the file ending to .zip and locate the filename in /word/media

    Returns:
        BytesIO: BytesIO object to be opened or saved for word-document processing.
    """
    with zipfile.ZipFile(io.BytesIO(word_file), mode='r') as zf:

        files = {x: zf.read(x) for x in zf.namelist()}
        files[imagepath] = icon_file

    # Create a new in-memory ZipFile object
    new_word_file = io.BytesIO()
    with zipfile.ZipFile(new_word_file, mode='w', compression=zipfile.ZIP_DEFLATED) as zkf:
        for name, file in files.items():
            # Add each file to the new zipfile
            zkf.writestr(name, file)

    # Reset the output_zip's file pointer to the beginning
    new_word_file.seek(0)
    return new_word_file
