from setup.install import ScoopPackageManager

def main():
    """
    This method is the main method which will install all the dependencies required for the project.
    ERLang: It is a programming language used to build massively scalable soft real-time systems with requirements on high availability.
    RabbitMQ: It is an open-source message-broker software that originally implemented the Advanced Message Queuing Protocol and has since been extended with a plug-in architecture to support Streaming Text Oriented Messaging Protocol, MQ Telemetry Transport, and other protocols.
    """
    scoop = ScoopPackageManager()
    scoop.install_all()