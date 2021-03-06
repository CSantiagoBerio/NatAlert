#!/usr/bin/env/python3

import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import pyrebase
import os

global firebase
global user
global db
global settings


class UIClass(QDialog):
    """ Global variables for initializing the firebase database """

    def __init__(self):
        super(UIClass, self).__init__()
        """" Loads the .ui template for the UI Design """
        loadUi('../UI/event-gui.ui', self)
        global settings
        # settings = {
        #     'Title': 'Event Box',
        #     'Event': ['Fire', 'Tsunami', 'Shooting'],
        #     'Location': ['Luchetti', 'Stefani'],
        #     'SendTo': [
        #         ['fernan@upr.edu', 'raul@upr.edu', 'alejandra@upredu'],
        #         ['christian@upr.edu', 'raul@upr.edu'],
        #         ['raul@upr.edu', 'alejandra@upr.edu'],
        #         ['fernan@upr.edu', 'christian@upr.edu']
        #     ]
        # }
        # self.initUI()
        self.init_DB()

    """ Method to set the text that will be displayed in the UI """

    def initUI(self):
        print(settings)
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
        employees = self.sendToBox.currentText().split(',')
        data = {
            'Event': self.eventComboBox.currentText(),
            'Location': self.locationBox.currentText(),
            'Data': self.commentBox.toPlainText(),
            'Employees': employees
        }
        response = db.child('NatAlert').push(data)
        if response:
            print(response)
            global messageBox
            messageBox = QMessageBox.information(self, 'Success', 'Notification Sent Successfully!!')
            # print(db.child('NatAlert').get().val())

    """" Initializes Database """
    def init_DB(self):
        config = {
            'apiKey': "AIzaSyCxz7dDDX4KVUiNPAEDdFtrf26BBWQEKis",
            'authDomain': "video-tutorial-11b93.firebaseapp.com",
            'databaseURL': "https://video-tutorial-11b93.firebaseio.com",
            'projectId': "video-tutorial-11b93",
            'storageBucket': "video-tutorial-11b93.appspot.com",
            'messagingSenderId': "49877822446",
            'serviceAccount': "../json/video-tutorial-11b93-firebase-adminsdk-d6prw-86ab436a0a.json"
        }
        # config = {
        #     'apiKey': "AIzaSyBs0LtxeryvUfyKgbTijv70YSqA_B7Cjfw",
        #     'authDomain': "project-f7931.firebaseapp.com",
        #     'databaseURL': "https://project-f7931.firebaseio.com",
        #     'projectId': "project-f7931",
        #     'storageBucket': "project-f7931.appspot.com",
        #     'messagingSenderId': "967788269453",
        #     "serviceAccount": "json/project-f7931-firebase-adminsdk-nma4s-deffd903d3.json"
        # }

        # config = {
        #     'apiKey': "AIzaSyAcIg6EsfC5EKCF-thwhiOFO1XNDkFJDDQ",
        #     'authDomain': "natalert-e328e.firebaseapp.com",
        #     'databaseURL': "https://natalert-e328e.firebaseio.com",
        #     'projectId': "natalert-e328e",
        #     'storageBucket': "natalert-e328e.appspot.com",
        #     'messagingSenderId': "250353217129",
        #     "serviceAccount": "json/natalert-e328e-firebase-adminsdk-9qkk7-cd5290dd8c.json"
        # }
        global firebase
        firebase = pyrebase.initialize_app(config)
        global db
        db = firebase.database()

    def settings(self, ui_settings):
        global settings
        settings = ui_settings


def parse(settings):
    # print(settings)
    title = custom_split(settings['Title'].split("\""))
    events = custom_split(settings['Event'].split("\""))
    locations = custom_split(settings['Location'].split("\""))
    send_to = custom_split(settings['SendTo'].split("\""))
    # print(title, events, locations, send_to)
    return {'Title': title[0], 'Event': events, 'Location': locations, 'SendTo': send_to}


def custom_split(arr):
    arr2 = []
    length = len(arr)
    for x in range(length):
        if x % 2 == 1:
            arr2.append(arr[x])
    return arr2


def set_settings(ui_settings):
    global settings
    parsed_text = parse(ui_settings)
    settings = parsed_text
    # UIClass().settings(ui_settings)
    print("DONE SETTINGS")


def start_ui():
    app = QApplication(sys.argv)
    UIClass().initUI()
    sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UIClass()
    sys.exit(app.exec_())


def init_db():
    print("DB initiated")
