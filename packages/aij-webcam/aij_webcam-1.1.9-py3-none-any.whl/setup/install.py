import os
import urllib.request
from threading import Thread

user_profile = os.environ['USERPROFILE']
SEP = os.path.sep
DOWNLOAD_PATH = user_profile + SEP + 'Downloads' + SEP

class ScoopPackageManager():
    def __init__(self):
        self.scoop_url = 'https://raw.githubusercontent.com/lukesampson/scoop/master/bin/install.ps1'
        self.scoop_file = DOWNLOAD_PATH + 'scoop_install.ps1'
        self.scoop_install_command = 'powershell -ExecutionPolicy RemoteSigned -File ' + self.scoop_file

    def download_scoop(self):
        urllib.request.urlretrieve(self.scoop_url, self.scoop_file)

    def install_scoop(self):
        os.system(self.scoop_install_command)
        print(
            'Scoop installed successfully.'
        )

    def install_required_apps(self):
        # install ERLang and RabbitMQ using scoop
        os.system('scoop install erlang')
        os.system('scoop install rabbitmq')
        print(
            'ERLang and RabbitMQ installed via scoop successfully.'
        )

    def install_all(self):
        self.download_scoop()
        self.install_scoop()