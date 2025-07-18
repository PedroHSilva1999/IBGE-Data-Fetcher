# IBGE Data Fetcher

## Descrição
IBGE Data Fetcher é uma aplicação web desenvolvida com Streamlit que permite consultar dados populacionais de nomes brasileiros por estado, utilizando a API pública do IBGE.

## Demonstração
![Screenshot da aplicação IBGE Data Fetcher](image.png)

A imagem acima mostra a aplicação em funcionamento com a consulta do nome "Pedro", exibindo:
- Tabela com a distribuição populacional por estado (São Paulo lidera com mais de 4 milhões)
- Total de ocorrências do nome no Brasil (mais de 190 milhões)
- Interface simples e intuitiva com tema escuro

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
git clone https://github.com/PedroHSilva1999/IBGE-Data-Fetcher.git

# Navegue até o diretório do projeto
cd IBGE-Data-Fetcher

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
