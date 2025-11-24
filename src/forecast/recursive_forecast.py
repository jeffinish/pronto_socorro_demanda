import pandas as pd

import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def recursive_forecast(df, model, features, steps=24):
    """
    df: dataframe completo com todas as features calculadas até o último instante observado
    steps: número de horas futuras
    """
    df_forecast = []
    last_df = df.copy()

    for _ in range(steps):
        # 1. Criar linha futura
        next_time = last_df.index[-1] + pd.Timedelta(hours=1)
        logging.info(f"Prevendo para {next_time}")
        row = {
            "datetime": next_time,
            "month": next_time.month,
            "dayofweek": next_time.dayofweek,
            "hour": next_time.hour,
            "is_weekend": 1 if next_time.dayofweek >= 5 else 0,
        }

        # 2. Criar lags e janelas usando o próprio df
        last_segment = last_df["demand"]

        for lag in [1, 2, 3, 24, 48, 168]:
            row[f"demand_lag_{lag}"] = last_segment.iloc[-lag]
            # logging.info(f"Lag {lag}: {row[f'demand_lag_{lag}']}")

        # rolling features
        for roll in [3,6,12,24]:
            row[f"demand_roll_mean_{roll}"] = last_segment.iloc[-roll:].mean()
            row[f"demand_roll_std_{roll}"]  = last_segment.iloc[-roll:].std()
            # logging.info(f"Rolling {roll} mean: {row[f'demand_roll_mean_{roll}']}")
            # logging.info(f"Rolling {roll} std: {row[f'demand_roll_std_{roll}']}")
        
        # 3. Criar dataframe temporário
        row_df = pd.DataFrame([row]).set_index("datetime")

        # 4. Prever demanda futura
        yhat = model.predict(row_df[features])[0]
        logging.info(f"Previsão: {yhat}")

        # 5. Registrar previsão
        row_df["demand"] = yhat

        # 6. Adicionar aos resultados e à série base
        df_forecast.append(row_df)
        last_df = pd.concat([last_df, row_df], axis=0)

    return pd.concat(df_forecast)
