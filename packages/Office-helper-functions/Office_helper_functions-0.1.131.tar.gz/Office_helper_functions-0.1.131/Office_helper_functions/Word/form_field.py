from bs4 import BeautifulSoup
import os
import zipfile
import io

def set_checkbox_value(xlsx_data, checkbox_value, checkbox_location):
    """Takes a Word document as a bytes object as input (from file.read() for example), returns a BytesIO to be opened by various libraries with one checkbox ticked.

    Args:
        xlsx_data (Bytes): Bytes representation of a Word document
        checkbox_value (int): 1 = checked, 0 = unchecked
        checkbox_location (int): which location from 0 to x your checkbox has in the number of checkboxes

    Returns:
        BytesIO: Returns a BytesIO to be used in document libraries
    """
    with zipfile.ZipFile(io.BytesIO(xlsx_data), mode='r') as zf:

        sheet1_data = zf.read('word/document.xml').decode('utf-8')
        soup = BeautifulSoup(sheet1_data, 'xml')

        std_elements_with_checkboxes = soup.find_all('w:sdt')
        x =std_elements_with_checkboxes[checkbox_location]
        if "checkbox" in str(x): 
            x.find('checked')['w14:val'] = checkbox_value
            x.find('w:t').string = ["☒" if checkbox_value==1 else "☐"][0]
                
        
        files = {x: zf.read(x) for x in zf.namelist()}
        modified_sheet1_data = str(soup)
        files['word/document.xml'] = modified_sheet1_data

    # Create a new in-memory ZipFile object
    output_zip = io.BytesIO()
    with zipfile.ZipFile(output_zip, mode='w') as zkf:
        for name, file in files.items():
            # Add each file to the new zipfile
            zkf.writestr(name, file)

    # Reset the output_zip's file pointer to the beginning
    output_zip.seek(0)
    return output_zip

def compress_word_file(word_file):
    """Adds an icon to a word file by first unzipping it, replacing an icon png file with a bytes object. returns a compressed BytesIO. No further processing is necessary to use as a document.

    Args:
        word_file (Bytes): Word file as a Bytes - object.
        icon_file (Bytes): Image object to be passed to the placeholder.

    Returns:
        BytesIO: BytesIO object to be opened or saved for word-document processing.
    """
    with zipfile.ZipFile(io.BytesIO(word_file), mode='r') as zf:

        files = {x: zf.read(x) for x in zf.namelist()}

    # Create a new in-memory ZipFile object
    new_word_file = io.BytesIO()
    with zipfile.ZipFile(new_word_file, mode='w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zkf:
        for name, file in files.items():
            # Add each file to the new zipfile
            zkf.writestr(name, file)

    # Reset the output_zip's file pointer to the beginning
    new_word_file.seek(0)
    return new_word_file


if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(__file__),'Fitness mall cert.docx'),'rb') as fh:
        file=set_checkbox_value(fh.read(), 1, 0)
    with open(os.path.join(os.path.dirname(__file__),'Fitness mall cert2.docx'),'wb') as fh:
        fh.write(file.read())
        
