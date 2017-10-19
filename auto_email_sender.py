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
    try:
        numeroSolicitud = int(input('Numero: '))
    except ValueError:
        print('Reingrese un numero')
        continue
    if isinstance(numeroSolicitud, int):
        break
while True :
    mañanaTarde = input('M o T:')
    if mañanaTarde == 'M' or mañanaTarde == 'm':
       mañanaTarde = 'Buen dia '
       break
    if mañanaTarde == 'T' or mañanaTarde == 't':
       mañanaTarde = 'Buenas tardes '
       break
    if mañanaTarde != 'T' or 't' or 'M' or 'm':
       print('Reingrese T, t, M o m')
       continue
while True :
    try:
        ingresoReceptor = int(input('1)target1 2)target2 3)target3 '))
    except ValueError:
        print('Reingrese un numero')
        continue
    if ingresoReceptor == 1:
            receptor = receptor[0]
            break
    if ingresoReceptor == 2:
            receptor = receptor[1]
            break
    if ingresoReceptor == 3:
            receptor = receptor[2]
            break
    if ingresoReceptor == 4:        #Para testeo
            receptor = receptor[3]  #Para testeo
            break                   #Para testeo
    if ingresoReceptor > 4 or ingresoReceptor < 1: #Para testeo "ingresoReceptor > 4"
            print('Reingrese un numero que corresponda con el destinatario deseado')
            continue
smtpObj.sendmail(miEmail,receptor,'Subject: S.E. '+str(numeroSolicitud)+'\n'+mañanaTarde+frase)
smtpObj.quit()
