import socket
import sys
import logging
import configparser
import threading
from smtpHandler import SmtpHandler

logger = logging.getLogger('mainlogger')
out_hdlr = logging.StreamHandler(sys.stdout)
out_hdlr.setLevel(logging.DEBUG)
logger.addHandler(out_hdlr)
logger.setLevel(logging.DEBUG)


def connection_handler(connection, client_addr, conf):
    smtp = SmtpHandler(connection, client_addr)
    smtp.greeting(conf.get('SMTP', 'SERVER_DOMAIN'))
    connection.close()

def main():
    if len(sys.argv) > 1:
        print("Usage: mailtrawl.py")
    conf = configparser.ConfigParser()
    conf.read('mailtrawl.cfg')
    
    # Starts a listener on specified port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('localhost', conf.getint('SMTP', 'PORT'))
    s.bind(addr)
    s.listen(1)

    #Main handler loop
    while True:
        conn, client_addr = s.accept()
        logger.debug('Incoming connection from %s', client_addr)
        threading.Thread(target=connection_handler, args=(conn, client_addr, conf)).start()


if __name__ == '__main__':
    main()