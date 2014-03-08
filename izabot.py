###############################################################################
###############################################################################
##izabot 0.4.0                                                                #
###############################################################################
###############################################################################
##creato da: izabera                                                          #
##licenza: MIT License                                                        #
##                                                                            #
##se questo sorgente vi e' stato utile, sarei felice se me lo faceste sapere  #
##con una mail a izaberina at gmail dot com                                   #
##                                                                            #
##vietato rimuovere questo riquadro                                           #
###############################################################################
##TODO:                                                                       #
##sistemare lo stile, le split tagliano via roba                              #
##comandi di avvio                                                            #
##                                                                            #
###############################################################################

import socket
import random

r = attivo = started = 0

###############################################################################
##dati del bot                                                                #
###############################################################################

owner = 'izabera'
nomebot = 'izabot'
password = 'xxxx'
rete = 'irc.freenode.net'
port = 6667
comandi = ['PRIVMSG','NOTICE','JOIN','INVITE','PART','QUIT','KICK']
comandibot = ['join','part','quit','messaggio','query','notice','game','g','bacio','ping','delira',]
trigger = '+'

###############################################################################
##autenticazione                                                              #
###############################################################################

nickserv = 1
authserv = 0
altro = 0

###############################################################################
##funzioni di basso livello                                                   #
##interfaccia col protocollo                                                  #
###############################################################################

def ircsend ( messaggio ): #azione base
  irc.send ( messaggio+'\r\n' )
  print '<'+nomebot+'> '+messaggio #in questo modo si puo' stilizzare a piacere

def ircnick ( nick ):
  ircsend ( 'NICK '+nick )

def ircprivmsg ( destinatario, messaggio, action=None ) :
  #persona puo' essere un chan se preceduto da un cancelletto
  if action == None:
    ircsend ( 'PRIVMSG '+destinatario+' :'+messaggio )
  else :
    ircsend ( 'PRIVMSG '+destinatario+' :\001ACTION '+messaggio )

def ircjoin ( chan ) : #il chan deve avere un asterisco davanti
  ircsend ( 'JOIN '+chan)

def ircpart ( chan, motivo=None ) :
  if motivo == None:
    ircsend ( 'PART '+chan )
  else :
    ircsend ( 'PART '+chan+': '+motivo )

def ircquit ( motivo=None ) :
  if motivo == None:
    ircsend ( 'QUIT' )
  else :
    ircsend ( 'QUIT '+motivo )

def ircnotice ( destinatario, messaggio ) :
  ircsend ( 'NOTICE '+destinatario+' :'+messaggio )

###############################################################################
##macro                                                                       #
###############################################################################

def avvio ( ) :
  global started;
  if started == 0:
    ircprivmsg ( owner, 'sono connesso' )
    ircjoin ( '#'+nomebot )
    if nickserv:
      ircprivmsg ( 'NickServ', 'identify '+password )
    if authserv:
      ircprivmsg ( 'AuthServ', 'auth '+nomebot+' '+password )
    if altro:
      ircsend ( 'JOIN #vhost')
    started = 1

def autojoin ( ) :  #join se invitato
  channel=data.split('INVITE ')[1].split( )[1]
  ircjoin ( channel )
  ircprivmsg ( channel, 'ciao a tutti')

def messaggio ( ) :
  channel=data.split('PRIVMSG ')[-1].split(' :')[0]
  if len(data.split(' :+messaggio '))>=2:
    messaggio=data.split(' :+messaggio ')[1]
    ircprivmsg ( channel, messaggio )

def query ( ) :
  ricevitore=data.split(' :+query ')[1].split( )[0]
  if len(data.split(' :+query '))>=2:
    messaggio=data.split(' :+query ')[1].split(ricevitore+' ')[1]
    ircprivmsg ( ricevitore, messaggio )

def notice ( ) :
  ricevitore=data.split(' :+notice ')[1].split( )[0]
  if len(data.split(' :+notice '))>=2:
    messaggio=data.split(' :+notice ')[1].split(ricevitore+' ')[1]
    ircnotice ( ricevitore, messaggio )

def join ( ) :
  if len(data.split(' :+join '))==2:
    canale=data.split(' :+join ')[1].split( )[0]
    ircjoin ( canale )

def part ( ) :
  channel=data.split('PRIVMSG ')[-1].split(' :')[0]
  nick=data.split('!')[0][1:]
  if (nick == owner):
    ircpart ( channel )

