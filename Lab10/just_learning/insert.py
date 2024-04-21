import psycopg2 # Срочно дайте асинкпиджи пажеееее
from config import load_config

def insert_vendor(vendor_name):
    sql = """INSERT INTO vendors(vendor_name)
            VALUES(%s) RETURNING vendor_id;"""
    

    vendor_id = None
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Экзекютим
                cur.execute(sql, (vendor_name,))

                # получаем сгенерированный айди чтоль

                rows = cur.fetchone()
                if rows:
                    vendor_id = rows[0]
                

                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        return vendor_id
    

if __name__ == "__main__":
    insert_vendor("3M Co.")
    # Ачо это? так же мне кажется мы нарушаем принцип DRY. если будем каждый раз писать коннекшон, я думаю как то это облегчить
