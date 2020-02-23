class MainTest:

    _class_number = 20
    _class_string = 'Hello , world!'

    @staticmethod
    def get_local_number():
        return 14

    @staticmethod
    def get_class_number():
        return MainTest._class_number

    @staticmethod
    def get_class_string():
        return MainTest._class_string

