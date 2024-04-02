# passo a passo do projeto

# passo 1 - Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# pip install pyautogui (no terminal)
import pyautogui
import time

# clicar -> pyautogui.click
# escrever -> pyautogui.write
# apertar uma tecla -> pyautogui.press  
# apertar -> pyautogui.hotkeymarca
# scroll(rolar) -> pyautogui.scroll

pyautogui.PAUSE = 1.5
# aperta a tecla do windows
pyautogui.press("win")
# digita o nome do programa (chrome)
pyautogui.write("chrome")
time.sleep(3)
# aperta enter
pyautogui.press("enter")     

time.sleep(3)

# Digitar o link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# espera 5 segundos
time.sleep(3)

# passo 2 - Fazer login
pyautogui.click(x=3043, y=764)
pyautogui.write("freitag.andre@gmail.com")
# passar para o campo de senha
pyautogui.press("tab")
# digitar a senha
pyautogui.write("ktulu")

#time.sleep(3)
# clicar em logar
pyautogui.click(x=3395, y=963)
time.sleep(3)

# passo 3 - Importar a base de dados (comando para importar a base de dados pip install pandas numpy openpyxl)
import pandas #ferramenta que trabalha com base de dados
tabela = pandas.read_csv("produtos.csv")
#print("Column names in tabela:", tabela.columns)
print(tabela)

# passo 4 - cadastrar um produtoobs 
# para cada linha da minha tabela
for linha in tabela.index:
    # Se atingirmos o produto 5, interrompa o loop
    if linha >= 3:
        break
    # clicar no 1º campo
    pyautogui.click(x=3040, y=616)




    # extrair os dados da linha atual
    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = str(tabela.loc[linha, "categoria"])
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    custo = str(tabela.loc[linha, "custo"])
    obs = tabela.loc[linha, "obs"] if not pandas.isna(tabela.loc[linha, "obs"]) else ""

    # codigo do produto
    pyautogui.write(f"{codigo}\t{marca}\t{tipo}\t{categoria}\t{preco_unitario}\t{custo}\t{obs}\t", interval=0.1)
    """codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab") 
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")  
    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")"""    

    # enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)

"""pyautogui.hotkey('ctrl','a')  # Seleciona tudo (alternative method)
    pyautogui.hotkey('ctrl','x')  # Deleta os itens selecionados (alternative method)
    
    # Limpar os campos (use appropriate keyboard shortcuts or field clearing methods)
    #pyautogui.hotkey('ctrl', 'a')  # Select all
#pyautogui.press('delete')      # Delete the selected content"""
    
   