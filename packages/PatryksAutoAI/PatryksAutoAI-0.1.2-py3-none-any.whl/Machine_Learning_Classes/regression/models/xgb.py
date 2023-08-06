from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import mean_squared_error,KFold
from model_data.metrics_regression import Metrics
import xgboost as xgb
import numpy as np
import optuna

class XGB(Metrics):
    def __init__(self):
        self.model = None
        self.parameters = None

    def create(self, X, y, params=None):
        if params == None:
            gbm = xgb.XGBRegressor()
            gbm.fit(X,y)
            self.model = gbm
        else:
            gbm = xgb.XGBRegressor(**params)
            gbm.fit(X,y)
            self.model = gbm
            self.parameters = params

    def create_grid(self, X,y, params=None, cv=3):
        params_columns = ['eval_metric', 'boosting_type', 'objective', 'max_bin',
                          'n_estimators', 'max_depth', 'learning_rate', 'subsample',
                          'colsample_bytree', 'gamma', 'min_child_weight', 'pos_scale_weight',
                          'max_delta_step', 'seed', 'num_boost_round', 'verbosity']
        params_basic = {
            'eval_metric': ['rmse'],
            'boosting_type': ['gblinear'],
            'objective': ['regression'],
            'learning_rate': [1e-4, 1e-1],
            'gamma': [0, 1],
            'min_child_weight': [3, 20],
            'pos_scale_weight': [0.1, 2],
            'max_delta_step': [1, 10],
            'num_leaves': [20,200],
            'n_estimators': [30, 100],
            'max_depth': [5, 32],
            'min_child_samples': [30,70],
            'subsample': [0.3, 0.9],
            'colsample_bytree': [0.5, 1.0],
            'seed': [42],
            'max_bin': [255],
            'verbosity': -1
        }
        if params == None:
                params = params_basic
        else:
            for parameter in params_columns:
                if parameter not in params.keys():
                    params[parameter] = params_basic[parameter]

        gbm = xgb.XGBRegressor()
        grid_search = GridSearchCV(gbm, params, cv=cv, n_jobs=-1)
        grid_search.fit(X, y)
        best_model = grid_search.best_estimator_
        self.model = best_model
        self.parameters = grid_search.best_params_

    def create_optuna(self, X, y, params=None, n_trials=5,available_memory_gb=3):
        rows = len(X)
        memory_row = X.memory_usage(deep=True).sum() / rows
        max_bin = int(np.floor(available_memory_gb * 1024**3 / (rows * memory_row)))

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        dtrain = xgb.DMatrix(X_train, label=y_train)
        dtest = xgb.DMatrix(X_test, label=y_test)

        params_columns = ['eval_metric', 'boosting_type', 'objective', 'max_bin',
                          'n_estimators', 'max_depth', 'learning_rate', 'subsample',
                          'colsample_bytree', 'gamma', 'min_child_weight', 'pos_scale_weight',
                          'max_delta_step', 'seed', 'num_boost_round', 'verbosity']
        params_basic = {
            'eval_metric': ['rmse'],
            'boosting_type': ['gblinear'],
            'objective': ['reg:squarederror'],
            'learning_rate': [1e-4, 1e-1],
            'gamma': [0, 1],
            'min_child_weight': [3, 20],
            'pos_scale_weight': [0.1, 2],
            'max_delta_step': [1, 10],
            'num_leaves': [20,200],
            'n_estimators': [30, 100],
            'max_depth': [5, 32],
            'min_child_samples': [30,70],
            'subsample': [0.3, 0.9],
            'colsample_bytree': [0.5, 1.0],
            'seed': [42],
            'max_bin': [255],
            'verbosity': -1
        }
        if params == None:
                params = params_basic
        else:
            for parameter in params_columns:
                if parameter not in params.keys():
                    params[parameter] = params_basic[parameter]
        
        def objective(trial):
            param = {
                'eval_metric': params['eval_metric'],
                'boosting_type': params['boosting_type'],
                'objective': params['objective'],
                'max_bin': params['max_bin'],
                'n_estimators': trial.suggest_int('n_estimators', params["n_estimators"][0], params["n_estimators"][1]),
                'max_depth': trial.suggest_int('max_depth', params["max_depth"][0], params["max_depth"][1]),
                'learning_rate': trial.suggest_loguniform('learning_rate', params['learning_rate'][0], params['learning_rate'][1]),
                'subsample': trial.suggest_uniform('subsample', params['subsample'][0], params['subsample'][1]),
                'colsample_bytree': trial.suggest_uniform('colsample_bytree', params['colsample_bytree'][0], params['colsample_bytree'][1]),
                'gamma': trial.suggest_loguniform('gamma', params['gamma'][0], params['gamma'][1]),
                'min_child_weight': trial.suggest_int('min_child_weight', params['min_child_weight'][0], params['min_child_weight'][1]),
                'scale_pos_weight': trial.suggest_loguniform('scale_pos_weight', params['scale_pos_weight'][0], params['scale_pos_weight'][1]),
                'max_delta_step': trial.suggest_int('max_delta_step', params['max_delta_step'][0], params['max_delta_step'][1]),
                'seed': params['seed'],
                'num_boost_round': params["num_boost_round"],
                'verbosity': params['verbosity']
            }
            xgb_model= xgb.train(param, dtrain)
            y_pred = xgb_model.predict(dtest)
            rmse = np.sqrt(mean_squared_error(y_test, y_pred))
            return rmse
    
        study = optuna.create_study(direction='minimize')
        study.optimize(objective, n_trials=n_trials)
        best_params = study.best_trial.params
        model = xgb.XGBRegressor(**best_params)
        self.model = model.fit(X, y)
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