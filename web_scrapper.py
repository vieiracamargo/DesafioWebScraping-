#importa as bibliotecas

from selenium import webdriver
from selenium.webdriver.common.by import By
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



