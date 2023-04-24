times = ('Flamengo', 'Corinthians', 'Ceara', 'Fortalaza', 'Chapecoence', 'São Paulo')

print(f'Os 5 primeiros são: {times[0:5]}')
print(f'Os ultimos 4 colocados são: {times[2:]}')
print(f'Os times em ordem alfabetica são: {sorted(times)}')
print(f'O time da chapecoence está na posição {times.index("Chapecoence")+1}')