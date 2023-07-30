import dropbox
import os
from dropbox.files import WriteMode
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        Datasave = dropbox.Dropbox(self.access_token)
        for root, folder, file in os.walk(file_from):
            for i in file:
                firstpath = os.path.join(root,i)
                relativepath = os.path.relpath(firstpath, file_from)
                dropboxpath = os.path.join(file_to, relativepath)
        with open(file_from, 'rb') as file1:
             Datasave.files_upload(file1.read(),dropboxpath,mode = WriteMode("overwrite"))

def main():
    access_token = ""
    transferData =  TransferData(access_token)
    gateway = input("Enter the path of files to upload: ")
    arrival = input("Enter the path to upload the files onto Dropbox: ")
    transferData.upload_file(gateway, arrival)
    print("THE FILE HAS BEEN MOVED SUCCESSFULLY")

main()