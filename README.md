izabot
======

un bot irc in python

utilizzo
-
- configurare il bot con i dati corretti in `botdata.txt`
- far partire `izabot.py`

per aggiungere e modificare funzioni anche con il bot attivo:
- modificare il file `cus_lib.py`
- dare il comando `+ricarica`

bug e limitazioni
-
al momento le funzioni definite dall'utente possono applicarsi solo agli eventi PRIVMSG

l'autenticazione non funziona ancora bene

testato con
-
Python 2.7.5

comandi
-
- **standard:** +messaggio +query +notice +join +part +quit
- **utili:** +calcola +wiki +dado +ping
- **giochi:** +game +eqgame +wikigame
il trigger `+` è configurabile in `botdata.txt`
