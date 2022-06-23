
import os
import shutil
import pickle

class file_operations:

    def __init__(self):
        self.model_dir = 'models/'

    def save_model(self,model,filename):
        try:
            

            with open(self.model_dir+'/' + filename +'.sav','wb') as f:
                pickle.dump(model,f)
        except Exception as e:
            raise(e)

    def load_model(self,filename):
        try:
            with open(self.model_dir+'/'+filename+'.sav','rb') as f:
                return pickle.load(f)
        except Exception as e:
            raise(e)


    