###############################################################################
###############################################################################
##izabot 0.5.0                                                                #
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
##funzioni da correggere                                                      #
##lettura da file                                                             #
##aggiornamento da file possibile?                                            #
##prendere il chan in un altro modo                                           #
##perche' stampa doppio?                                                      #
###############################################################################

import socket
import random

r = attivo = started = 0

###############################################################################
##dati del bot                                                                #
###############################################################################

import leggidati
owner = leggidati.owner
nomebot = leggidati.nomebot
password = leggidati.password
rete = leggidati.rete
port = leggidati.port
comandi = leggidati.comandi
comandibot = leggidati.comandibot
trigger = leggidati.trigger

###############################################################################
##autenticazione                                                              #
###############################################################################

nickserv = 0
authserv = 1
altro = 0

###############################################################################
##funzioni di basso livello                                                   #
##interfaccia col protocollo                                                  #
###############################################################################

def ircsend ( messaggio ): #azione base #debug:perfetta
  irc.send ( messaggio+'\r\n' )
  print '<'+nomebot+'> '+messaggio.strip() #in questo modo si puo' stilizzare a piacere

def ircnick ( nick ): #debug:da testare
  ircsend ( 'NICK '+nick )

def ircprivmsg ( destinatario, messaggio, action=None ) : #debug:perfetta
  #destinatario puo' essere un chan se preceduto da un cancelletto
  if action == None:
    ircsend ( 'PRIVMSG '+destinatario+' :'+messaggio )
  else :
    ircsend ( 'PRIVMSG '+destinatario+' :\001ACTION '+messaggio )

def ircjoin ( chan ) : #il chan deve avere un asterisco davanti #debug:perfetta
  ircsend ( 'JOIN '+chan)

def ircpart ( chan, motivo=None ) : #debug:funziona senza arg, da testare con
  if motivo == None:
    ircsend ( 'PART '+chan )
  else :
    ircsend ( 'PART '+chan+' '+motivo )

def ircquit ( motivo=None ) : #debug:perfetta
  if motivo == None:
    ircsend ( 'QUIT :izabot by izabera' )
  else :
    ircsend ( 'QUIT :'+motivo )
  raise SystemExit

def ircnotice ( destinatario, messaggio ) : #debug:perfetta
  ircsend ( 'NOTICE '+destinatario+' :'+messaggio )

###############################################################################
##macro                                                                       #
###############################################################################

def avvio ( ) : #debug:perfetta
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

def autojoin ( ) :  #join se invitato #debug:cambiare e mettere in gestione eventi
  channel=data.split('INVITE ')[1].split( )[1]
  ircjoin ( channel )
  ircprivmsg ( channel, 'ciao a tutti')

def messaggio ( raw_arg=None ) :#debug:perfetta
  if raw_arg!=None:
    channel=raw_arg.split()[0]
    try:
      messaggio=raw_arg.split()[1:]
      messaggio=' '.join(messaggio)
    except:
      messaggio=''
    ircprivmsg ( channel, messaggio )

def query ( raw_arg=None ) :#debug:perfetta
  if raw_arg!=None:
    ricevitore=raw_arg.split()[0]
    try:
      messaggio=raw_arg.split()[1:]
      messaggio=' '.join(messaggio)
    except:
      messaggio=''
    ircprivmsg ( ricevitore, messaggio )

def notice ( raw_arg=None ) :#debug:perfetta
  if raw_arg!=None:
    ricevitore=raw_arg.split()[0]
    try:
      messaggio=raw_arg.split()[1:]
      messaggio=' '.join(messaggio)
    except:
      messaggio=''
    ircnotice ( ricevitore, messaggio )

def join ( raw_arg=None ) :#debug:perfetta
  if raw_arg!=None:
    ircjoin ( raw_arg )

def part ( raw_arg=None ) :#debug:funziona senza argomento, testare con
  channel=data.split('PRIVMSG ')[-1].split(' :')[0]
  nick=data.split('!')[0][1:]
  if (nick == owner):
    if raw_arg==None:
      ircpart ( channel )
    else:
      ircpart ( channel, raw_arg )

def _quit ( raw_arg=None ) :#debug:perfetta
  nick=data.split('!')[0][1:]
  motivo=raw_arg
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
    print 'comando: '+comando #debug
    funzioni[comando]()
  else:
    print 'comando: '+comando+', parametri: '+parametri #debug
    funzioni[comando](parametri)

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
    if comando=='PRIVMSG': #il bot non gestisce altri eventi per ora #debug:aggiungere gestione eventi
      if testo[0:2]==':'+trigger and testo[2:].split()[0] in comandibot:
        if testo.find(' ')!=-1:
          esegui (testo[2:].split()[0],testo[testo.index(' ')+1:].strip())
        else:
          esegui (testo[2:].split()[0])
    stampa = '<'+utente+'> '+comando+' '+destinatario+' '+testo #finale
#    stampa = '<'+utente+'> _utente_ '+comando+' _comando_ '+destinatario+' _destinatario_ '+testo+' _testo_' #debug
    print stampa
  
def bacio ( raw_arg ) : #esempio di comando #debug:da testare
  channel=data.split('PRIVMSG ')[-1].split(' :')[0]
  nick=data.split('!')[0][1:]
  if len(data.split(' :+bacio '))==2:
    ricevitore=data.split(' :+bacio ')[1].split( )[0]
    ircprivmsg ( channel, nick+' manda un dolce bacio :* a '+ricevitore)

def deliranza ( ) : #esempio scemo di action #debug:da testare
  channel=data.split('PRIVMSG ')[-1].split(' :')[0]
  ircprivmsg ( channel, 'balla meglio di johnny depp', 1)

def game ( ) : #semplice gioco, funzione di avvio #debug:da testare
  global attivo
  global r
  r=random.randint(0,10000)
  if not attivo:
    channel=data.split('PRIVMSG ')[-1].split(' :')[0]
    ircprivmsg ( channel, 'dite un numero da 0 a 10000 preceduto da +g')
    ircprivmsg ( channel, 'esempio: +g 10000')
    attivo=1

def gameon ( ) : #semplice gioco, funzione di gioco #debug:da testare
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

def ping ( ) : #debug:da testare
  channel=data.split('PRIVMSG ')[-1].split(' :')[0]
  nick=data.split('!')[0][1:]
  ircprivmsg ( channel, nick+': pong!')

funzioni={'messaggio':messaggio,'query':query,'join':join,'part':part,'quit':_quit,'notice':notice,'delira':deliranza,'game':game,'bacio':bacio,'gameon':gameon,'ping':ping}

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
  if data.find ( '---------- END OF MESSAGE(S) OF THE DAY ----------' ) != -1: #per ogn
    avvio ( )
#  if data.find('INVITE')!=-1:
#    autojoin ( )
#  if data.find(' :+bacio ')!=-1:
#    bacio ( )
#  if data.find(' :+messaggio ')!=-1:
#    messaggio ( )
#  if data.find(' :+query ')!=-1:
#    query ( )
#  if data.find(' :+notice ')!=-1:
#    notice ( )
#  if data.find(' :+join ')!=-1:
#    join ( )
#  if data.find(' :+part')!=-1:
#    part ( )
#  if data.find(' :+ping')!=-1:
#    ping ( )
#  if data.find(' :+game')!=-1:
#    game ( )
#  if data.find(' :+delira')!=-1:
#    deliranza ( )
#  if data.find(' :+g ')!=-1:
#    gameon ( )
#  if data.find(' :+quit')!=-1:
#    _quit ( )
#    break
