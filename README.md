# SatelliteScraper

Um Web Scraper criado para coletar informações de satélites no site [Heavens Above](https://www.heavens-above.com/Satellites.aspx). Os dados coletados incluem Nome, Estado Orbital, Designação e Órbita, sendo organizados e exportados em CSV, prontos para consulta depois.

## Tecnologias Utilizadas

- Python
- BeautifulSoup4
- pandas

## Instalação e Execução
Siga os passos abaixo para configurar e executar o projeto localmente.

### Pré-requisitos
Antes de iniciar, certifique-se de ter os seguintes itens instalados:

- [Python](https://www.python.org/downloads)

### 1. Clone o repositório:
```bash
git clone https://github.com/rafaelwnk/SatelliteScraper
cd SatelliteScraper
```

### 2. Crie e ative o ambiente virtual:
```bash
python -m venv venv
```
- No Windows:
```bash
venv\Scripts\activate
```
- No Linux/MacOS:
```bash
source venv/bin/activate
```

### 3. Instale as dependências:
```bash
pip install -r requirements.txt
```

### 4. Execute o projeto:
```bash
python main.py
```

## Contribuições

Se você tiver alguma sugestão de melhoria, ideia nova ou perceber algo que pode ser ajustado:

    1.Faça um fork do repositório

    2.Crie uma nova branch: git checkout -b feature

    3.Faça um commit: git commit -m 'feat: new feature'

    4.Faça o push para a branch : git push origin feature

    5.Abra um pull request