# Legge i dati del bot da un file.
dati = open("botdata.txt","r")
riga = ''
owner = nomebot = password = rete = port = comandibot = trigger = ""
while riga != '#endend':
  riga = dati.readline()
  if riga[0:len(riga)-1]=='#owner':
    riga = dati.readline()
    owner = riga[0:len(riga)-1]
  if riga[0:len(riga)-1]=='#nomebot':
    riga = dati.readline()
    nomebot = riga[0:len(riga)-1]
  if riga[0:len(riga)-1]=='#password':
    riga = dati.readline()
    password = riga[0:len(riga)-1]
  if riga[0:len(riga)-1]=='#rete':
    riga = dati.readline()
    rete = riga[0:len(riga)-1]
  if riga[0:len(riga)-1]=='#port':
    riga = dati.readline()
    port = int(riga[0:len(riga)-1])
  if riga[0:len(riga)-1]=='#comandibot':
    riga = dati.readline()
    while riga[0:len(riga)-1]!='#end':
      comandibot += riga[0:len(riga)-1]+' '
      riga = dati.readline()
  if riga[0:len(riga)-1]=='#trigger':
    riga = dati.readline()
    trigger = riga[0:len(riga)-1]
dati.close()
comandibot=comandibot.split()
