#macro library

from bas_lib import *

def autojoin ( ) :  #join se invitato #debug:cambiare e mettere in gestione eventi
  channel=data.split('INVITE ')[1].split( )[1]
  ircjoin ( channel )
  ircprivmsg ( channel, 'ciao a tutti')

def messaggio (utente,comando,destinatario,parametri) :
  try:
    parametri=parametri.strip( )
    temp=parametri.split( )
    mess=''
    if len(temp)>1:
      mess=parametri[len(temp[0])+1:]
    ircprivmsg ( temp[0], mess )
  except:
    pass

def query (utente,comando,destinatario,parametri) :
  messaggio(utente,comando,destinatario,parametri)

def notice (utente,comando,destinatario,parametri) :
  ircnotice ( destinatario, parametri )

def join (utente,comando,destinatario,parametri) :
  ircjoin ( parametri )

def part (utente,comando,destinatario,parametri) :
  if utente == owner:
    if parametri=='':
      ircpart ( destinatario )
    else:
      ircpart ( destinatario, parametri )

def cuit (utente,comando,destinatario,parametri) :
#per qualche motivo la funzione deve avere un nome diverso da quit
  if utente == owner:
    if parametri!='':
      ircquit( parametri )
    else:
      ircquit( )
