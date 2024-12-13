# Desafio de Consumo de API - Ray Consulting

<details>
<summary><strong>Código Python</strong></summary>

O código utiliza a biblioteca googleapiclient e uma chave API do YouTube para consumir dados da playlist [Formula 1](https://www.youtube.com/playlist?list=PLfoNZDHitwjUv0pjTwlV1vzaE0r7UDVDR). O script gera uma planilha com o número de visualizações, comentários, likes, descrição, título, id do vídeo, data de publicação, duração e palavras-chaves.

</details>

<details>
<summary><strong>Desafios Enfrentados na Construção do Código</strong></summary>

- **Entender como cadastrar uma chave API Google**, além da criação do projeto.
- **Entender os comandos e endpoints** para requisitar os dados corretos e específicos de playlists e dos vídeos.

</details>

<details>
<summary><strong>Como Rodar o Código?</strong></summary>

Siga os passos abaixo para configurar o ambiente:

1. **Faça um fork ou clone do repositório**:
   - Acesse o repositório no GitHub: [DesafioRay](https://github.com/rtmr01/DesafioRay)
   ```bash
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

</details>

<details>
<summary><strong>Construção do Dashboard</strong></summary>

**Dashboard disponível [aqui](https://app.powerbi.com/view?r=eyJrIjoiNzBmM2IxZGQtNGZkNi00ZDk3LTliYTUtMzAwMWJhMGYwNTU1IiwidCI6ImUyZjc3ZDAwLTAxNjMtNGNmNi05MmIwLTQ4NGJhZmY5ZGY3ZCJ9&pageName=af9a926c575b387b4403)**

O dashboard interativo foi construído com as seguintes ferramentas:

- **PowerBI**: Para visualização dos dados, alimentado pelo arquivo .csv gerada pelo código em Python no dia 09/12/2024 transformado em planilha **Excel**.
- **Figma**: Usado para estilizar o layout e a interface de usuário (UI).

### Desafios na Construção

O maior desafio na construção do dashboard foi a **transformação de dados**. Alguns obstáculos que surgiram:

- **Identificação de pilotos mais mencionados**: Foi necessário tratar a coluna de descrição, criando uma cópia e eliminando todos os caracteres (exceto o sobrenome dos pilotos) para criar uma lista integrada com os demais gráficos do dashboard.
- **Conversão de dados**: Alguns dados eram gerados como "strings", o que exigiu a conversão para números inteiros na planilha para que pudessem ser corretamente analisados.
- **Criação do exibidor de duração**: Os dados de duração do vídeo eram recebidos em dias (D:HH:MM:SS), foi necessário adicionar uma fórmula que multiplica por 86.400 os dias porque um dia tem exatamente 86.400 segundos (24 horas x 60 minutos x 60 segundos). Assim, transformamos a fração de dia em um número de segundos. Por exemplo, 0,000694 x 86400 vira algo como 60 segundos. Subtraí 1 segundo para corrigir um erro de arredondamento da API e do YouTube.

</details>

<details>
<summary><strong>Escolhas Técnicas</strong></summary>

- O código em **Python** retorna um arquivo CSV, um formato simples e amplamente compatível que pode ser aberto em formato **Excel** para visualização e manipulação de dados. Além disso, o formato CSV facilita a integração direta no Power BI, especialmente na aba de 'Transformar Dados', por sua simplicidade e eficiência. Essa escolha torna o código mais enxuto, enquanto permite flexibilidade para análise e uso em ferramentas populares como Excel e Power BI.
- A ferramenta de dashboard interativo escolhida foi o **Power BI** devido à sua ampla gama de possibilidades para criação de visualizações personalizadas, como a criação do gráfico de menções, integração eficiente com diversas fontes de dados, suporte a transformações avançadas por meio do Power Query e uma interface amigável que facilita a análise interativa. Além disso, o Power BI oferece recursos robustos para criação de relatórios dinâmicos, automação de atualizações de dados e compartilhamento de insights em diferentes plataformas.

</details>
