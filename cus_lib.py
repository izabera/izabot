from __future__ import division
#custom functions library

from bas_lib import *
from mac_lib import *

import random

def game (utente,destinatario,parametri) :
  global attivo
  global r
  r=random.randint(0,10000)
  if not attivo and parametri == '':
    ircprivmsg ( destinatario, 'dite un numero da 0 a 10000 preceduto da +g')
    ircprivmsg ( destinatario, 'esempio: +g 10000')
    attivo=1

def gameon (utente,destinatario,parametri) :
  global attivo
  if attivo!=1 :
    ircprivmsg ( destinatario, 'gioco non attivo')
  else:
    try:
      numero = int(parametri)

      if r==numero :
        ircprivmsg ( destinatario, 'congratulazioni '+utente+'! hai indovinato!')
        attivo = 0
      elif r<numero :
        ircprivmsg ( destinatario, 'troppo grande!')
      else :
        ircprivmsg ( destinatario, 'troppo piccolo!')
    except:
      print 'errore'

def bacio (utente,destinatario,parametri) :
  ircprivmsg ( destinatario, utente+' manda un dolce bacio :* a '+parametri)

def deliranza (utente,destinatario,parametri) :
  if parametri=='':
    ircprivmsg ( destinatario, 'balla meglio di johnny depp', 1)

def calcola (utente,destinatario,parametri) :
  if parametri!='':
    try:
      output=eval(parametri)
      ircprivmsg(destinatario,parametri+'='+str(output))
    except:
      ircprivmsg(destinatario,'errore')

#'comando':nome_funzione
#attenzione a non creare conflitti
#comandi e nomi funzionio vietati:
#'messaggio':messaggio
#'query':query
#'join':join
#'part':part
#'quit':cuit
#'notice':notice
#'ping':ping
#'ricarica':ricarica
cus_funct={'delira':deliranza,\
           'bacio':bacio,\
           'g':gameon,\
           'game':game,
           'calcola':calcola}
