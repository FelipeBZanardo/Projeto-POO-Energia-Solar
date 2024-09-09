# Projeto Final - Programação Orientada a Objetos (Python)
> *Turma 11080 - Santander Coders 2024 - Engenharia de Dados*

Desenvolvimento do projeto "Impacto da Energia Solar" com o intuito de extrair dados da API (Application Programming Interface) da OWID (Our World In Data), manipular os dados, persistí-los em um Banco de Dados e, por fim, gerar insights através da plotagem de gráficos.
**Todo projeto foi desenvolvido com a linguagem de programação Python.**

## ✒️Autores 
- [Alessandra Cruz](https://github.com/alessandracruz)
- [Álex Buracosky](https://github.com/aburacosk)
- [Diana Osorio](https://github.com/diana468)
- [Diogo Moura](https://github.com/HyogoMoura)
- [Felipe Zanardo](https://github.com/FelipeBZanardo)
- [Thiago Silva](https://github.com/thiagodemedeiros)

## 📋 Descrição do Projeto

**1) Extração de Dados:** API da OWID
- [solar-pv-cumulative-capacity](https://ourworldindata.org/grapher/solar-pv-cumulative-capacity)
- [solar-pv-prices](https://ourworldindata.org/grapher/solar-pv-prices)
- [modern-renewable-energy-consumption](https://ourworldindata.org/grapher/modern-renewable-energy-consumption)

**2) Manipulação de Dados:** 
- Alteração nos nomes de cada coluna;
- Verificação de valores nulos;
- Verificação e conversão dos tipos de dados de cada coluna;
- Merge de DataFrames;
- Conversão de valores monetários de Dólar para Real.

**3) Geração de gráficos:**
- Capacidade de Geração de Energia Solar vs Preço/Geração;
- Geração de Energia Renovável pelo mundo.

**4) Persistência no Banco de Dados: SQLite**
- Tabelas geradas são persistidas localmente no banco de dados SQLite
- Verificar arquivo: [energia_renovavel3.db](https://github.com/FelipeBZanardo/Projeto-POO-Energia-Solar/blob/main/energia_renovavel3.db)
---

## Demonstração
<p align="center">
  <img src="./_captures/Demonstracao.gif">
</p>

## 📋  Pré-requisitos
- Ter instalado o **[Python](https://www.python.org/)**;
- Ter instalado todas as bibliotecas Python listadas ao decorrer desse Readme;
- Ter instalado uma IDE de sua preferencia:
    - **[Visual Studio Code](https://code.visualstudio.com/)**, por exemplo.
    - **[Google Colab](https://colab.research.google.com/notebook)** (Não é necessário instalação).

## ⚙️ Executar o projeto:
- Fazer o clone do repositório do projeto [Projeto-POO-Energia-Solar](https://github.com/FelipeBZanardo/Projeto-POO-Energia-Solar);
- Abrir o arquivo **main.ipynb** na IDE;
- Selecionar a opção "Run All" para iniciar todas as funções;
- Pronto! Veja toda a manipulação de dados presente no notebook, a criação de gráficos e por fim a persistência no banco de dados.

## 🧾 Bibliotecas Python utilizadas
Clique sobre o link para instalar cada biblioteca utilizada.

- [API de Dados OWID](https://pypi.org/project/owid-catalog/):
`from owid.catalog import charts `
`from owid import catalog `

- [Pandas](https://pypi.org/project/pandas/):
`import pandas as pd`

- [SQLite3](https://pypi.org/project/db-sqlite3/):
`import sqlite3`

- [SQLAlchemy](https://pypi.org/project/SQLAlchemy/):
`from sqlalchemy import create_engine`

- [OS](https://pypi.org/project/os-sys/):
`import os`

- Plotagem de gráficos com [Matplotlib](https://pypi.org/project/matplotlib/):
`import matplotlib.pyplot as plt`

- Plotagem de gráficos com [Seaborn](https://pypi.org/project/seaborn/):
`import seaborn as sns`

- [Enum](https://pypi.org/project/enum/):
`from enum import Enum`

- Requisição http via [Requests](https://pypi.org/project/requests/):
`import requests`

- [JSON](https://pypi.org/project/jsonlib/):
`import json`

## 🛠️ Tecnologias Utilizadas

* [Visual Studio Code](https://code.visualstudio.com/) - IDE 
* [Python](https://www.python.org/) - Linguagem de Programação

## 📈 Melhorias futuras

- Buscar tabelas em diferentes fontes de dados, não somente a da OWID;
- Melhorar a criação de gráficos.
- Criar um banco de dados persistido em núvem;
- Fazer o deploy do projeto;

## 📺 Apresentação
(https://docs.google.com/presentation/d/1Xh4UbzwNorR2PUcvsOygN5ebmMStlnAeewYMZBKHT0Y/edit#slide=id.g2d2c011bc31_0_115)


