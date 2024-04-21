from configparser import ConfigParser


def load_config(filename="database.ini", section="postgresql"):
    parser = ConfigParser()
    parser.read(filename)

    # кажется получаем данные с нашего ини файла, но я бы предпочел все же использовать env файл нежели ini. Так как уже работал с ними через dotenv
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    
    return config


if __name__ == "__main__":
    config = load_config()
    print(config)

# Конфиг файл нужен что бы извлечь данные с ini файла, данные которые в них должны хранится в секрете, но я все еще предпочитаю использовать env файл чем ini
# Код сработал успешно, и так, как хотелось бы