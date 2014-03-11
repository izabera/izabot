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
##aggiornamento da file possibile?                                            #
##prendere il chan in un altro modo                                           #
###############################################################################

import socket

###############################################################################
##dati del bot                                                                #
###############################################################################

from leggidati import *

###############################################################################
##autenticazione                                                              #
###############################################################################

from auth import *

###############################################################################
##funzioni di basso livello                                                   #
##interfaccia col protocollo                                                  #
###############################################################################

from bas_lib import *

###############################################################################
##macro                                                                       #
###############################################################################

from mac_lib import *

###############################################################################
##funzioni avanzate                                                           #
###############################################################################

from adv_lib import *

###############################################################################
##modulo di connessione                                                       #
###############################################################################

from irc_con import *

irc.connect ( ( rete, port ) )
irc.recv ( 4096 )
ircnick ( nomebot )
ircsend ( 'USER '+nomebot+' '+nomebot+' '+nomebot+' :bot creato da iza in python\r\n' )
while 1:
  data = irc.recv ( 4096 )
  analisi (data) 
#  if data.find ( '---------- END OF MESSAGE(S) OF THE DAY ----------' ) != -1: #per ogn
  avvio ( )
