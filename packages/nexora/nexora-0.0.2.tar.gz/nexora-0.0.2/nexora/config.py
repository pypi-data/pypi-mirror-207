import configparser

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("config.ini")
    default = config["MODEL"]
    print(default["max_depth"])
