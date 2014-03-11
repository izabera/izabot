from bas_lib import *

nickserv = 0
authserv = 1
altro = 0

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
