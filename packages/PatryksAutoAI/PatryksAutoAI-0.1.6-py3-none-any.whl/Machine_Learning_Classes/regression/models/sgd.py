from sklearn.model_selection import GridSearchCV, train_test_split,KFold
from sklearn.metrics import mean_squared_error
from Machine_Learning_Classes.regression.metrics_regression import Metrics
from sklearn.linear_model import SGDRegressor
import numpy as np

class SGD(Metrics):
    def __init__(self):
        self.model = None
        self.parameters = None

    def create(self, X, y, params=None):
        if params == None:
            gbm = SGDRegressor()
            gbm.fit(X,y)
            self.model = gbm
        else:
            gbm = SGDRegressor(**params)
            gbm.fit(X,y)
            self.model = gbm
            self.parameters = params
         
    def create_grid(self,X,y, params=None, cv=3):
        params_columns = ['loss', 'penalty', 'alpha', 'learning_rate', 'eta0']

        params_basic = {
            'loss': ['squared_epsilon_insensitive', 'epsilon_insensitive', 'squared_error', 'huber'],
            'penalty': ['l1', 'l2', 'elasticnet'],
            'alpha': [0.0001, 0.001, 0.01],
            'learning_rate': ['constant', 'optimal', 'invscaling', 'adaptive'],
            'eta0': [0.001, 0.01, 0.1],
        }
        if params == None:
                params = params_basic
        else:
            for parameter in params_columns:
                if parameter not in params.keys():
                    params[parameter] = params_basic[parameter]
        
        sgd = SGDRegressor()
        grid_search = GridSearchCV(sgd, params, cv=cv)
        grid_search.fit(X, y)
        best_params = grid_search.best_params_
        best_model = grid_search.best_estimator_
        self.model = best_model
        self.parameters = best_params

    def score(self, X, y):
        preds = np.round(self.model.predict(X))
        return self.calculate_metrics(y, preds)

    def predict(self, X):
        return self.model.predict(X)
    
    def evaluate_kfold(self, X, y, df_test, n_splits=5, params=None):
        if params == None:
            params = self.parameters
        kfold = KFold(n_splits=n_splits, shuffle=True, random_state=42)
        if y.shape[1] > 1:
          predictions = np.zeros(shape=(df_test.shape[0],y.shape[1]))
        else:
          predictions = np.zeros(shape=(df_test.shape[0],))
        roc = []
        n=0

        for i, (train_index, valid_index) in enumerate(kfold.split(X,y)):
            X_train, X_test = X.iloc[train_index], X.iloc[valid_index]
            y_train, y_test = y.iloc[train_index], y.iloc[valid_index]
            self.create(X_train,y_train,params=params)
            predictions += self.predict(df_test)/n_splits
            val_pred = self.predict(X_test)
            roc.append(mean_squared_error(y_test,val_pred))

            print(f"{i} Fold scored: {roc[i]}")

        print(f"Mean roc score {np.mean(roc)}")
        return predictions

    def get(self):
        return self.model
    
    def get_parameters(self):
        return self.parameters