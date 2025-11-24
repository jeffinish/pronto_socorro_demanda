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
- `notebooks/` : Jupyter notebooks com análise e experimentos
	- `1 - Análise Exploratória.ipynb` : exploração inicial dos dados
	- `2 - Modelo Linear.ipynb` : implementação de um modelo linear básico
	- `2.1 - Modelo Linear + Features.ipynb` : adição de novas features
	- `2.2 - Modelo Linear Refinado.ipynb` : refinamentos e avaliação
- `src/` : código fonte com funções de engenharia de features
	- `features/feature_engineering.py` : funções para transformar os dados
- `README.md` : este arquivo

**Dados**

- Fonte: arquivo CSV em `data/raw/dataset_pronto_socorro.csv`.
- Observações: manter cópia dos dados brutos em `data/raw/` e versões limpas em `data/processed/`.

**Notebooks e fluxo recomendado**

1. Abrir `notebooks/1 - Análise Exploratória.ipynb` para entender as colunas, valores faltantes e distribuições.
2. Executar `notebooks/2 - Modelo Linear.ipynb` para ver uma baseline de modelos lineares.
3. Passar para `2.1` e `2.2` para engenharia de features e refinamentos.

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

**Código**

O código reutilizável está em `src/features/feature_engineering.py`. Use essas funções para transformar os dados antes de treinar modelos nos notebooks.

**Resultados e métricas**

Nos notebooks de modelagem são exploradas métricas típicas para regressão e/ou classificação (por exemplo, RMSE, MAE, R², AUC), dependendo do objetivo final (prever contagem de demanda ou classes de lotação).

**Próximos passos sugeridos**

- Criar `requirements.txt` e/ou `environment.yml` para reproduzibilidade
- Adicionar scripts de pré-processamento em `src/` para pipeline reproducível
- Testes unitários básicos para funções em `src/features`
- Explorar modelos não-lineares (tree-based, ensembles) e validação temporal

**Contribuição**

Contribuições e sugestões são bem-vindas. Abra uma issue descrevendo a proposta ou um pull request com mudanças.

**Licença**

Colocar aqui a licença desejada (ex.: MIT) ou manter para discussão.

---

Se quiser, posso também:

- Gerar `requirements.txt` automaticamente a partir do ambiente
- Criar um `Makefile`/scripts para executar pipeline
- Adicionar um notebook de avaliação final com gráficos resumidos

Diga qual desses próximos passos você prefere que eu faça primeiro.
