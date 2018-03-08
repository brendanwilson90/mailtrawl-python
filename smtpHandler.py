import socket
import sys
import logging
import configparser


class SmtpHandler:

    def __init__(self, connection, client_addr):
        self.logger = logging.getLogger('smtplogger')
        self.logger.setLevel(logging.DEBUG)
        self.conf = configparser.ConfigParser()
        self.conf.read('mailtrawl.cfg')
        self.connection = connection
        self.client_addr = client_addr
        

    def handle_session(self):
        welcome = "220 %s" % self.conf.get('SMTP', 'SERVER_DOMAIN')
        self.connection.sendall(welcome.encode())