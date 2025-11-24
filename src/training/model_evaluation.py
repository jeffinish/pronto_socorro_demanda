import numpy as np
import pandas as pd

from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error

def evaluate_model(model, X, y, tscv):
    metrics = []
    for train_idx, test_idx in tscv.split(X):
        X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
        y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

        model.fit(X_train, y_train)
        preds = model.predict(X_test)

        mae  = mean_absolute_error(y_test, preds)
        rmse = np.sqrt(mean_squared_error(y_test, preds))
        mape = np.mean(np.abs((y_test - preds) / y_test)) * 100
        r2   = r2_score(y_test, preds)

        metrics.append([mae, rmse, mape, r2])

    return pd.DataFrame(metrics, columns=["MAE", "RMSE", "MAPE", "R2"]) , pd.DataFrame({'model':str(model.named_steps['model']),'y_true':y_test, 'y_pred':preds})