import pandas as pd

class Get_data:
    def __init__(self,file_path):
        self.file_path= file_path

    def getdata(self):
        self.data = pd.read_csv(self.file_path)
        return self.data

