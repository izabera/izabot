from __future__ import division
from math import *
import urllib2
import xml.dom.minidom as xml
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

def eqgame (utente,destinatario,parametri) :
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
    ambiente_attivo = 'eqgame'
  elif parametri == 'off':
    ambiente_attivo = ''
  elif ambiente_attivo == 'eqgame':
    try:
      if eval(r)==int(parametri) :
        ircprivmsg ( destinatario, 'congratulazioni '+utente+'! hai indovinato!')
        ambiente_attivo = ''
    except:
      pass

def asterisco (testo):
  aster=''
  for i in range(len(testo)):
    if testo[i]!=' ':
      aster+='*'
    else :
      aster+=' '
  return aster

def nascondi (stringa, testo): #nascondi('Ciao Barba blu Gatto','barba Blu')='Ciao ***** *** Gatto
  aster=asterisco(testo)
  stringalow=stringa.lower().replace(testo.lower(),aster)
  finale = ''
  for i in range(len(stringa)):
    if stringa[i].lower() == stringalow[i].lower():
      finale+=stringa[i]
    else:
      finale+=stringalow[i]
  return finale

temp=0
def wikigame (utente,destinatario,parametri) :
  global ambiente_attivo
  global r
  global temp
  if parametri == 'on' and ambiente_attivo == '':
    ircprivmsg(destinatario,'\0038,4indovinate di che pagina di wikipedia si tratta')
    r=wikibackend('random','','action=query&list=random&rnnamespace=0&format=xml')#schifezza
    stampa=wikibackend('testo',r)
    stampa=nascondi(stampa,r)
    formatta(destinatario, stampa)
    ambiente_attivo = 'wikigame'
    temp=0
  elif parametri == 'hint' and ambiente_attivo == 'wikigame':
    temp+=3
    ircprivmsg(destinatario,'\0038,4indizio: '+r[0:temp]+asterisco(r[temp:]))
  elif parametri == 'off':
    ambiente_attivo = ''
  elif ambiente_attivo == 'wikigame':
    try:
      if r.strip().lower()==parametri.strip().lower() : #probabilmente non serve strippare
        ircprivmsg ( destinatario, 'congratulazioni '+utente+'! hai indovinato!')
        ambiente_attivo = ''
    except:
      pass

def bacio (utente,destinatario,parametri) :
  ircprivmsg ( destinatario, utente+' manda un dolce bacio :* a '+parametri)

def deliranza (utente,destinatario,parametri) :
  if parametri=='':
    ircprivmsg ( destinatario, 'balla molto meglio di johnny depp', 1)

def calcola (utente,destinatario,parametri) :
  if parametri!='':
    try:
      output=eval(parametri)
      if output == int(output):
        output= int(output)
      ircprivmsg(destinatario,parametri+'='+str(output))
    except:
      ircnotice(destinatario,'errore')

def dado (utente,destinatario,parametri) :
  if parametri=='':
    ircprivmsg(destinatario,str(random.randint(1,6)))
  else:
    try:
      parametri = int (parametri)
      ircprivmsg(destinatario,str(random.randint(0,parametri)))
    except:
      pass

def formatta (destinatario,invio):
    taglia = tagliaold = 0
    while taglia != -1:
      if taglia != tagliaold:
        ircprivmsg(destinatario,invio[tagliaold:taglia].strip())
      tagliaold=taglia
      taglia = invio.find(' ',100+tagliaold)
    if len(invio[tagliaold:].strip())!=0:
      ircprivmsg(destinatario,invio[tagliaold:].strip())

def wiki (utente,destinatario,parametri) :
  if parametri!='':
    invio=wikibackend('testo',parametri)
    formatta(destinatario,invio)

def wikibackend (tipo,parametri,indirizzo='action=query&prop=extracts&exsentences=2&explaintext&format=xml&titles='): #tipo e' 'random' o 'testo'
  try:
    indirizzo='https://it.wikipedia.org/w/api.php?'+indirizzo
    parametri=parametri.replace(' ','%20')
    invio=urllib2.urlopen(indirizzo+parametri).read()
    if invio.find('" missing="" />')!=-1:
      return 'pagina non trovata'
    else:
      invio=invio.replace('&quot;','"')
      invio=invio.replace('\n',' ')
      risu=xml.parseString(invio)
      if tipo == 'random':
        return risu.getElementsByTagName('page')[0].attributes['title'].value.encode('utf-8').strip()
      else :
        return risu.getElementsByTagName('extract')[0].firstChild.nodeValue.encode('utf-8').strip()
  except Exception as exception:
    return exception.__class__.__name__

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
           'eqgame':eqgame,\
           'wiki':wiki,\
           'dado':dado,
           'wikigame':wikigame}
