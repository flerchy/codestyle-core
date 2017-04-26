import os
from PyQt4 import QtSql
import sys
import subprocess

def backup_uzytkownika(katalog_domowy):
    db = QtSql.QSqlDatabase('QSQLITE')
    db.setDatabaseName(katalog_domowy + '/.backup.conf')
    db.open()
    
    query = QtSql.QSqlTableModel(None, db)
    query.setTable("Katalogi")
    query.select()
    
    print "Uzytkownik ma %d katalogow" % query.rowCount()
    
    
    for i in range(query.rowCount()):
        nazwa = query.record(i).value('nazwa').toString()
        id_serwera = query.record(i).value('id_serwera').toInt()[0]
        
        query_serwera = QtSql.QSqlTableModel(db = db)
        query_serwera.setTable("Serwery")
        query_serwera.setFilter("id = %d" % id_serwera)
        query_serwera.select()
        
        adres = query_serwera.record(0).value('adres').toString()
        katalog_docelowy = query_serwera.record(0).value('katalog docelowy').toString()   
        klucz = query_serwera.record(0).value('klucz').toString() 
        
        print "Katalog %s wysylamy na serwer %s:%s" % (nazwa, adres, katalog_docelowy)
        print "rsync -ave \"ssh -i %s -o PasswordAuthentication=no\" %s %s:\"%s\"" % (klucz, nazwa, adres, katalog_docelowy)
        subprocess.call("rsync -ave \"ssh -i %s -o PasswordAuthentication=no\" %s %s:\"%s\"" % (klucz, nazwa, adres, katalog_docelowy), shell = True)
        
def wykonaj_backup():
    plik = open('/etc/passwd')
    linie = plik.readlines()
    for linia in linie:
        lista = linia.split(':')
        if int(lista[2]) >= 1000:
            sciezka = lista[5] + '/.backup.conf'
            if os.path.exists(sciezka):
                print "Uzytkownik %s ma skonfigurowane" % lista[0]
                backup_uzytkownika(lista[5])

wykonaj_backup()

