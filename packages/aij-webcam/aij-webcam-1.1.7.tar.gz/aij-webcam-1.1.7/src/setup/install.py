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

    def run(self):
        self.download_scoop()
        self.install_scoop()

class ErLangInstallerThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.erlang_url = 'https://raw.githubusercontent.com/kerl/kerl/master/kerl'
        self.erlang_file = DOWNLOAD_PATH + 'kerl'
        self.erlang_install_command = 'scoop install erlang'

    def download_erlang(self):
        urllib.request.urlretrieve(self.erlang_url, self.erlang_file)

    def install_erlang(self):
        os.system(self.erlang_install_command)

    def run(self):
        self.download_erlang()
        self.install_erlang()


class RabbitMQInstallerThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.rabbitmq_url = 'https://raw.githubusercontent.com/rabbitmq/rabbitmq-server/master/scripts/rabbitmq-defaults'
        self.rabbitmq_file = DOWNLOAD_PATH + 'rabbitmq-defaults'
        self.rabbitmq_install_command = 'scoop install rabbitmq'

    def download_rabbitmq(self):
        urllib.request.urlretrieve(self.rabbitmq_url, self.rabbitmq_file)

    def install_rabbitmq(self):
        os.system(self.rabbitmq_install_command)

    def run(self):
        self.download_rabbitmq()
        self.install_rabbitmq()

