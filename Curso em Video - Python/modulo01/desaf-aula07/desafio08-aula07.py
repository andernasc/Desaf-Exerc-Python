# DESAFIO 08 - AULA 07 - CONVERSOR DE MEDIDAS
# dm > decimetro, cm > centimetro, mm > milimetro,
# dam > decâmetro, hm > hectômetro, km > quilômetro

medida = float(input('Digite uma distância em metros: '))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida / 10
hm = medida / 100
km = medida / 1000

print('A media  de  {}m corresponde a \n{:.0f} dm \n{:.0f} cm \n{:.0f} mm \n{} dam \n{} hm \n{} km'.format(medida, dm, cm, mm, dam, hm, km))