def _quit ( ) :
  nick=data.split('!')[0][1:]
  try:
    motivo=data.split(' :+quit ')[1]
  except:
    motivo=None
  if (nick == owner):
    if motivo!=None:
      ircquit( motivo )
    else:
      ircquit( )

###############################################################################
##funzioni avanzate                                                           #
###############################################################################

def esegui (comando,parametri=None):
  if parametri==None:
    print 'comando: '+comando
  else:
    print 'comando: '+comando+', parametri: '+parametri

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
    if comando=='PRIVMSG': #il bot non gestisce altri eventi per ora
      if testo[0:2]==':'+trigger and testo[2:].split()[0] in comandibot:
        if testo.find(' ')!=-1:
          esegui (testo[2:].split()[0],testo[testo.index(' ')+1:].strip())
        else:
          esegui (testo[2:].split()[0])
    stampa = '<'+utente+'> '+comando+' '+destinatario+' '+testo #finale
#    stampa = '<'+utente+'> _utente_ '+comando+' _comando_ '+destinatario+' _destinatario_ '+testo+' _testo_' #debug
    print stampa
  
def bacio ( ) : #esempio di comando
  channel=data.split('PRIVMSG ')[-1].split(' :')[0]
  nick=data.split('!')[0][1:]
  if len(data.split(' :+bacio '))==2:
    ricevitore=data.split(' :+bacio ')[1].split( )[0]
    ircprivmsg ( channel, nick+' manda un dolce bacio :* a '+ricevitore)

def deliranza ( ) : #esempio scemo di action
  channel=data.split('PRIVMSG ')[-1].split(' :')[0]
  ircprivmsg ( channel, 'balla meglio di johnny depp', 1)

def game ( ) : #semplice gioco, funzione di avvio
  global attivo
  global r
  r=random.randint(0,10000)
  if not attivo:
    channel=data.split('PRIVMSG ')[-1].split(' :')[0]
    ircprivmsg ( channel, 'dite un numero da 0 a 10000 preceduto da +g')
    ircprivmsg ( channel, 'esempio: +g 10000')
    attivo=1

def gameon ( ) : #semplice gioco, funzione di gioco
  global attivo
  if attivo!=1 :
    channel=data.split('PRIVMSG ')[-1].split(' :')[0]
    ircprivmsg ( channel, 'gioco non attivo')
  else :
    channel=data.split('PRIVMSG ')[-1].split(' :')[0]
    nick=data.split('!')[0][1:]
    numero=data.split(' :+g ')[1].split( )[0]
    try:
      numero = int(numero)

      if r==numero :
        ircprivmsg ( channel, 'congratulazioni '+nick+'! hai indovinato!')
        attivo = 0
      elif r<numero :
        ircprivmsg ( channel, 'troppo grande!')
      else :
        ircprivmsg ( channel, 'troppo piccolo!')
    except ValueError:
      print 'errore'

def ping ( ) :
  channel=data.split('PRIVMSG ')[-1].split(' :')[0]
  nick=data.split('!')[0][1:]
  ircprivmsg ( channel, nick+': pong!')

###############################################################################
##modulo di connessione                                                       #
###############################################################################

irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( rete, port ) )
irc.recv ( 4096 )
ircnick ( nomebot )
ircsend ( 'USER '+nomebot+' '+nomebot+' '+nomebot+' :bot creato da iza in python\r\n' )
while 1:
  data = irc.recv ( 4096 )
  analisi (data) 
  if data.find ( 'PING' ) != -1:
    ircsend ( 'PONG ' + data.split( ) [ 1 ] + '\r\n' )
#  if data.find ( '---------- END OF MESSAGE(S) OF THE DAY ----------' ) != -1:
    avvio ( )
  if data.find('INVITE')!=-1:
    autojoin ( )
  if data.find(' :+bacio ')!=-1:
    bacio ( )
  if data.find(' :+messaggio ')!=-1:
    messaggio ( )
  if data.find(' :+query ')!=-1:
    query ( )
  if data.find(' :+notice ')!=-1:
    notice ( )
  if data.find(' :+join ')!=-1:
    join ( )
  if data.find(' :+part')!=-1:
    part ( )
  if data.find(' :+ping')!=-1:
    ping ( )
  if data.find(' :+game')!=-1:
    game ( )
  if data.find(' :+delira')!=-1:
    deliranza ( )
  if data.find(' :+g ')!=-1:
    gameon ( )
  if data.find(' :+quit')!=-1:
    _quit ( )
    break
