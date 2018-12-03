#!/usr/bin/env/python3

import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import pyrebase


class UIClass(QDialog):
    """ Global variables for initializing the firebase database """
    global firebase
    global user
    global db
    global settings

    def __init__(self):
        super(UIClass, self).__init__()
        """" Loads the .ui template for the UI Design """
        loadUi('event-handler.ui', self)
        settings = {
            'Title': 'Event Box',
            'Event': ['Fire', 'Tsunami', 'Shooting'],
            'Location': ['Luchetti', 'Stefani'],
            'SendTo': [
                ['fernan@upr.edu', 'raul@upr.edu', 'alejandra@upredu'],
                ['christian@upr.edu', 'raul@upr.edu'],
                ['raul@upr.edu', 'alejandra@upr.edu'],
                ['fernan@upr.edu', 'christian@upr.edu']
            ]
        }
        self.initUI()
        self.init_DB()

    """ Method to set the text that will be displayed in the UI """
    def initUI(self):

        if settings['Title'] and settings['Event'] and settings['Location'] and settings['SendTo']:
            self.Title.setText(settings['Title'])
            """ Initializes all the components of the UI template"""
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
                self.sendToBox.addItem(str(sendTo))

            # Checks if the submit button is clicked, if clicked calls the submiData() function
            if self.notificationButton.isChecked():
                self.notificationButton.clicked.connect(lambda: self.submitData())

            self.setWindowTitle('Event Box')
            self.show()
            # self.QApplication(sys.argv)
            # sys.exit(self.exec_())
        else:
            print('Incorrect Dictionary Format')

    """ Submits the data selected in the UI, to the database using a dictionary"""
    def submitData(self):
        print(str(self.eventComboBox.currentText()))
        print(str(self.locationBox.currentText()))
        print(str(self.sendToBox.currentText()))
        print(str(self.commentBox.toPlainText()))
        employees = self.sendToBox.currentText().split(',')
        data = {
            'Event': self.eventComboBox.currentText(),
            'Location': self.locationBox.currentText(),
            'Data': self.commentBox.toPlainText(),
            'Employees': employees
        }
        print(data)
        response = db.child('NatAlert').push(data)
        if response:
            print(response)
            global messageBox
            messageBox = QMessageBox.information(self, 'Success', 'Notification Sent Successfully!!')
            print(db.child('NatAlert').get().val())

    """" Initializes Database """
    def init_DB(self):
        config = {
            'apiKey': "AIzaSyAcIg6EsfC5EKCF-thwhiOFO1XNDkFJDDQ",
            'authDomain': "natalert-e328e.firebaseapp.com",
            'databaseURL': "https://natalert-e328e.firebaseio.com",
            'projectId': "natalert-e328e",
            'storageBucket': "natalert-e328e.appspot.com",
            'messagingSenderId': "250353217129",
            "serviceAccount": "natalert-e328e-firebase-adminsdk-9qkk7-cd5290dd8c.json"

         }
        global firebase
        firebase = pyrebase.initialize_app(config)
        auth = firebase.auth()
        global user
        user = auth.sign_in_with_email_and_password('christian.santiago23@upr.edu', 'Machluan0212')
        global db
        db = firebase.database()
        print(user['idToken'])


    def setSettings(self, ui_settings):
        global settings
        settings = ui_settings



def start_ui():
    app = QApplication(sys.argv)
    window = UIClass().initUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UIClass()
    sys.exit(app.exec_())
