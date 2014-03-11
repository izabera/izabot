#macro library

from bas_lib import *

def autojoin ( ) :  #join se invitato #debug:cambiare e mettere in gestione eventi
  channel=data.split('INVITE ')[1].split( )[1]
  ircjoin ( channel )
  ircprivmsg ( channel, 'ciao a tutti')

def messaggio (utente,destinatario,parametri) :
  ircprivmsg ( destinatario, parametri )

def query (utente,destinatario,parametri) :
  try:
    parametri=parametri.strip( )
    temp=parametri.split( )
    mess=''
    if len(temp)>1:
      mess=parametri[len(temp[0])+1:]
    ircprivmsg ( temp[0], mess )
  except:
    pass

def notice (utente,destinatario,parametri) :
  try:
    parametri=parametri.strip( )
    temp=parametri.split( )
    mess=''
    if len(temp)>1:
      mess=parametri[len(temp[0])+1:]
    ircnotice ( temp[0], mess )
  except:
    pass

def join (utente,destinatario,parametri) :
  ircjoin ( parametri )

def part (utente,destinatario,parametri) :
  if utente == owner:
    if parametri=='':
      ircpart ( destinatario )
    else:
      ircpart ( destinatario, parametri )

def cuit (utente,destinatario,parametri) :
#per qualche motivo la funzione deve avere un nome diverso da quit
  if utente == owner:
    if parametri!='':
      ircquit( parametri )
    else:
      ircquit( )

def e_ping ( parametri ):
  ircsend ( 'PONG ' + parametri )
  
def e_join ( utente, destinatario ):
  ircprivmsg (destinatario, 'ciao '+utente)