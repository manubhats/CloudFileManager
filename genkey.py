__author__ = 'Manu'
'''
Created on Feb 9, 2015

@author: manubhat
'''

import gnupg

gpg = gnupg.GPG()

ascii_armored_public_keys = gpg.export_keys('A75C7D15')
ascii_armored_private_keys = gpg.export_keys('A75C7D15', True)
f = open('mykey.asc', 'wb')
# with open('mykey.asc', 'wb') as f:
f.write(ascii_armored_public_keys)
f.write(ascii_armored_private_keys)

