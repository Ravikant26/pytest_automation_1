import configparser


config=configparser.RawConfigParser()
config.read("E:\\user\\CT-19_notes_2024\\6_python_selenium_class_5_03_july_2024\\configuration\\config.ini")

class Readconfigdata():
    @staticmethod
    def getusername():
        username=config.get("login data",'username')
        return username

    @staticmethod
    def getpassword():
        password=config.get("login data","password")
        return password


