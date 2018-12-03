from UI.createUI import UIClass
from UI import createUI


class Main:
    def __init__(self):

        super(Main, self).__init__()
        self.settings = {
            'Title': 'From Main',
            'Event': ['From Main', 'From Main2', 'From Main3'],
            'Location': ['From Main', 'From Main2'],
            'SendTo': ['from main', 'not from main']
        }

        createUI.set_settings(self.settings)
        createUI.start_ui()


if __name__ == '__main__':
    # window = UIClass()
    app = Main()
