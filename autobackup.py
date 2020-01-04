import schedule
import time
import os
import zipfile
import shutil

########### schedule time ###########
def job():
    print("Making schedule backup...")

schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("08:00").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("09:00").do(job)
# schedule.every().minute.at(":19").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

########### backup process ###########

# copy folder and compress it into a zip file
def docopy(source_folder, target_folder):
    for subdir, dirs, files in os.walk(source_folder):
        for file in files:
            print os.path.join(subdir, file)
            shutil.copy2(os.path.join(subdir, file), target_folder)

if __name__ =='__main__':
    print 'Starting Execution'

    # compress into zip
    ## for windows ##
    source_folder = 'path:\\...\name'
    target_zip = 'path:\\...\name.zip'
    doprocess(source_folder, target_zip)

    # copy to backup folder
    ## for windows ##
    source_folder = 'path:\\...\name'
    target_folder = 'path:\\...\name_backup'
    docopy(source_folder, target_folder)


    print 'Ending execution'    
