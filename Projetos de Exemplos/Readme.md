# Projetos de exemplo para estudos

## Web Scraping

## Aprendendo a extrair informações de uma página web

Nesse projeto usei o framework scrapy para extrair algumas informações do site Tripadvisor a respeito da **Lagoa do Paraíso** em **Jericoacoara(Ceará)** local que pretendo conhecer em breve.

Foram extraídas as seguintes informações:

- Nome da pessoa que comentou;
- Localização de onde essa pessoa mora;
- Título do comentário;
- Descrição do comentário;
- Data do comentário;
- Tipo de viagem.

<img src="Web%20scraping/Image/coment.png" >

**Ferramentas utilizadas:**

- Python 3
- Scrapy

**observação:** A versão do python precisa ser superior a 3.5

### Preparando o ambiente:

- Criando um ambiente virtual

`pip install virtualenv`

`virtualenv nomeambiente`

- Instalando o scrapy

`conda install -c conda-forge scrapy`

### Estrutura do projeto:

No arquivo items.py e comentarios.py (esse último arquivo está na pasta spiders) você encontra toda a estrutura utilizada para o desenvolvimento do projeto os outros arquivos são criados automaticamente quando iniciamos o scrapy.

### Exportando os dados:

Depois que os dados foram extraídos as informações foram salvas em arquivos .csv e .json, o intuito e deixar os dados devidamente preparados para uma análise mais profunda.

## NLP

## Data Cleaning

## Dataset _<https://www.kaggle.com/karrrimba/movie-metadatacsv>_

O objetivo principal era prever o gênero do filme com base na descrição da trama
utilizando o primeiro dataset, porém durante a análise dos dados observei que a coluna genêro desse dataset possui muitos valores incorretos como: números, palavras incorretas, palavras escritas fora da ordem e palavras com variação ortográfica mais que se referem à mesma coisa.

Durante os estudos de NLP (_Natural language processing_), conheci a biblioteca fuzzywuzzy que é usada para correspondência de string. No segundo dataset temos uma coluna que possui vários genêros e subgenêros de filmes e que já está devidamente limpa, peguei esses dados e através da biblioteca fuzzywuzzy apliquei a similaridade de strings no dataset onde os dados estão incorretos. Além de corrigir os prblemas que já foram citados acima consegui reduzir o número de genêros do meu dataset de 2265 valores únicos para 995 valores únicos.
