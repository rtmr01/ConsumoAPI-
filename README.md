# Desafio de Consumo de API - Ray Consulting
## Código python
O código utiliza a biblioteca googleapiclient e uma chave API do YouTube para consumir dados da playlist
[fórmula 1](https://www.youtube.com/playlist?list=PLfoNZDHitwjUv0pjTwlV1vzaE0r7UDVDR). O script gera uma planilha com
o número de visualizações, comentários, likes, descrição, título, id do vídeo, data de publicação, duração e palavras-chaves.

## Desafios Enfrentados na construção do código

**Entender como cadastrar uma chave API Google** além da criação do projeto
**Entender os comandos e endpoints** para requisitar os dados corretos e específicos de playlists e dos vídeos


## Como Rodar o Código?

Siga os passos abaixo para configurar o ambiente:

1. **Faça um fork ou clone do repositório**:
   - Acesse o repositório no GitHub: [DesafioRay](https://github.com/rtmr01/DesafioRay)
   - ```bash
     git clone https://github.com/rtmr01/DesafioRay
     ```

2. **Instale o Python 3**:
   - Certifique-se de ter a versão 3 do Python instalada.
     ```bash
     python --version

     ```

3. **Crie um ambiente virtual**:
   - No terminal, navegue até o diretório do projeto clonado e execute o seguinte comando:
     ```bash
     python -m venv venv
     ```
   - Ative o ambiente virtual:
     ```bash
     venv\Scripts\activate
     ```

4. **Instale as bibliotecas do Google**:
   - No terminal, execute os seguintes comandos:
     ```bash
     pip install -r requirements.txt
     ```

5. **Rode o código**:
   - No terminal, execute:
     ```bash
     python main.py
     ```


## Construção do Dashboard

O dashboard interativo foi construído com as seguintes ferramentas:

- **PowerBI**: Para visualização dos dados, alimentado pela planilha gerada pelo código em Python no dia 09/12/2024.
- **Figma**: Usado para estilizar o layout e a interface de usuário (UI).

### Desafios na Construção

O maior desafio na construção do dashboard foi a **transformação de dados**. Alguns obstáculos que surgiram:

- **Identificação de pilotos mais mencionados**: Foi necessário tratar a coluna de descrição,criando uma cópia e eliminando todas os caracteres (exceto o sobrenome dos pilotos) para criar uma lista integrada com os demais gráficos do dashboard.

- **Conversão de dados**: Alguns dados eram gerados como "strings", o que exigiu a conversão para números inteiros na planilha para que pudessem ser corretamente analisados.
  
- **Criação do exibidor de duração**: Os dados de duração do vídeo eram recebidos em dias (D:HH:MM:SS), foi necessário adcionar uma fórmula que multiplica por 86400 os dias porque um dia tem exatamente 86.400 segundos (24 horas x 60 minutos x 60 segundos).
Assim, transformamos a fração de dia em um número de segundos. Por exemplo, 0,000694 x 86400 vira algo como 60 segundos.
Subtrai 1 segundo para corrigir um erro de arredondamento da API e do YouTube.


- Dashboard disponível em [Dashboard](https://app.powerbi.com/view?r=eyJrIjoiNzBmM2IxZGQtNGZkNi00ZDk3LTliYTUtMzAwMWJhMGYwNTU1IiwidCI6ImUyZjc3ZDAwLTAxNjMtNGNmNi05MmIwLTQ4NGJhZmY5ZGY3ZCJ9&pageName=af9a926c575b387b4403)

