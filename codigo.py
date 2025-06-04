#importando bibliotecas necessárias
import pyautogui
import time
import pandas

# pyautogui.press -> aperta uma tecla
# pyautogui.click -> Clica em algum lugar
# pyautogui.write -> escrever um texto
# pyautogui.hotkey -> aperta uma combinação de teclas (ctl + c, ETC)
# pyautogui.position -> Diz a posição do seu mouse naquele momento

pyautogui.PAUSE = 0.5

# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Abrir o chrome
pyautogui.press("win")
pyautogui.write("Opera")
pyautogui.press("enter")

# Digitar o site 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# espera 3 segundos
time.sleep(3)

# Passo 2 : Fazer login
pyautogui.click(x=710, y=361)
# Digitar email
pyautogui.write("exemplo1@gmail.com")
# Digitar senha
pyautogui.press("tab")
pyautogui.write("Senhasupersecreta1")

# Entrar
pyautogui.press("tab")
pyautogui.press("enter")

# espera de 3s
time.sleep(2)

# Passo 3: Importar a base de dados usando pandas
tabela = pandas.read_csv("produtos.csv")

# Passo 4: Cadastrar a base de dados

for linha in tabela.index: #para cada linha da minha tabela

    pyautogui.click(x=707, y=259)

    codigo = str(tabela.loc[linha, "codigo"]) #.loc[linha, coluna] # strg = texto -> str()
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = str(tabela.loc[linha, "marca"]) # strg = texto -> str()
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo  = str(tabela.loc[linha, "tipo"]) # strg = texto -> str()
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"]) # strg = texto -> str()
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"]) # strg = texto -> str()
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"]) # strg = texto -> str()  
    pyautogui.write(custo)
    pyautogui.press("tab")   

    obs = str(tabela.loc[linha, "obs"]) # strg = texto -> str()
    if obs != "nan":
        pyautogui.write(obs)
    
    pyautogui.press("tab")

    #descer a página (poderia usar pyautogui.press("pgdn") tbm)
    pyautogui.scroll(-10000)
    pyautogui.press("enter")

    time.sleep(2)

    #subir a página (poderia usar pyautogui.press("pgup") tbm)
    pyautogui.scroll(10000)

# Passo 5 : Repetir para os outros produtos

# nan -> Not a number