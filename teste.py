import re
import json

texto = '''headers: {'Content-Type': 'application/json'} | jsonData: ('{"usuario": "victor", "senha": "**************", "modeloNome": "preAprovacaoRevo", "modeloId": 32, "ambiente": "prod", "tomadoresInformacoes": [{"cpfcnpj": 10305306707, "proposta": 143741, "informacoes": {"valorFinanciado": 12000.0, "rendaInformada": 8000.0, "valorParcela": 299.0}}], "parametros": {"usuario": "creditomassa@moneyp.com.br", "senha": "***********", "codigoParametro": "CREDITO_MASSA", "chave": "91afb9ae-1144-42a0-b961-8655af99f64c", "consultaCompleta": 1, "dataBaseAno": 2024, "dataBaseMes": 1}, "logger_username": "revo", "operacao_id": 133696}')'''

match = re.search(r"jsonData:\s*\(\s*'(.+)'\s*\)", texto)
if match:
    json_data = match.group(1)
    data = json.loads(json_data)
    proposta = data['tomadoresInformacoes'][0]['proposta']
    print("Número da Proposta:", proposta)
