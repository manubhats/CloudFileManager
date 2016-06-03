__author__ = 'Manu'
'''
Created on Feb 5, 2015

@author: manubhat
'''
# Include the Dropbox SDK
# Include the GNUPG Library
import gnupg
import dropbox

access_token = 'H8ZZjpTqlvIAAAAAAAAAaCSwX6VIYEXHPlsU7NLb_oc0PwQaz6VMCWzPPGHfabKr'
client = dropbox.client.DropboxClient(access_token)
gpg = gnupg.GPG()
gpg.encoding = 'utf-8'

class mydropbox1:

    def encrypt(self, myfile):
        gpg = gnupg.GPG()
        print 'Encrypting file...........', myfile
        f = open(myfile, 'rb')
        dirs = 'F:/Crypton/'
        fname = myfile.split('/')[-1]
        status = gpg.encrypt_file(f,
                                  recipients=['manubhats@gmail.com'],
                                  output=dirs + fname,
                                  always_trust=True)

        print 'ok: ', status.ok
        print 'status: ', status.status
        print 'stderr: ', status.stderr

        print 'Uploading file..........'
        f = open(dirs + fname, 'rb')
        response = client.put_file('/' + fname, f, overwrite=True)
        print 'UPLOADED Complete \n', response


    def listdropbox(self):
        folder_metadata = client.metadata('/')
        filelist = []

        print folder_metadata['contents']

        for files in folder_metadata['contents']:
            if files['is_dir'] is False:
                filelist.append(files['path'])

        return filelist

    def downloaddropbox(self, myfile):
    # Download the file from Dropbox
        f = client.get_file(myfile)
    # Decrypt the downloaded file
        status = gpg.decrypt_file(f, passphrase='crypton', output='F:/' + myfile)

        print 'ok: ', status.ok
        print 'status: ', status.status
        print 'stderr: ', status.stderr
        print 'Downloading file..........'
        print 'DOWNLOAD Complete'

# References
#
# https://docs.python.org/2/library/tkinter.html
#
# https://pythonhosted.org/python-gnupg/
#
# https://www.python.org/