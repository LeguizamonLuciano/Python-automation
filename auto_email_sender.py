import smtplib
#Constantes START
miEmail = 'your@email.com'
receptor = ['target@email.com','target@email.com','target@email.com; target@email.com']
frase = 'podrias pedir el manual\u003F, la muestra no lo trajo\n\nMuchas gracias!'
#Constantes END
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login(miEmail, 'password')
while True :
    numeroSolicitud = input('Numero: ')
    if numeroSolicitud.isnumeric() == True:
        break
    if numeroSolicitud.isnumeric() == False:
        continue
while True :
    mañanaTarde = input('M o T:')
    if mañanaTarde == 'M':
        mañanaTarde = 'Buen dia '
        break
    if mañanaTarde == 'T':
        mañanaTarde = 'Buenas tardes '
        break
while True :
    ingresoReceptor = input('1)Target 2)Target 3)Target ')
    if ingresoReceptor.isnumeric() == True:
        if ingresoReceptor == 1:
            receptor = receptor[0]
        if ingresoReceptor == 2:
            receptor = receptor[1]
        if ingresoReceptor == 3:
            receptor = receptor[2]
    if numeroSolicitud.isnumeric() == False:
        continue
smtpObj.sendmail(miEmail,receptor,'Subject: S.E. '+numeroSolicitud+'\n'+mañanaTarde+frase)
smtpObj.quit()
