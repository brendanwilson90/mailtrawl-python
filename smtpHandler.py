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
        

    def greeting(self, domain):
        # Handle greeting
        welcome = "220 %s\n" % domain
        self.connection.sendall(welcome.encode())
        response = self.connection.recv(512)
        response = response.split()
        client_hostname = response.pop()
        acknowledge = '250 %s Hello [%s]\n' % (domain, self.client_addr[0])
        self.connection.sendall(acknowledge.encode())