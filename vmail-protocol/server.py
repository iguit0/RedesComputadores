#!/usr/bin/python3
# coding: UTF-8

# https://github.com/iguit0/Redes-De-Computadores

from datetime import datetime
import smtpd
import asyncore

def welcome_msg():
  print('                      _  _                                                  _  ')
  print('                     (_)| |                         _                      | | ')
  print(' _   _  ____   _____  _ | |    ____    ____  ___  _| |_  ___    ____  ___  | | ')
  print('| | | ||    \ (____ || || |   |  _ \  / ___)/ _ \(_   _)/ _ \  / ___)/ _ \ | | ')
  print(' \ V / | | | |/ ___ || || |   | |_| || |   | |_| | | |_| |_| |( (___| |_| || | ')
  print('  \_/  |_|_|_|\_____||_| \_)  |  __/ |_|    \___/   \__)\___/  \____)\___/  \_)')
  print('                              |_|                                              ')
  print('\n')
  return None

class vMailServer(smtpd.SMTPServer):
    no = 0
    def __init__(*args, **kwargs):
        welcome_msg()
        print('\tServidor vMail rodando na porta ' + str(PORT))
        smtpd.SMTPServer.__init__(*args, **kwargs)

    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        filename = '%s-%d.eml' % (datetime.now().strftime('%Y%m%d%H%M%S'),self.no)
        print(filename) # nome do arquivo a ser gerado
        f = open(filename, 'wb')
        f.write(data)
        f.close
        print('%s salvo com sucesso.' % filename)
        self.no += 1
        pass

if __name__ == "__main__":
    PORT = 8000
    smtp_server = vMailServer(('localhost', PORT), None)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        smtp_server.close()
