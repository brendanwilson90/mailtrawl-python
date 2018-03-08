import socket
import sys
import logging
import configparser
from smtpHandler import SmtpHandler

logger = logging.getLogger('mainlogger')
out_hdlr = logging.StreamHandler(sys.stdout)
out_hdlr.setLevel(logging.DEBUG)
logger.addHandler(out_hdlr)


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
        smtp = SmtpHandler(conn, client_addr)
        smtp.handle_session()

if __name__ == '__main__':
    main()