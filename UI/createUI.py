#!/usr/bin/env/python3

import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import pyrebase



class UIClass(QDialog):
    global firebase
    global user
    global db
    def __init__(self):
        super(UIClass, self).__init__()
        loadUi('event-handler.ui', self)
        self.settings = {
            'Title': 'Event Box',
            'Event': ['Fire', 'Tsunami', 'Shooting'],
            'Location': ['Luchetti', 'Stefani'],
            'SendTo': ['All', 'None']
        }
        self.initUI(self.settings)
        self.init_DB()

    def initUI(self, settings):
        if settings['Title'] and settings['Event'] and settings['Location'] and settings['SendTo']:
            self.Title.setText(settings['Title'])
            self.eventComboBox.setEditable(False)
            self.locationBox.setEditable(False)
            self.sendToBox.setEditable(False)
            self.notificationButton.setCheckable(True)
            self.notificationButton.toggle()
            if len(settings) is 5:
                self.notificationButton.setText(settings['NotificationText'])
            else:
                self.notificationButton.setText('Submit')

            # Adds objects to the Dropdown Menu for Events
            for event in settings['Event']:
                self.eventComboBox.addItem(event)

            # Adds objects to the Dropdown Menu for Locations
            for location in settings['Location']:
                self.locationBox.addItem(location)

            # Adds objects to the Dropdown Menu for the Send To
            for sendTo in settings['SendTo']:
                self.sendToBox.addItem(sendTo)

            # self.notificationButton.clicked.connect(self.submitData())
            if self.notificationButton.isChecked():
                self.notificationButton.clicked.connect(lambda: self.submitData())

            self.setWindowTitle('Event Box')
            self.show()
            # self.QApplication(sys.argv)
            # sys.exit(self.exec_())
        else:
            print('Incorrect Dictionary Format')

    """
    Aqui esta la funcion que hace el submit al database, en print(str(a)), a es el string que se va a submit al database
    """
    def submitData(self):
        print(str(self.eventComboBox.currentText()))
        print(str(self.locationBox.currentText()))
        print(str(self.sendToBox.currentText()))
        print(str(self.commentBox.toPlainText()))
        data = {
            'Event': self.eventComboBox.currentText(),
            'Location': self.locationBox.currentText(),
            'Data': self.commentBox.toPlainText(),
            'Employees': ['fernan@upr.edu', 'raul@upr.edu', 'alejandra@upr.edu']
        }
        print(data)
        test = db.child('NatAlert').push(data)
        if test:
            print(test)
            global messageBox
            messageBox = QMessageBox.information(self, 'Success', 'Notification Sent Successfully!!')
            print(db.child('NatAlert').get().val())
            # alertWindow = loadUi('alert.ui')
            # alertWindow.show()



    def init_DB(self):
        config = {
            'apiKey': "AIzaSyAcIg6EsfC5EKCF-thwhiOFO1XNDkFJDDQ",
            'authDomain': "natalert-e328e.firebaseapp.com",
            'databaseURL': "https://natalert-e328e.firebaseio.com",
            'projectId': "natalert-e328e",
            'storageBucket': "natalert-e328e.appspot.com",
            'messagingSenderId': "250353217129",
            "serviceAccount": "../natalert-e328e-firebase-adminsdk-9qkk7-cd5290dd8c.json"

         }
        global firebase
        firebase = pyrebase.initialize_app(config)
        auth = firebase.auth()
        global user
        user = auth.sign_in_with_email_and_password('christian.santiago23@upr.edu', 'Machluan0212')
        global db
        db = firebase.database()
        print(user['idToken'])




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UIClass()
    # window.setWindowTitle('Eventr Box')
    # window.show()
    sys.exit(app.exec_())
