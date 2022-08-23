########################################## PACOTES
import pandas as pd
import random
import datetime
from datetime import timedelta


########################################## FUNÇÕES
## Geração de data aleatória
def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)
 
"""
PRECO de acordo com o tipo de atendimento realizado 
1 - Primeira Consulta - Cobra de $10 a $50
2 - Retorno - Cobra de $50 a $150
3 - Procedimento - Cobra de $150 a $5000
"""
def preco(row):
    if row['tipo'] == 1:
        return round(randint(10, 50), 2)
    elif row['tipo'] == 2:
        return round(randint(50, 150), 2)
    elif row['tipo'] == 3:
        return round(randint(150, 5000), 2)

########################################## GERAÇÃO DOS DADOS
## Geração de datas aleatórias com respeito ao mês de fevereiro
data = list()

for ano_itr in range(2):
    for mes_itr in range(12):
        for dia_itr in range(1000):
            ano = str(random.randint(2020, 2021))
            mes = str(random.randint(1, 12))
            mes = '0' + mes if len(mes) < 2 else mes
            dia = str(random.randint(1,28)) if mes == 2 else str(random.randint(1,30))
            dia = '0' + dia if len(dia) < 2 else dia
            data.append(ano + mes + dia)
            
            
## Criação da tabela 
df = {'id_antedimento': [5548712 + x for x in range(24000)] 
      , 'prioridade': [random.randint(1, 3) for x in range(24000)]
      , 'tipo': [random.randint(1, 3) for x in range(24000)] # tipo1: 10-40 min | tipo2: 30-130min | tipo3: 120-359
      , 'paciente': [random.randint(1, 2000) for x in range(6000)] 
                      + [random.randint(500, 1200) for x in range(6000)]
                      + [random.randint(700, 1000) for x in range(6000)]
                      + [random.randint(800, 2000) for x in range(6000)]
      , 'dentista': [random.randint(1, 500) for x in range(6000)] 
                      + [random.randint(430, 500) for x in range(6000)]
                      + [random.randint(1, 250) for x in range(6000)]
                      + [random.randint(120, 400) for x in range(6000)]
      , 'data': data
     }

# Observação: horário de funcionamento 8~18h

df = pd.DataFrame(df)

## Horário aleatório de início do atendimento, respeitando o horário de funcionamento da clínica
## Vale considerar que um procedimento não poderá extrapolar o horário de 23:59
d1 = datetime.datetime.strptime('1/1/1999 7:30 AM', '%m/%d/%Y %I:%M %p')
d2 = datetime.datetime.strptime('1/1/1999 6:00 PM', '%m/%d/%Y %I:%M %p')

df['inicio'] = [random_date(d1, d2) for _ in range(24000)]

"""
Delta do tempo, para duração do procedimento de acordo com a prioridade
1 - Baixa - Duração de 10 a 30 minutos
2 - Média - Duração de 20 a 120 minutos
3 - Alta - Duração de 110 a 359 minutos
"""
df['fim'] = ''
for linha in range(24000):
    if df.iloc[linha, 2] == 1:
        df.iloc[linha, 7] = df.iloc[linha, 6] + timedelta(minutes=random.randint(10, 30))
    elif df.iloc[linha, 2] == 2:
        df.iloc[linha, 7] = df.iloc[linha, 6] + timedelta(minutes=random.randint(20, 120))
    else:
        df.iloc[linha, 7] = df.iloc[linha, 6] + timedelta(minutes=random.randint(110, 359))


# AJUSTE TEMPO
df.inicio = df.inicio.astype('str').str.split(' ', 1, expand=True)[1]
df.fim = df.fim.astype('str').str.split(' ', 1, expand=True)[1]

# PRECO
df['fatura'] = df.apply(lambda row: preco(row), axis=1)


df.head()

# Export do documento
#df.to_csv('D:/programming/Untitled Folder/atendimento.csv', encoding='utf-8', index=None, sep=';')