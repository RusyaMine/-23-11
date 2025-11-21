from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self):
        pass

    @abstractmethod
    def close(self):
        pass


class SQLiteDatabase(DatabaseInterface):
    def connect(self):
        print("Connecting to SQLite...")

    def execute_query(self):
        print("Executing SQLite query...")

    def close(self):
        print("Closing SQLite connection...")


if __name__ == "__main__":
    dbs = [SQLiteDatabase()]

    for db in dbs:
        db.connect()
        db.execute_query()
        db.close()
