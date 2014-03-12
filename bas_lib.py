#base functions library

from leggidati import *
from irc_con import *

import time
import datetime

ambiente_attivo = ''
#le funzioni di ambiente assegnano il loro identificativo a ambiente_attivo
r=0
started=0
secondi=int(time.time())

def ircsend ( messaggio ): #azione base
  irc.send ( messaggio+'\r\n' )
  print datetime.datetime.fromtimestamp(time.time()).strftime('%H-%M-%S')+\
     ' <'+nomebot+'> '+messaggio.strip() #in questo modo si puo' stilizzare a piacere

def ircnick ( nick ): #debug:da testare
  ircsend ( 'NICK '+nick )

def ircprivmsg ( destinatario, messaggio, action=None ) :
  #destinatario puo' essere un chan se preceduto da un cancelletto
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
    ircsend ( 'PART '+chan+' :'+motivo )

def ircquit ( motivo=None ) :
  if motivo == None:
    ircsend ( 'QUIT :izabot by izabera' )
  else :
    ircsend ( 'QUIT :'+motivo )
  raise SystemExit

def ircnotice ( destinatario, messaggio ) :
  ircsend ( 'NOTICE '+destinatario+' :'+messaggio )
