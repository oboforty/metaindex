import requests
import shutil
from ftplib import FTP

DBs = ['hmdb', 'kegg', 'chebi', 'chemspider', 'pubchem', 'metlin']

LOG = ''
OFFLINE = True


def http_log(r, _id=None):
    global LOG
    LOG += "  {} GET {}\n    {}\n\n".format(r.status_code, r.url, r.content)


def get_http_log():
    global LOG

    f = str(LOG)
    LOG = ''

    return f


def download_file(url, local_filename):
    # NOTE the stream=True parameter below
    # with requests.get(url, stream=True) as r:
    #     r.raise_for_status()
    #     with open(local_filename, 'wb') as f:
    #         for chunk in r.iter_content(chunk_size=8192):
    #             if chunk: # filter out keep-alive new chunks
    #                 f.write(chunk)
    #                 # f.flush()

    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    return local_filename


def download_file_ftp(url, local_filename, username, password):
    ftp = FTP(url)
    ftp.login(username, password)

    # Get All Files
    files = ftp.nlst()

    # Print out the files
    for file in files:
        ftp.retrbinary("RETR " + file, open("download/to/your/directory/" + file, 'wb').write)

    ftp.close()

    print('All files downloaded for ' + str(diff.seconds) + 's')
