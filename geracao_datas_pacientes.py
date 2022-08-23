########################################## PACOTES
import pandas as pd
from random import randint



########################################## GERAÇÃO DOS DADOS
df = pd.read_csv('D:/programming/Untitled Folder/pacientes.csv', encoding='utf-8', sep=';')

data = list()

for dado in range(2000):
    ano = str(randint(1930, 2015))
    mes = str(randint(1, 12))
    mes = '0' + mes if len(mes) < 2 else mes
    dia = str(randint(1,28)) if mes == 2 else str(randint(1,30))
    dia = '0' + dia if len(dia) < 2 else dia
    data.append(ano + mes + dia)
    
df['nascimento'] = data

df.to_csv('D:/programming/Untitled Folder/pacientes_atualizado.csv', encoding='utf-8', index=None, sep=';') 
