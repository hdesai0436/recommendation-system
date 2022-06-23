from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

class model_finder:
    def __init__(self):
        self.lg = LogisticRegression()

    def get_best_param_logistic(self,x_train,y_train):
        try:
            self.param_grid = {'solver':['newton-cg', 'lbfgs', 'liblinear'],'penalty':['l2'],
            'C':[1.0, 0.1, 0.01]}
            self.grid = GridSearchCV(estimator=self.lg,param_grid=self.param_grid,cv=3,verbose=5)

            self.grid.fit(x_train,y_train)

            #best parameter 
            self.solver = self.grid.best_params_['solver']
            self.penalty = self.grid.best_params_['penalty']
            self.C = self.grid.best_params_['C']

            #create new model with best parameters

            self.new_lg = LogisticRegression(penalty=self.penalty,C=self.C,solver=self.solver)

            self.new_lg.fit(x_train,y_train)

            return self.new_lg
        except Exception as e:
            raise(e)