import requests
from requests import get
from bs4 import BeautifulSoup
import re
import pandas as pd
import warnings
import time
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python import PythonOperator, PythonVirtualenvOperator
from airflow.utils.dates import days_ago
from time import perf_counter
warnings.filterwarnings("ignore")

# Definindo funções


def getPage():
    url = "http://parceiros.heineken.com.br/irj/portal"
    try:
        user = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'}
        response = requests.get(url, headers=user, timeout=30, verify=False)
        print(response.status_code)
    except requests.exceptions.RequestException:
        return None

    bs = BeautifulSoup(response.content, 'html.parser')
    string = [s.text for s in bs.find(
        'div', {'align': 'center'}).find_all('strong')][0]

    return string


def regex_dates(strings):
    try:
        match = re.search(r'(\d+/\d+/\d+)', strings)
    except:
        match = None
    return match.group(1)


def read_table():

    url = "https://ptax.bcb.gov.br/ptax_internet/consultarTodasAsMoedas.do?method=consultaTodasMoedas"
    dataframe = pd.read_html(url,
                             decimal=',', thousands='.')[0]

    print("lendo tabela")
    print(dataframe.tail())
    return dataframe


def transform_dataframe():

    dataframe = read_table()
    strings = getPage()

    dataframe_transformed = dataframe[dataframe.Tipo != 'Tipo']
    dataframe_transformed['Data'] = regex_dates(strings)
    dataframe_transformed2 = dataframe_transformed[['Data', 'Cod Moeda', 'Tipo', 'Moeda',
                                                    'Taxa Compra', 'Taxa Venda', 'Paridade Compra', 'Paridade Venda']]

    dataframe_transformed2.rename(columns={'Data': 'DATA',
                                           'Cod Moeda': 'COD_MOEDA',
                                           'Tipo': 'TIPO',
                                           'Moeda': 'MOEDA',
                                           'Taxa Compra': 'TAXA_COMPRA',
                                           'Taxa Venda': 'TAXA_VENDA',
                                           'Paridade Compra': 'PARIDADE_COMPRA',
                                           'Paridade Venda': 'PARIDADE_VENDA'}, inplace=True)
    print("transformando a tabela")
    print(dataframe_transformed2.tail())
    return dataframe_transformed2


def save_csv():
    files = transform_dataframe()
    files.to_csv("/home/eden/jsons/currency.csv",
                 index=False, encoding='utf-8')
    print("exportando aqrquivo")


# configuração da DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    # Exemplo: Inicia em 20 de Janeiro de 2021
    'start_date': datetime(2021, 4, 29),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    # Em caso de erros, tente rodar novamente apenas 1 vez
    'retries': 1,
    # Tente novamente após 30 segundos depois do erro
    'retry_delay': timedelta(seconds=30),
    # Execute uma vez a cada 15 minutos
    'schedule_interval': '*/2 * * * *'
}

with DAG(dag_id='moedas',
         default_args=default_args,
         schedule_interval=None,
         tags=['currency']
         ) as dag:

    # tarefa para acessar o site
    t1 = PythonOperator(
        task_id='acessa_site',
        python_callable=getPage,
        do_xcom_push=False,
        dag=dag,
    )

    # ler a tabela html no site
    t2 = PythonOperator(
        task_id='retorna_tabela',
        python_callable=read_table,
        do_xcom_push=False,
        dag=dag,
    )

    # aplicar transformações na tabela
    t3 = PythonOperator(
        task_id='transforma_tabela',
        python_callable=transform_dataframe,
        do_xcom_push=False,
        dag=dag,
    )

    # salvar o arquivo csv
    t4 = PythonOperator(
        task_id='salva_arquivo',
        python_callable=save_csv,
        do_xcom_push=False,
        dag=dag,
    )

    # dependências entre as tarefas
    t1 >> t2 >> t3 >> t4
