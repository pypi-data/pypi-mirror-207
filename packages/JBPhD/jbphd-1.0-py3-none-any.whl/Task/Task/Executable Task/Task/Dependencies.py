import subprocess
import platform
from datetime import datetime
import sys
import os

python_path = sys.executable
#print("\n\nChecking that Python is installed...")
#print(f'\n\nPath to Python: {python_path}')
now = datetime.now()
date_time_string = now.strftime("%d-%m-%y")
outputtime = now.strftime("%H:%M:%S")

cpurun = subprocess.Popen([python_path, 'cpudepsinstall.py'])


filename = "participant number.txt"

with open(filename, "r") as f:
    first_line = f.readline()
    words = first_line.split()
    participant_number = None
    for word in words:
        if word.isdigit():
            participant_number = int(word)

folder_name = f'Participant {participant_number}'
depfile = os.path.join(folder_name, f"{participant_number} - Dependency Installation.txt")

dir_path = os.path.dirname(os.path.realpath(__file__))

filename = "participant number.txt"

lines = '\n \n--------------------------------------------------------------- \n\n'

def dependencies():

    #print("\n\nStarting Dependency Installation...")
    startup_info = None
    if platform.system() == 'Windows':
        startup_info = subprocess.STARTUPINFO()
        startup_info.dwFlags |= subprocess.STARTF_USESHOWWINDOW


    with open(depfile, 'w+') as f:

        f.write("Python Path: " + python_path + lines)
        f.write('Installation commenced at: ' + outputtime + lines)
        proc = subprocess.Popen([python_path, '-m' , 'pip', 'install', '--upgrade', 'pip'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, startupinfo=startup_info)

        stdout, stderr = proc.communicate()
        output, error = proc.communicate()
        if stderr:
            f.write(stderr.decode('utf-8'))

            #print((stderr.decode('utf-8')))
            f.write('\n')
            raise Exception(f'At {outputtime}, an error occurred during the installation of the dependencies')
        f.write(stdout.decode('utf-8'))
        ##print(Exception)
        f.write('\n')

        packages = ['sendgrid','psutil','plyer','cryptography','pygame', 'pandas', 'google-auth', 'google-auth-oauthlib', 'google-auth-httplib2', 'google-api-python-client', 'Pillow']

        proc = subprocess.Popen([python_path, '-m' , 'pip', 'install'] + packages, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, startupinfo=startup_info)

        stdout, stderr = proc.communicate()
        output, error = proc.communicate()
        if stderr:
            f.write(stderr.decode('utf-8'))

            #print((stderr.decode('utf-8')))
            f.write('\n')
            raise Exception(f'At {outputtime}, an error occurred during the installation of the dependencies')
        f.write(stdout.decode('utf-8'))
        ##print(Exception)
        f.write('\n')
        #print("\n\nPackage Installation Complete")
dependencies()
import Export

from plyer import notification

notification.notify(
    title='Task Beginning',
    message='The task is now starting, it may take a short while to load and install all of the relevant files',
    app_name='My Python App',
    timeout=10,
)
cpurun.terminate()
