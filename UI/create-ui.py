#!/usr/bin/env/python3

import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *


class UI(QDialog):

    def __init__(self):
        super(UI, self).__init__()
        loadUi('event-handler.ui', self)
        self.settings = {
            'Title': 'Event Handler',
            'Event': ['Fire Hazard', 'Shooting Hazard', 'Earthquake Hazard'],
            'Location': ['Stefani Bldg', 'Luchetti Bldg', 'Centro de Estudiantes'],
            'SendTo': ['All', 'None', 'Some'],
            'NotificationText': 'Send Notification'
        }
        self.Title.setText(self.settings['Title'])
        self.eventComboBox.setEditable(False)
        self.locationBox.setEditable(False)
        self.sendToBox.setEditable(False)
        self.notificationButton.setText(self.settings['NotificationText'])

        # Adds objects to the Dropdown Menu for Events
        for event in self.settings['Event']:
            self.eventComboBox.addItem(event)

        # Adds objects to the Dropdown Menu for Locations
        for location in self.settings['Location']:
            self.locationBox.addItem(location)

        # Adds objects to the Dropdown Menu for the Send To
        for sendTo in self.settings['SendTo']:
            self.sendToBox.addItem(sendTo)








if __name__ =='__main__':
    app = QApplication(sys.argv)
    window = UI()
    window.setWindowTitle('Event Box')
    window.show()
    sys.exit(app.exec_())
