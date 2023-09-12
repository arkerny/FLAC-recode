import os
import subprocess
import time

def trans(path):
    pathDir = os.listdir(path)
    log = open('log.txt', 'w', encoding = 'utf-8')

    log.write('$ Time: ' + time.strftime("%a %b %d %H:%M %Y", time.localtime()) + '\n')
    log.write('---------- Start ----------' + '\n')

    for allDir in pathDir:
        saveDir = allDir.replace('.flac', '_recode.flac')
        saveDir = saveDir.replace('.mp3', '_recode.flac')
        cmd = 'ffmpeg -y -i "' + path + allDir + '" "' + path + '00_' + saveDir + '"'
        log.write('$ Time: ' + time.strftime("%a %b %d %H:%M %Y", time.localtime()) + '\n')
        log.write('# ' + cmd + ' Start!' + '\n')
        ret = subprocess.getoutput(cmd)
        log.write(ret + '\n')
        log.write('# ' + allDir + ' Done!' + '\n')
        log.write('---------- Next ----------' + '\n')

    log.write('$ Time: ' + time.strftime("%a %b %d %H:%M %Y", time.localtime()) + '\n')
    log.write('---------- End ----------' + '\n')
    print("Done!")

if __name__ == '__main__':
    path = input('Please input dir path: ')
    trans(path)