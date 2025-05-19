# Importa artista porque vai usar o objeto
from artista import Artista

# Função para criar artista
# Aqui ele tenta criar um um Artista que foi definido em outra classe (artista.py), caso ele consiga ele retorna um objeto to tipo artista
# Se ele não conseguir ele manda um erro dizendo que não conseguiu.
def criar_artista(nome, tipo_arte, bio, redes_sociais):
    try:
        artista = Artista(nome, tipo_arte, bio, redes_sociais)
        print(f"Artista {nome} criado com sucesso!")
        return artista
    except Exception as e:
        print(f"Erro ao criar artista: {e}")