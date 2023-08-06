import configparser

config = configparser.ConfigParser()
config.read("./config.ini")
b = config.sections()
print(b)
