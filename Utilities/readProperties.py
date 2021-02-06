import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/config.ini")


class ConfigReader:

    @staticmethod
    def getUrl():
        Url = config.get("common data", "base_url")
        return Url

    @staticmethod
    def getUserEmail():
        userEmail = config.get("common data", "username")
        return userEmail

    @staticmethod
    def getPassword():
        password = config.get("common data", "password")
        return password
