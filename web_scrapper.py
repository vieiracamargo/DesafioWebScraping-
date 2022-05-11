#importa as bibliotecas

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


#atribui o  webdrive a variável driver e maximiza a janela
driver = webdriver.Chrome()
driver.maximize_window()

#navega até a página da URL
driver.get("https://www.zoom.com.br/")

#aguarda 1 segundo para o proximo comando
time.sleep(1)

#identifica a barra de busca na URL e escreve "RX 6600" no campo de pesquisa
search_box = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div/div[3]/div/div/div[1]/input").send_keys("RX 6600")

time.sleep(1)

#identifica o botão pesquisar e simula o click
search_button = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div/div[3]/div/div/div[1]/button").click()

time.sleep(5)

#filtra o produto pelo "menor preço"
drop_down = Select(driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div[1]/div/div/div/div[2]/select"))
drop_down.select_by_value("price_asc")

time.sleep(5)

#seleciona o primeiro produto
buy = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div[2]/div/div/article[1]/span/a").click()