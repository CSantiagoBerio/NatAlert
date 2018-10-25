import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from UI.testing import *


class UI(QDialog):
    def __int__(self):
        super(UI, self).__int__()
        loadUi('event_handler.ui')
        set = settings
        self.initUI(set)

    def initUI(self, settings):
        if settings['Title'] and settings['Event'] and settings['Location'] and settings['SendTo']:
            self.Title.setText(settings['Title'])
            if settings['NotificationText']:
                self.notificationButton.setText(settings['NotificationText'])
            else:
                self.notificationButton.setText('Submit')

            for item in settings['Event']:
                self.eventComboBox.addItem(item)
            for item in settings['Location']:
                self.locationBox.addItem(item)
            for item in settings['SendTo']:
                self.sendToBox.addItem(item)

            self.setWindowTitle(settings['Title'])
            self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UI()
    sys.exit(app.exec_())
