import pandas as pd

def create_lag_features(df, column="demand", lags=[1,2,3,24,48,168]):
    """
    Cria colunas defasadas (lags).
    Ex: demanda na última hora, dia anterior, semana anterior...
    """
    for lag in lags:
        df[f"{column}_lag_{lag}"] = df[column].shift(lag)
    return df


def create_rolling_features(df, column="demand", windows=[3,6,12,24]):
    """
    Cria médias móveis e desvios de janelas móveis.
    """
    for w in windows:
        df[f"{column}_roll_mean_{w}"] = df[column].rolling(w).mean()
        df[f"{column}_roll_std_{w}"]  = df[column].rolling(w).std()
    return df


def add_time_features(df):
    """
    Adiciona variáveis temporais úteis.
    """
    df["hour"] = df.index.hour
    df["dayofweek"] = df.index.dayofweek  # Já existe no dataset original
    df["month"] = df.index.month
    df["is_weekend"] = df["dayofweek"].isin([5,6]).astype(int)
    return df
