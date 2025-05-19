# aqui tem que fazer o import porque essas coisas estão definidas em outros arquivos.
import json
from artista import Artista
from obra import Obra

# Função para salvar dados em arquivo JSON
# Esse try e except é o tratamento de erro que o professor pede. 
def salvar_dados(artistas):
    try:
        with open("artistas.json", "w") as file:
            # Salvando os dados no formato JSON, convertendo objetos Artista e Obra para dicionários
            artistas_data = {artista.nome: {
                'tipo_arte': artista.tipo_arte,
                'bio': artista.bio,
                'redes_sociais': artista.redes_sociais,
                'obras': [{'titulo': obra.titulo, 'descricao': obra.descricao, 'preco': obra.preco, 'categoria': obra.categoria} for obra in artista.obras]
            } for artista in artistas}
            json.dump(artistas_data, file, indent=4)
            print("Dados salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")



# Função para carregar dados
def carregar_dados():
    try:
        with open("artistas.json", "r") as file:
            artistas_data = json.load(file)
            artistas = []
            for nome, data in artistas_data.items():
                # Criando uma instância de Artista com os dados carregados do arquivo JSON
                artista = Artista(nome, data['tipo_arte'], data['bio'], data['redes_sociais'])
                for obra_data in data['obras']:
                    # Criando instâncias de Obra e associando à instância de Artista
                    obra = Obra(obra_data['titulo'], obra_data['descricao'], obra_data['preco'], obra_data['categoria'])
                    artista.adicionar_obra(obra)  # Adiciona a obra ao artista
                artistas.append(artista)
            print("Dados carregados com sucesso!")
            return artistas
    except FileNotFoundError:
        print("Arquivo de dados não encontrado. Criando novo arquivo.")
        return []