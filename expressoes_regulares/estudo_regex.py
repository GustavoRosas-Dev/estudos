'''
Criar regex que:

1. valida CPF 
2. vaida data
3. Substitui/reorganiza a data
4. Localiza padrão dentro de texto
'''

import re

# Dados
cpf_tipo_1 = '123.456.789-00'
cpf_tipo_2 = ' 123.456.789-00'
cpf_tipo_3 = 'abc123.456.789-00def'
email_tipo_1 = 'gustavo@gmail.com'
telefone_tipo_1 = '(11) 91234-5678'
cep_tipo_1 = '01234-010'
variavel_tipo_1 = 'snake_case '
log_tipo_1 = '1993-05-14 12:35:28 [INFO] Mensagem do log'
filtrar_url_tipo_1 = 'https://chat.openai.com/c/2ff015d6-2455-4db2-b22e-760c48055675'
validar_cartao_de_credito_tipo_1 = '374245455400126'

# Patterns
validacao_de_cpf = re.compile(pattern=r'\d{3}\.\d{3}\.\d{3}\-\d{2}')
validacao_de_email = re.compile(pattern=r'^[a-zA-Z0-9._%+-]{3,7}@gmail.com')  # abc@gmail.com ou abcdefg@gmail.com
extracao_de_numeros_de_telefone = re.compile(pattern=r'\([1-9]{2}\)[ ][1-9]{4,5}[-][0-9]{4}')  # (11) 91234-5678
validacao_de_cep = re.compile(pattern=r'[0-9]{5}[-][0-9]{3}')  # (11) 91234-5678
validacao_de_variavel = re.compile(pattern=r'^\w+\s$') # snake_cases
analise_de_logs = re.compile(pattern=r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \[INFO\] .*$')
filtrar_url_em_texto = re.compile(pattern=r'https://\S+')

'''
Validação de Números de Cartão de Crédito:

Expressão Regular: \b(?:\d[ -]*?){13,16}\b
Isso pode ser usado para validar números de cartão de crédito, permitindo diferentes formatos e espaços em branco entre os dígitos.
Extração de Tags HTML:

Expressão Regular: <[^>]+>
Isso pode ser usado para extrair tags HTML de um documento, tornando útil para análise de conteúdo da web.
Validação de Senhas Fortes:

Expressão Regular: ^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}
Isso pode ser usado para validar senhas fortes, exigindo pelo menos uma letra maiúscula, uma letra minúscula, um dígito e um caractere especial.
Extração de Endereços de IP:

Expressão Regular: \b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b
Isso pode ser usado para extrair endereços de IP de um texto maior.
'''

# Escolha
padrao_escolhido = filtrar_url_em_texto  # Escolha aqui o padrão validador

# Ação
buscar = padrao_escolhido.search(filtrar_url_tipo_1)

if buscar:
    print(buscar.group())
else:
    print('Não encontrado!')

