from __future__ import division
from math import *
import urllib2
#custom functions library

from bas_lib import *
from mac_lib import *

import random

def ping (utente,destinatario,parametri) :
  ircprivmsg ( destinatario, utente+': pong!')

def game (utente,destinatario,parametri) :
  global ambiente_attivo
  global r
  if parametri == 'on' and ambiente_attivo == '':
    r=random.randint(0,10000)
    ircprivmsg ( destinatario, 'ho scelto un numero da 0 a 10000, indovinatelo')
    ambiente_attivo='game'
  elif parametri == 'off':
    ambiente_attivo = ''
  elif ambiente_attivo == 'game':
    try:
      if r==int(parametri) :
        ircprivmsg ( destinatario, 'congratulazioni '+utente+'! hai indovinato!')
        ambiente_attivo = ''
      elif r>int(parametri) :
        ircprivmsg ( destinatario, 'troppo piccolo!')
      elif r<int(parametri) :
        ircprivmsg ( destinatario, 'troppo grosso!')
    except:
      print 'problema'
    
def bacio (utente,destinatario,parametri) :
  ircprivmsg ( destinatario, utente+' manda un dolce bacio :* a '+parametri)

def deliranza (utente,destinatario,parametri) :
  if parametri=='':
    ircprivmsg ( destinatario, 'balla molto meglio di johnny depp', 1)

def calcola (utente,destinatario,parametri) :
  if parametri!='':
    try:
      output=eval(parametri)
      ircprivmsg(destinatario,parametri+'='+str(output))
    except:
      ircprivmsg(destinatario,'errore')

def dado (utente,destinatario,parametri) :
  if parametri=='':
    ircprivmsg(destinatario,str(random.randint(1,6)))
  else:
    try:
      parametri = int (parametri)
      ircprivmsg(destinatario,str(random.randint(0,parametri)))
    except:
      pass

def wiki (utente,destinatario,parametri) :
  if parametri!='':
    try:
      indirizzo='https://it.wikipedia.org/w/api.php?action=query&prop=extracts&exsentences=2&explaintext&format=xml&titles='
      parametri=parametri.replace(' ','%20')
      invio=urllib2.urlopen(indirizzo+parametri).read()
      if invio.find('" missing="" />')!=-1:
        ircprivmsg(destinatario,'pagina non trovata')
      else:
        invio=invio[invio.find('ve">')+4:]
        invio=invio.replace('</extract></page></pages></query></api>','')
        invio=invio.replace('&quot;','"')
        invio=invio.replace('\n',' ')
        taglia = tagliaold = 0
        while taglia != -1:
          if taglia != tagliaold:
            ircprivmsg(destinatario,invio[tagliaold:taglia].strip())
          tagliaold=taglia
          taglia = invio.find(' ',100+tagliaold)
        if len(invio[tagliaold:].strip())!=0:
          ircprivmsg(destinatario,invio[tagliaold:].strip())
    except Exception as exception:
      ircprivmsg(destinatario,exception.__class__.__name__)

def game2 (utente,destinatario,parametri) :
  global ambiente_attivo
  global r
  a=['+','-','*','//']
  if parametri == 'on' and ambiente_attivo == '':
    ircprivmsg ( destinatario, 'io dico un\'espressione e voi dite il risultato')
    ircprivmsg ( destinatario, 'le divisioni sono divisioni intere')
    ircprivmsg ( destinatario, 'esempio: 5+3*2+3/5')
    ircprivmsg ( destinatario, 'risposta: 11')
    ircprivmsg ( destinatario, ' ')
    while 1:
      r=str(random.randint(0,10))
      for i in range (5):
          r+=a[random.randint(0,3)]
          r+=str(random.randint(0,10))
      try:
          eval(r)
          break
      except:
          pass
    ircprivmsg ( destinatario, 'espressione: ----------->  '+r.replace('//','/') )
    ambiente_attivo = 'game2'
  elif parametri == 'off':
    ambiente_attivo = ''
  elif ambiente_attivo == 'game2':
    try:
      if eval(r)==int(parametri) :
        ircprivmsg ( destinatario, 'congratulazioni '+utente+'! hai indovinato!')
        ambiente_attivo = ''
    except:
      pass

#'comando':nome_funzione
#attenzione a non creare conflitti
#comandi e nomi funzionio riservati:
#'messaggio':messaggio
#'query':query
#'join':join
#'part':part
#'quit':cuit
#'notice':notice
#'ricarica':ricarica
cus_funct={'delira':deliranza,\
           'bacio':bacio,\
           'game':game,
           'ping':ping,\
           'calcola':calcola,\
           'game2':game2,\
           'wiki':wiki,\
           'dado':dado}
