#advanced functions library

from bas_lib import *
from mac_lib import *

import random

def esegui (utente,comando,destinatario,testo):
#splitta testo
  comandobot=parametri=''
  if testo.find(' ')!=-1:
    parametri=testo[testo.index(' ')+1:].strip()
  try:
    if testo[0:2]==':'+trigger and testo[2:].split()[0] in comandibot:
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
    if comandobot in comandibot:
      e_privmsg[comandobot](utente,destinatario,parametri)
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
    stampa = '<'+utente+'> '+comando+' '+destinatario+' '+testo #finale
#    stampa = '<'+utente+'> _utente_ '+comando+' _comando_ '+destinatario+' _destinatario_ '+testo+' _testo_' #debug
    if utente!=nomebot:
      print stampa
    esegui (utente,comando,destinatario,testo)
  
def bacio (utente,destinatario,parametri) : #esempio di comando #debug:da testare
  ircprivmsg ( destinatario, utente+' manda un dolce bacio :* a '+parametri)

def deliranza (utente,destinatario,parametri) : #esempio scemo di action #debug:da testare
  if parametri=='':
    ircprivmsg ( destinatario, 'balla meglio di johnny depp', 1)

def game (utente,destinatario,parametri) : #semplice gioco, funzione di avvio #debug:da testare
  global attivo
  global r
  r=random.randint(0,10000)
  if not attivo and parametri == '':
    ircprivmsg ( destinatario, 'dite un numero da 0 a 10000 preceduto da +g')
    ircprivmsg ( destinatario, 'esempio: +g 10000')
    attivo=1

def gameon (utente,destinatario,parametri) : #semplice gioco, funzione di gioco #debug:da testare
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

def ping (utente,destinatario,parametri) : #debug:da testare
  ircprivmsg ( destinatario, utente+': pong!')

e_privmsg={'messaggio':messaggio,\
           'query':query,\
           'join':join,\
           'part':part,\
           'quit':cuit,\
           'notice':notice,\
           'delira':deliranza,\
           'game':game,\
           'bacio':bacio,\
           'g':gameon,\
           'ping':ping}