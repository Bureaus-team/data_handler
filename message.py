import re

def format_json(input_json):
    # Remove quebras de linha e espaços extras
    input_json = re.sub(r'\s+', ' ', input_json)
    
    # Substituir aspas duplas duplicadas por aspas simples
    formatted_json = re.sub(r'""', r'"', input_json)
    
    # Ajustar a estrutura geral
    formatted_json = re.sub(r'"usuario"', r'"usuario"', formatted_json)
    formatted_json = re.sub(r'"senha"', r'"senha"', formatted_json)
    formatted_json = re.sub(r'"modeloNome"', r'"modeloNome"', formatted_json)
    formatted_json = re.sub(r'"modeloId"', r'"modeloId"', formatted_json)
    formatted_json = re.sub(r'"ambiente"', r'"ambiente"', formatted_json)
    formatted_json = re.sub(r'"tomadoresInformacoes"', r'"tomadoresInformacoes"', formatted_json)
    formatted_json = re.sub(r'"cpfcnpj"', r'"cpfcnpj"', formatted_json)
    formatted_json = re.sub(r'"proposta"', r'"proposta"', formatted_json)
    formatted_json = re.sub(r'"informacoes"', r'"informacoes"', formatted_json)
    formatted_json = re.sub(r'"valorFinanciado"', r'"valorFinanciado"', formatted_json)
    formatted_json = re.sub(r'"rendaInformada"', r'"rendaInformada"', formatted_json)
    formatted_json = re.sub(r'"valorParcela"', r'"valorParcela"', formatted_json)
    formatted_json = re.sub(r'"parametros"', r'"parametros"', formatted_json)
    formatted_json = re.sub(r'"codigoParametro"', r'"codigoParametro"', formatted_json)
    formatted_json = re.sub(r'"chave"', r'"chave"', formatted_json)
    formatted_json = re.sub(r'"consultaCompleta"', r'"consultaCompleta"', formatted_json)
    formatted_json = re.sub(r'"dataBaseAno"', r'"dataBaseAno"', formatted_json)
    formatted_json = re.sub(r'"dataBaseMes"', r'"dataBaseMes"', formatted_json)
    formatted_json = re.sub(r'"logger_username"', r'"logger_username"', formatted_json)
    formatted_json = re.sub(r'"operacao_id"', r'"operacao_id"', formatted_json)

    # Corrigir o jsonData
    formatted_json = re.sub(r'{\s*\"', r'{"', formatted_json)
    
    return formatted_json

# Exemplo de uso
input_json = '''"headers: {'Content-Type': 'application/json'} | jsonData: ('{""usuario"": ""victor"", ""senha"": ""**************"", ""modeloNome"": ""preAprovacaoRevo"", ""modeloId"": 32, ""ambiente"": ""prod"", ""tomadoresInformacoes"": [{""cpfcnpj"": 1260671470, ""proposta"": 206931, ""informacoes"": {""valorFinanciado"": 14847.48, ""rendaInformada"": 8000.0, ""valorParcela"": 373.34, ""prazo"": 72.0, ""estado_instalacao"": ""RN"", ""valor_conta_luz"": 700.0, ""tipoAnalise"": 1, ""celular"": ""(84) 98844-1002"", ""cep"": ""59.575-000"", ""email"": ""muciobarbosajr@hotmail.com""}}], ""parametros"": {""usuario"": ""creditomassa@moneyp.com.br"", ""senha"": ""***********"", ""codigoParametro"": ""CREDITO_MASSA"", ""chave"": ""91afb9ae-1144-42a0-b961-8655af99f64c"", ""consultaCompleta"": 1, ""dataBaseAno"": 2024, ""dataBaseMes"": 3}, ""logger_username"": ""revo"", ""operacao_id"": 196884}')"'''

formatted_json = format_json(input_json)
print(formatted_json)