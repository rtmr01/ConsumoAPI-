# Desafio de Consumo de API - Ray Consulting

## Desafios Enfrentados

### Maior Desafio: 
**Entender como usar as novas ferramentas inéditas**, como as bibliotecas do Google.

## Lembretes Importantes

- **Vídeos com thumbnail de batida** têm mais visualizações.
  - Exemplos: *HungriaGP* e *MonacoGP*.

## Como Rodar o Código?

Siga os passos abaixo para configurar o ambiente:

1. **Baixe o Visual Studio Code**:
   - [Visual Studio Code](https://code.visualstudio.com/download)

2. **Instale o Python 3**:
   - Certifique-se de ter a versão 3 do Python instalada.

3. **Instale as bibliotecas do Google**:
   - No terminal, execute os seguintes comandos:
     ```bash
     pip install --upgrade google-api-python-client
     pip install --upgrade google-auth-oauthlib google-auth-httplib2
     ```

4. **Faça um fork ou clone do repositório**:
   - Acesse o repositório no GitHub: [DesafioRay](https://github.com/rtmr01/DesafioRay)

## Construção do Dashboard

O dashboard interativo foi construído com as seguintes ferramentas:

- **PowerBI**: Para visualização dos dados, alimentado pela planilha gerada pelo código em Python no dia 09/12/2024.
- **Figma**: Usado para estilizar o layout e a interface de usuário (UI).

### Desafios na Construção

O maior desafio na construção do dashboard foi a **transformação de dados**. Alguns obstáculos que surgiram:

- **Identificação de pilotos mais mencionados**: Foi necessário criar uma coluna extra para verificar os pilotos mais mencionados em cada descrição, impactando diretamente as estatísticas dos highlights gerados.
  
- **Conversão de dados**: Alguns dados eram gerados como "strings", o que exigiu a conversão para números inteiros na planilha para que pudessem ser corretamente analisados.
