import pandas as pd
import numpy as np

def generate_future_features(df, periods, freq=None, feature_function=None):
    """
    Gera um dataframe futuro com as mesmas features utilizadas no modelo.
    
    Parâmetros
    ----------
    df : pd.DataFrame
        DataFrame original contendo uma coluna datetime como índice.
    periods : int
        Quantidade de períodos futuros a gerar.
    freq : str, opcional
        Frequência temporal (ex: 'H' para hora, 'D' para dia).
        Se None, será inferido automaticamente.
    feature_function : callable, opcional
        Função personalizada para gerar features. Caso None,
        será usada a função padrão de features temporais.

    Retorno
    -------
    future_df : pd.DataFrame
        DataFrame contendo datas futuras com todas as features.
    """
    
    # 1️⃣ Inferir frequência automaticamente, caso não seja informada
    if freq is None:
        inferred = pd.infer_freq(df.index)
        if inferred is None:
            raise ValueError("Não foi possível inferir a frequência. Especifique freq='H', por exemplo.")
        freq = inferred

    # 2️⃣ Criar range futuro
    last_date = df.index.max()
    future_index = pd.date_range(start=last_date, periods=periods+1, freq=freq)[1:]

    future_df = pd.DataFrame(index=future_index)

    # 3️⃣ Função padrão de criação de features
    def default_features(df_):
        df_features = df_.copy()
        df_features["hour"] = df_features.index.hour
        df_features["dayofweek"] = df_features.index.dayofweek
        df_features["day"] = df_features.index.day
        df_features["week"] = df_features.index.isocalendar().week.astype(int)
        df_features["month"] = df_features.index.month
        df_features["is_weekend"] = (df_features.index.dayofweek >= 5).astype(int)
        return df_features

    # 4️⃣ Criar features
    if feature_function:
        future_df = feature_function(future_df)
    else:
        future_df = default_features(future_df)

    return future_df
