import os
import json
import base64
from glob import glob


class FileInterface:
    def __init__(self):
        os.chdir('files/')

    def list(self,params=[]):
        try:
            filelist = glob('*.*')
            return dict(status='OK',data=filelist)
        except Exception as e:
            return dict(status='ERROR',data=str(e))

    def get(self,params=[]):
        try:
            filename = params[0]
            if (filename == ''):
                return None
            fp = open(f"{filename}",'rb')
            isifile = base64.b64encode(fp.read()).decode()
            return dict(status='OK',data_namafile=filename,data_file=isifile)
        except Exception as e:
            return dict(status='ERROR',data=str(e))

    def upload(self,params=[]):
        os.chdir('../')

        try:
            filename = params[0]
            
            if (filename == ''):
                return None

            fp = open(f"{filename}",'rb')
            isifile = base64.b64encode(fp.read())
            fp.close()

            uploadedfp = open(f'./files/{filename}', 'wb')
            uploadedfp.write(base64.b64decode(isifile))
            uploadedfp.close()

            os.chdir('files/')
            return dict(status='OK',data_namafile=filename)
        except Exception as e:
            os.chdir('files/')
            return dict(status='ERROR',data=str(e))

    def delete(self,params=[]):
        try:
            filename = params[0]

            if (filename == ''):
                return None
            
            os.remove(filename)

            return dict(status='OK')
        except Exception as e:
            return dict(status='ERROR',data=str(e))

if __name__=='__main__':
    f = FileInterface()
    print(f.list())
    print(f.get(['pokijan.jpg']))
