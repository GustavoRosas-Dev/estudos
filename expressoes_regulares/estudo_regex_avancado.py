# Objetivo: extrair todas as informações dos registros de "Pedido recebido" (data, hora, ID do pedido e nome do cliente).

import re

texto = """
2023-09-15 14:30:45 [INFO] Pedido recebido: ID 12345, Cliente: João Silva
2023-09-15 14:32:10 [INFO] Pedido enviado: ID 12345, Status: Enviado
2023-09-15 14:35:20 [ERROR] Erro ao processar pedido: ID 12345, Mensagem: Falha no pagamento
2023-09-15 15:10:55 [INFO] Pedido recebido: ID 67890, Cliente: Maria Santos
2023-09-15 15:12:30 [INFO] Pedido enviado: ID 67890, Status: Enviado
"""

# Expressão regular para encontrar registros de "Pedido recebido"
padrao = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[INFO\] Pedido recebido: ID (\d+), Cliente: ([\w\s]+)'

# Encontrar todas as correspondências no texto
correspondencias = re.findall(padrao, texto)

# Imprimir as informações extraídas
for correspondencia in correspondencias:
    data_hora, id_pedido, nome_cliente = correspondencia
    print(f"Data/Hora: {data_hora}, ID do Pedido: {id_pedido}, Nome do Cliente: {nome_cliente}")
