
#Classe que representa Pokémon
class Pokemon():
    def __init__(self, nome, vida, força):#Atributos do Pokémon
        self.nome = nome
        self.vida = vida
        self.força = força
        print(f"{self.nome} entrou na batalha!")#Mensagem ao entrar em batalha

    def atacar(self, inimigo):#Método para atacar outro Pokémon
        print(f"{self.nome} atacou {inimigo.nome}, causando {self.força} de dano.")
        inimigo.vida -= self.força
        print(f"{inimigo.nome} ficou com {inimigo.vida} de vida.\n")

# Classe que herda de Pokemon e tem ataque especial
class PokemonLendario(Pokemon):
    def ataque_especial(self, inimigo):
        print(f"{self.nome} usou ataque especial!")
        inimigo.vida -= 50
        print(f"{inimigo.nome} ficou com {inimigo.vida} de vida.\n")


#Criando Pokémons
pokemon1 = Pokemon("Pikachu", 210, 40)
print(f"com {pokemon1.vida} de vida.\n")

pokemon2 = PokemonLendario("Charmander", 200,50)
print(f"com {pokemon2.vida} de vida.\n")

#Rodando ataques
pokemon1.atacar(pokemon2)
pokemon2.atacar(pokemon1)
pokemon2.ataque_especial(pokemon1)