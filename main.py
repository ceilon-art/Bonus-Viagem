import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACf91a0a47bb5cf68bcf861e4dc3aa5018"
# Your Auth Token from twilio.com/console
auth_token = "c93eca713fb7a7f0f4b4781e2c886531"
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas']
                                     > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas']
                                   > 55000, 'Vendas'].values[0]
        print(
            f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5511981753865",
            from_="+16673031341",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)


# Para cada arquivo:

# Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000

# Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor

# Caso não seja maior do que 55.000 não quero fazer nada
