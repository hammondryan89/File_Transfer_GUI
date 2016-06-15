import shutil
import os
import datetime



dir_src = os.path.dirname('%s')
dir_dst = os.path.dirname('%s')

now = datetime.datetime.now()
before = now - datetime.timedelta(hours = 24)


def move():
    for files in os.listdir(dir_src): 
        src_file = os.path.join(dir_src, files)
        dst_file = os.path.join(dir_dst, files)
        st = os.stat(src_file)
        mod_time = datetime.datetime.fromtimestamp(st.st_mtime)
        if mod_time > before:
            shutil.move(src_file, dst_file)
            print (dst_file)
        else:
            print (src_file +' has not been modifided in 24 Hours')

 
    
    
    

