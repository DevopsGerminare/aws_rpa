# Importando bibliotecas
import psycopg2
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime

# Configurações do Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.google.com/search?q=dolar')

# Capturando valor do dólar
dolar_element = driver.find_element(by='xpath', value='//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')
dolar = float(dolar_element.text.replace(',', '.'))

# Capturando data e hora
data = datetime.now().strftime('%Y-%m-%d')
horario = datetime.now().strftime('%H:%M:%S')

# Inserindo no banco de dados
conn = psycopg2.connect('postgres://avnadmin:AVNS_kEd3qvXSZW_LoEuliQW@interdisciplinar-dion-heitorbelo.h.aivencloud.com:24707/defaultdb?sslmode=require')
cur = conn.cursor()

query_sql = 'INSERT INTO dolar (data, horario, valor) VALUES (%s, %s, %s)'
cur.execute(query_sql, (data, horario, dolar))

# Efetivando a transação
conn.commit()

# Fechando conexão com o banco e o Selenium
cur.close()
conn.close()
driver.quit()
