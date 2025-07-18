# IBGE Data Fetcher

## Descrição
IBGE Data Fetcher é uma aplicação web desenvolvida com Streamlit que permite consultar dados populacionais de nomes brasileiros por estado, utilizando a API pública do IBGE.

## Funcionalidades
- Consulta de nomes na base de dados do IBGE
- Visualização da distribuição populacional por estado
- Exibição do total de ocorrências do nome pesquisado

## Requisitos
- Python 3.6 ou superior
- Bibliotecas necessárias:
  - streamlit
  - pandas
  - requests

## Instalação

```bash
# Clone o repositório (se estiver usando git)
git clone <url-do-repositorio>

# Navegue até o diretório do projeto
cd <diretorio-do-projeto>

# Instale as dependências
pip install streamlit pandas requests
```

## Como usar

1. Execute a aplicação:
```bash
streamlit run app.py
```

2. Acesse a aplicação no navegador (geralmente http://localhost:8501)

3. Digite um nome no campo de pesquisa e clique em "Search"

4. Visualize os resultados da distribuição populacional por estado

## Sobre os dados
Os dados são obtidos em tempo real da API pública do IBGE:
- API de nomes: https://servicodados.ibge.gov.br/api/v2/censos/nomes
- API de estados: https://servicodados.ibge.gov.br/api/v1/localidades/estados

## Estrutura do projeto
- `app.py`: Arquivo principal contendo o código da aplicação
