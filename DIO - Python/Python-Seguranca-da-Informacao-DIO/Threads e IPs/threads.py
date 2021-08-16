from threading import Thread

def carro(velocidade):
	trajeto = 0
	while(trajeto < 100):
		print('O carro1: {}'.format(trajeto))
		trajeto += velocidade

t_carro1 = Thread(target=carro, args=[1])
t_carro2 = Thread(target=carro, args=[1.5])

t_carro1.start()
t_carro2.start()
