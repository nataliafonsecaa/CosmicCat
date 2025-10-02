🌌 Cosmic Cat
Durante a disciplina Linguagem de Programação Aplicada, desenvolvi um jogo 2D com Python e Pygame, chamado Cosmic Cat. Um jogo 2D feito em Python com Pygame, onde você controla um gatinho espacial chamado Nyan, que deve desviar de alienígenas coloridos para sobreviver no espaço sideral.

🎮 Como jogar
- Use as setas do teclado para mover o gatinho.
- Desvie dos alienígenas que caem da parte superior da tela.
- Sobreviva o tempo necessário para avançar de fase.
- Se atingir o limite de tempo da fase 2, você vence o jogo!
- Se colidir com um alien, é Game Over.

📂 Estrutura do projeto

CosmicCat/
│── assets/              # Imagens e sons do jogo

│   ├── Player1.png

│   ├── Enemy1.png

│   ├── Enemy2.png

│   ├── Enemy3.png

│   ├── Levelbg0.png

│   ├── 7481714.jpg

│   ├── Level1.wav

│   └── Level2.wav

│
│── src/                 # Código-fonte organizado

│   ├── game.py          # Lógica do jogo

│   ├── menu.py          # Menu inicial

│   ├── score.py         # Tela de score

│   ├── utils.py         # Funções auxiliares (carregar imagens, tocar música)

│   └── __init__.py

│

│── main.py              # Arquivo principal para rodar o jogo

│── requirements.txt     # Dependências do projeto


🚀 Como rodar
1. Clone este repositório
git clone https://github.com/nataliafonsecaa/CosmicCat.git
cd CosmicCat

2. Crie e ative um ambiente virtual (recomendado)
   
python -m venv venv

venv\Scripts\activate   # no Windows

source venv/bin/activate  # no Linux/Mac

3. Instale as dependências
pip install -r requirements.txt

4. Execute o jogo
python main.py

📦 Dependências

- Python 3.10+
- Pygame

No requirements.txt adicione:

pygame


