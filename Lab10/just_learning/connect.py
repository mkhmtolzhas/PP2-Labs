import psycopg2 # Я предпочел бы asyncpg, так как я НЕДОБЕКЕНДЕР, НЕДОПИТОНИСТ, И Я СЛЕДУЮ ТРЕНДАМ, Я СТАДО
from config import load_config # Ну тут понятно, данные нужны

def connect(config):
    try:
        with psycopg2.connect(**config) as conn:
            print(f"{config["user"]} успешно подключился к серверу.")
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == "__main__":
    connect(load_config())