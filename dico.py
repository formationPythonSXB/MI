contacts = {'Sebastian': {'email': 'Donec.felis.orci@consectetueripsumnunc.edu', 'born': 1979},
 'Barclay':   {'email': 'aliquet.metus.urna@neceleifend.co.uk', 'born': 2000},
 'Vivien':    {'email': 'pharetra@a.com', 'born': 1955},
 'Britanney': {'email': 'eu.tellus.Phasellus@arcuvelquam.ca', 'born': 1961},
 'Reese':     {'email': 'tortor.dictum.eu@egestasSed.ca', 'born': 1951},
 'Keegan':    {'email': 'libero.nec@cursuset.co.uk', 'born': 1998},
 'Ezekiel':   {'email': 'tempus.mauris.erat@aclibero.org', 'born': 1951},
 'Odessa':    {'email': 'massa.Quisque.porttitor@felis.net', 'born': 1925},
 'Elijah':    {'email': 'luctus.vulputate.nisi@nunc.com', 'born': 1963},
 'Hilel':     {'email': 'lectus.pede.et@aliquetsem.ca', 'born': 1982},
 'Callie':    {'email': 'et.euismod.et@aliquetmagnaa.net', 'born': 1984},
 'India':     {'email': 'Duis.sit.amet@Phaselluslibero.com', 'born': 1938},
 'Lane':      {'email': 'amet@turpis.ca', 'born': 1922},
 'Alexis':    {'email': 'sagittis.placerat@nibhdolor.net', 'born': 1927},
 'Micah':     {'email': 'lorem.eget.mollis@SeddictumProin.com', 'born': 1914},
 'Rigel':     {'email': 'sollicitudin@eratinconsectetuer.org', 'born': 1941},
 'Avram':     {'email': 'tincidunt.vehicula@vulputate.org', 'born': 1919},
 'Dieter':    {'email': 'ornare.lectus.justo@Integeridmagna.org', 'born': 1937},
 'Sarah':     {'email': 'cubilia.Curae.Phasellus@non.net', 'born': 1946},
 'Graham':    {'email': 'elit.Curabitur.sed@maurisIntegersem.edu', 'born': 1931},
 'Daquan':    {'email': 'fermentum.convallis.ligula@porttitorinterdum.co.uk', 'born': 1934},
 'Nell':      {'email': 'purus@lectusconvallisest.org', 'born': 1997},
 'Ocean':     {'email': 'ut@Nuncquisarcu.net', 'born': 2006},
 'Cruz':      {'email': 'Aenean.euismod.mauris@idmollisnec.edu', 'born': 1950},
 'Hyacinth':  {'email': 'amet@Nunc.edu', 'born': 1929}
}

for contact in contacts :
    mailSplit = contacts[contact]['email'].split('.')
    if mailSplit[len(mailSplit)-1] == "edu" : print (contact , " est né(e) en " , contacts[contact]['born'])