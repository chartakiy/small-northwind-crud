# employees, orders, customers jadvallariga CRUD yozib kelish
# 1ta orderni ko'ryotganda -> order_detailsni to'la ko'rish
# 2ta sana qabul qilib, mana shu sana oraligidagi orderlar ro'yxatini chiqarib kelish
import psycopg2

class DataConnect:
  def __init__(self):
    self.connection = psycopg2.connect(
      dbname = 'n71__23_10',
      user = 'johnibek',
      password = '123john',
      host = 'localhost',
      port = 5433
    )
    self.cursor = self.connection.cursor()
    print("successfully connected to the database")


def main():
  db = DataConnect()


if __name__ == "__main__":
  main()