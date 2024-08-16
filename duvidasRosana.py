notas = [7.5, 8.0, 6.5, 9.0, 8.5]

# Como faço para calcular a média dessas notas?

# Soma
soma = sum(notas)

# Quantidade
quantidade = len(notas)

# Media
media = soma / quantidade

print(f"A media das notas e: {media: .2f}")

# Além disso, gostaria de saber como adicionar uma nova nota na lista e recalcular a média.

nova_nota = 7.0

# Append -> Acrescentar
notas.append(nova_nota)

# Soma
soma = sum(notas)

# Quantidade
quantidade = len(notas)

# Media
media = soma / quantidade

print(f"A media das notas e: {media: .2f}")