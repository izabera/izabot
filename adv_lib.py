#advanced functions library

from bas_lib import *
from mac_lib import *

import random

def esegui (utente,comando,destinatario,comandobot,parametri):
#utente = izabera
#comando = PRIVMSG, JOIN, PART
#destinatario = #izabot (channel)
#comandobot = +messaggio
#parametri = qualcuno blablabla

#  print 'comandobot: '+comandobot+', parametri: '+parametri #debug
  funzioni[comandobot](utente,comando,destinatario,parametri)

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
    print stampa
    if testo[0:2]==':'+trigger and testo[2:].split()[0] in comandibot:
      if testo.find(' ')!=-1:
        esegui (utente,comando,destinatario,testo[2:].split()[0],testo[testo.index(' ')+1:].strip())
      else:
        esegui (utente,comando,destinatario,testo[2:].split()[0],'')
  
def bacio (utente,comando,destinatario,parametri) : #esempio di comando #debug:da testare
  if comando=='PRIVMSG':
    ircprivmsg ( destinatario, utente+' manda un dolce bacio :* a '+parametri)

def deliranza (utente,comando,destinatario,parametri) : #esempio scemo di action #debug:da testare
  if parametri=='':
    ircprivmsg ( destinatario, 'balla meglio di johnny depp', 1)

def game (utente,comando,destinatario,parametri) : #semplice gioco, funzione di avvio #debug:da testare
  global attivo
  global r
  r=random.randint(0,10000)
  if not attivo and parametri == '' and comando == 'PRIVMSG':
    ircprivmsg ( destinatario, 'dite un numero da 0 a 10000 preceduto da +g')
    ircprivmsg ( destinatario, 'esempio: +g 10000')
    attivo=1

def gameon (utente,comando,destinatario,parametri) : #semplice gioco, funzione di gioco #debug:da testare
  global attivo
  if attivo!=1 :
    ircprivmsg ( destinatario, 'gioco non attivo')
  elif comando == 'PRIVMSG' :
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
  else:
    pass

def ping (utente,comando,destinatario,parametri) : #debug:da testare
  ircprivmsg ( destinatario, utente+': pong!')

funzioni={'messaggio':messaggio,\
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
