# DESAFIO 11 - AULA 07 - CALCULO TINTA PARA PINTAR PAREDE.( 19.5m2 / 1l tinta)

alt = float(input('Digite a altura da Parede: '))
larg = float(input('Digite a largura da Parede: '))
area = larg * alt
tinta = area / 19.5
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m2.'.format(alt, larg, area))
print('Para pintar esse metros quadrados, voce precisará de {} litros de tintas'.format(tinta))
print('*** Atenção: Este é um cálculo próximo, mas varia entre marcas, qualidade da tinta e superfície onde será aplicada.***')