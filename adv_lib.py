#advanced functions library

from bas_lib import *
from mac_lib import *

import random
import time
import datetime

import cus_lib
cus_funct=cus_lib.cus_funct

def esegui (utente,comando,destinatario,testo):
  ambiente_attivo=cus_lib.ambiente_attivo
  #splitta testo
  comandobot=parametri=''
  if testo.find(' ')!=-1:
    parametri=testo[testo.index(' ')+1:].strip()
  try:
    if testo[0:2]==':'+trigger and testo[2:].split()[0] in e_privmsg:
	  comandobot=testo[2:].split()[0]
  except:
    pass
#esempio PING
#utente = PING
#comando = :12345
#esempio = PING :12345
  if utente == 'PING':
    e_ping(comando)
#esempio PRIVMSG
#utente = tizio
#comando = PRIVMSG
#destinatario = persona o #chan
#comandobot = +comando
#parametri = param1 param2
#esempio = <tizio> PRIVMSG persona :+comando param1 param2
  elif comando == 'PRIVMSG':
    if ambiente_attivo == '':
      if comandobot in e_privmsg:
        e_privmsg[comandobot](utente,destinatario,parametri)
    else:
      if comandobot in e_privmsg:
        e_privmsg[comandobot](utente,destinatario,parametri)
      else:
        e_privmsg[ambiente_attivo](utente,destinatario,testo[1:])
      
#esempio JOIN
#utente = tizio
#comando = JOIN
#destinatario = #chan
  elif comando == 'JOIN':
    if utente != nomebot:
	  e_join(utente,destinatario[1:])#destinatario inizia con ':'

def analisi (data): #sta cosa di sicuro si puo' fare con regex in tipo 2 righe
  riga=data.split("\n")
  for i in range(len(riga)-1):
    stampa = utente = comando = destinatario = testo = ''
    parola=riga[i].split()
    #parola[0] e' l'utente
    if parola[0][0]==':':
      if '!' in parola[0]:
        utente = parola[0][1:parola[0].index('!')]
      else:
        utente = parola[0][1:len(parola[0])]
    else:
      utente = parola[0][0:len(parola[0])]
    try:
      comando = parola[1]
      destinatario = parola[2]
      testo = riga[i][riga[i].index(parola[3]):]
    except:
      pass
    stampa = datetime.datetime.fromtimestamp(time.time()).strftime('%H-%M-%S')+\
	   ' <'+utente+'> '+comando+' '+destinatario+' '+testo #finale
#    stampa = '<'+utente+'> _utente_ '+comando+' _comando_ '+destinatario+' _destinatario_ '+testo+' _testo_' #debug
    if utente!=nomebot:
      print stampa
    esegui (utente,comando,destinatario,testo)

def ricarica (utente, destinatario, parametri) :
  if utente == owner:
    reload(cus_lib)
    cus_funct=cus_lib.cus_funct
    e_privmsg.update(cus_funct)
    print 'funzioni ricaricate'

adv_funct={'messaggio':messaggio,\
           'query':query,\
           'join':join,\
           'part':part,\
           'quit':cuit,\
           'notice':notice,\
           'ricarica':ricarica}

e_privmsg=dict(adv_funct,**cus_funct)
