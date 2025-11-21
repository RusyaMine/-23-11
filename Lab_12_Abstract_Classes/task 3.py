from abc import ABC, abstractmethod
from time import sleep


class log(ABC):
    def header(self):
        return "===LOG START==="
    @abstractmethod
    def log(self,message):
        pass
class FileLogger(log):
    def __init__(self,filename="log.txt"):
        self.filename=filename
    def log(self,message):
        with open(self.filename, "a") as file:
            file.write(message + "\n")
        print(f"Written to {self.filename}")

class ConsoleLogger(log):

            def log(self, message):
                print(f"[Console] {message}")
if __name__ == "__main__":
    console = ConsoleLogger()
    file_logger = FileLogger()

    console.header()
    console.log("Hello world")

    file_logger.header()
    file_logger.log("Запись в журнал:")