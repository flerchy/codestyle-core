# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore, QtSql
import ui_uzytkownik
import sys
import os
import subprocess

class Uzytkownik(QtGui.QMainWindow):
    def __init__(self):
        super (Uzytkownik,self).__init__()
        self.ui = ui_uzytkownik.Ui_MainWindow()
        self.ui.setupUi(self)
       
        self.ui.wybierz_katalog.clicked.connect(self.wybierz_katalog)
        self.ui.wybierz_klucz.clicked.connect(self.wybierz_klucz)
        self.ui.dodaj_katalog.clicked.connect(self.dodaj_katalog)
        self.ui.dodaj_serwer.clicked.connect(self.dodaj_serwer)
        self.ui.usun_serwer.clicked.connect(self.usun_serwer)
        self.ui.usun_katalog.clicked.connect(self.usun_katalog)
        
        self.aktualizuj_serwery()
        self.aktualizuj_katalogi()
        
    def wybierz_katalog(self):
        dirname = QtGui.QFileDialog.getExistingDirectory(self, 'Wybierz katalog do backupu', '/home')
        self.ui.nazwa_katalogu.setText(dirname)
      
    def wybierz_klucz(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Wybierz plik klucza', '~')
        self.ui.sciezka_klucza.setText(filename)
       
    def dodaj_katalog(self):
        polaczenie = QtSql.QSqlDatabase('QSQLITE')
        polaczenie.setDatabaseName('/home/marta/.backup.conf')
        polaczenie.open()

        query = QtSql.QSqlTableModel(db = polaczenie)
        query.setTable("Katalogi")

        katalog = self.ui.nazwa_katalogu.text()
        id_serwera = self.ui.id_serwera.itemData(self.ui.id_serwera.currentIndex())

        query.insertRow(0)

        if os.path.isdir(katalog):
            query.setData(query.index(0, 0), katalog)
            query.setData(query.index(0, 1), id_serwera)
            query.submitAll()
        else:
            wiadomosc = QtGui.QMessageBox()
            wiadomosc.setText("Katalog nie istnieje")
            wiadomosc.exec_()

        self.aktualizuj_serwery()
        return
         
         
    def dodaj_serwer(self):
        polaczenie = QtSql.QSqlDatabase('QSQLITE')
        polaczenie.setDatabaseName('/home/marta/.backup.conf')
        polaczenie.open()

        query = QtSql.QSqlTableModel(db = polaczenie)
        query.setTable("Serwery")
        
        nazwa = self.ui.nazwa_serwera.text()
        katalog = self.ui.katalog_docelowy.text()
        klucz = self.ui.sciezka_klucza.text()
        
        query.insertRow(0)
        query.setData(query.index(0, 0), None)
        query.setData(query.index(0, 1), nazwa)
        query.setData(query.index(0, 2), katalog)
        query.setData(query.index(0, 3), klucz)
        query.submitAll()
        
        self.aktualizuj_serwery()
        return
    
    def aktualizuj_serwery(self):
        polaczenie = QtSql.QSqlDatabase('QSQLITE')
        polaczenie.setDatabaseName('/home/marta/.backup.conf')
        polaczenie.open()
        
        serwery = QtSql.QSqlTableModel(db = polaczenie)
        serwery.setTable('Serwery')
        serwery.select()
        
        self.ui.serwery.setModel(serwery)
        #self.ui.serwery.setColumnHidden(0, True)
        
        self.ui.id_serwera.clear()
        for i in range(serwery.rowCount()):
            wpis = '%s:%s' % (serwery.record(i).value('adres').toString(), serwery.record(i).value('katalog_docelowy').toString())
            # Zostawiamy jako qvariant, bo addItem przyjmuje qvariant
            id_serwera = serwery.record(i).value('id')
            self.ui.id_serwera.addItem(wpis, id_serwera)
        
    def aktualizuj_katalogi(self):
        print "Aktualizuje katalogi"
        polaczenie = QtSql.QSqlDatabase('QSQLITE')
        polaczenie.setDatabaseName('/home/marta/.backup.conf')
        polaczenie.open()
        
        katalogi = QtSql.QSqlTableModel(db = polaczenie)
        katalogi.setTable('Katalogi')
        katalogi.select()
        
        self.ui.katalogi.setModel(katalogi)
        self.ui.katalogi.setColumnHidden(1, True)
     
    def usun_serwer(self):
        polaczenie = QtSql.QSqlDatabase('QSQLITE')
        polaczenie.setDatabaseName('/home/marta/.backup.conf')
        polaczenie.open()

        query = QtSql.QSqlTableModel(db = polaczenie)
        query.setTable("Serwery")
        query.select()
        
        # Patrze jakie jest zaznaczenie
        wybrany = self.ui.serwery.selectedIndexes()
        
        if len(wybrany) > 0:
            wiersz = wybrany[0].row()
            query.removeRow(wiersz)
        self.aktualizuj_serwery()
     
    def usun_katalog(self):
        pass
           
def main():
	app = QtGui.QApplication(sys.argv)
	z = Uzytkownik()
	z.show()
	sys.exit(app.exec_())

main()
