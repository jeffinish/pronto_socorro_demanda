# Predição de Demanda do Pronto-Socorro

Este repositório contém um estudo de ciência de dados voltado para a predição de demanda em pronto-socorro. O objetivo é explorar, engenheirar features e construir modelos preditivos (regressão/classificação) para estimar a demanda e apoiar decisões operacionais.

**Sumário**

- **Descrição:** objetivo do projeto e escopo
- **Estrutura do repositório:** visão geral dos arquivos e pastas
- **Dados:** origem e formato dos dados brutos e processados
- **Notebooks:** sequência de análises e modelos
- **Como usar:** instruções para reproduzir o trabalho localmente
- **Próximos passos:** sugestões de melhorias

**Descrição**

O projeto foca em técnicas de engenharia de features, avaliação de métricas e modelagem preditiva para estimar a demanda do pronto-socorro com base em dados históricos. É um repositório para estudo e experimentação, não um produto de produção.

**Estrutura do repositório**

- `data/raw/` : dados originais (ex.: `dataset_pronto_socorro.csv`)
- `data/processed/` : dados transformados prontos para modelagem
- `models/` : modelos treinados e salvos
- `notebooks/` : Jupyter notebooks com análise, modelagem e predição
	- `1 - Análise Exploratória.ipynb` : exploração inicial dos dados
	- `2 - Modelo Linear.ipynb` : implementação de um modelo linear básico
	- `2.1 - Modelo Linear + Features.ipynb` : adição de novas features
	- `2.2 - Modelo Linear Refinado.ipynb` : refinamentos e avaliação
	- `3 - Modelos Regulares.ipynb` : exploração de modelos com regularização
	- `4 - Modelos Final.ipynb` : modelos finais e comparações
	- `5 - Predição.ipynb` : realização de predições e validação
- `src/` : código fonte reutilizável e modular
	- `features/` : engenharia de features
		- `feature_engineering.py` : funções para transformar os dados
	- `forecast/` : módulo de predição
		- `recursive_forecast.py` : predições recursivas/encadeadas
	- `training/` : treinamento e avaliação
		- `model_evaluation.py` : métricas e avaliação de modelos
	- `validation/` : validação e processamento
		- `sample_generation.py` : geração de amostras para validação
- `README.md` : este arquivo

**Dados**

- Fonte: arquivo CSV em `data/raw/dataset_pronto_socorro.csv`.
- Observações: manter cópia dos dados brutos em `data/raw/` e versões limpas em `data/processed/`.

**Notebooks e fluxo recomendado**

1. **`1 - Análise Exploratória.ipynb`** : exploração inicial dos dados, colunas, valores faltantes e distribuições
2. **`2 - Modelo Linear.ipynb`** : baseline com modelos lineares
3. **`2.1 - Modelo Linear + Features.ipynb`** : engenharia de features e adição de novas variáveis
4. **`2.2 - Modelo Linear Refinado.ipynb`** : refinamentos e avaliação do modelo linear
5. **`3 - Modelos Regulares.ipynb`** : exploração de modelos com regularização (Ridge, Lasso, ElasticNet)
6. **`4 - Modelos Final.ipynb`** : modelos finais, ensembles e comparações entre abordagens
7. **`5 - Predição.ipynb`** : realização de predições, validação e análise de resultados

**Como reproduzir localmente**

Recomenda-se usar um ambiente virtual (venv ou conda). Exemplo com `venv` no PowerShell:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
# Instale pacotes necessários (exemplo):
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
```

Abrir o Jupyter Notebook:

```powershell
jupyter notebook
```

Observação: se desejar, posso gerar um `requirements.txt` com versões específicas.

**Código e módulos**

O código reutilizável está organizado em módulos temáticos em `src/`:

- **`src/features/feature_engineering.py`** : funções para engenharia de features e transformação dos dados
- **`src/forecast/recursive_forecast.py`** : módulo para realização de predições recursivas/encadeadas
- **`src/training/model_evaluation.py`** : funções para avaliação de modelos e cálculo de métricas
- **`src/validation/sample_generation.py`** : geração de amostras e estratégias de validação

Importe e use essas funções nos notebooks para manter o código limpo e reutilizável.

**Resultados e métricas**

Nos notebooks de modelagem são exploradas métricas típicas para regressão e/ou classificação (por exemplo, RMSE, MAE, R², AUC), dependendo do objetivo final (prever contagem de demanda ou classes de lotação).

**Próximos passos sugeridos**

- Criar `requirements.txt` e/ou `environment.yml` para reproduzibilidade
- Adicionar scripts de pré-processamento em `src/` para pipeline reproducível
- Testes unitários básicos para funções em `src/features`
- Explorar modelos não-lineares (tree-based, ensembles) e validação temporal

**Contribuição**

Contribuições e sugestões são bem-vindas. Abra uma issue descrevendo a proposta ou um pull request com mudanças.
