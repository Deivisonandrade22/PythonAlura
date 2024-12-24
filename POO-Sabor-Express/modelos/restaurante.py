class Restaurante:
    def _init_(self,nome,categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Rapida', 'Artesanal')

restaurantes = [restaurante_praca, restaurante_pizza]

print(vars(restaurante_praca))
print(vars(restaurante_pizza))

