#!/usr/bin/python
# -*- coding: UTF-8 -*-

#######################################################
#                      TWO-TS
# Trabalho de Mestrado em Ciência da Computação da Universidade Federal do ABC (UFABC);
# Título do Trabalho: Two-Ts: Reprodução de Expressões Faciais em Cabeça Robótica com Tecnologia 3D;
# Discente: Tamires dos Santos;
# Orientador: Wagner Tanaka Botelho;
#
# Descrição: Emoções básicas e universais da TWO-TS. 
#
# Princiapis referências: https://github.com/adafruit/Adafruit_Python_PCA9685/blob/master/examples/simpletest.py
# 
# Data de Modificação: 13/05/2021
#######################################################

from __future__ import division
import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

#### Servomotores/Posições
# Pescoço
m0 = 0
m1 = 1
m2 = 2
# Maxilar
m3 = 3
# Boca
m4 = 4
m5 = 5
# Sobrancelhas
m6 = 6
m7 = 7
# Olhos
m8 = 8 #esquerdo
m9 = 9 #direito
# Palpebras
m10 = 10 #esquerda
m11 = 11 #direita
# Boca (triste)
m12 = 12 #esquerda
m13 = 13 #direita
#################

# Definição do Pulso 
minPulso = 650
maxPulso = 2350

def definirAngulo(angulo):
    larguraPulso = 0
    valorAnalogico = 0
    larguraPulso = (angulo - 0)*(maxPulso-minPulso)/180 +minPulso
    valorAnalogico = int(float(larguraPulso) / 1000000 * 50 * 4096)
    return valorAnalogico

def posicaoInicial():
    # Posicao inicial
    pwm.set_pwm(m0, 0, definirAngulo(100))
    pwm.set_pwm(m1, 0, definirAngulo(50))
    pwm.set_pwm(m2, 0, definirAngulo(70))
    pwm.set_pwm(m3, 0, definirAngulo(0))
    pwm.set_pwm(m4, 0, definirAngulo(100))
    pwm.set_pwm(m5, 0, definirAngulo(90))
    pwm.set_pwm(m6, 0, definirAngulo(130))
    pwm.set_pwm(m7, 0, definirAngulo(50))
    pwm.set_pwm(m8, 0, definirAngulo(90))
    pwm.set_pwm(m9, 0, definirAngulo(90))
    pwm.set_pwm(m10, 0, definirAngulo(20))
    pwm.set_pwm(m11, 0, definirAngulo(120))
    pwm.set_pwm(m12, 0, definirAngulo(90))
    pwm.set_pwm(m12, 0, definirAngulo(90))
    pwm.set_pwm(m13, 0, definirAngulo(180))


posicaoInicial()
while True:
    print("1 - Felicidade")
    print("2 - Medo")
    print("3 - Nojo")
    print("4 - Raiva")
    print("5 - Surpresa")
    print("6 - Tristeza")
    
    opcao = input()
    time.sleep(5)

    if opcao == '1': #felicidade
        #UA12
        pwm.set_pwm(m4, 0, definirAngulo(10))
        pwm.set_pwm(m5, 0, definirAngulo(180))
        #UA6
        pwm.set_pwm(m10, 0, definirAngulo(70))
        pwm.set_pwm(m11, 0, definirAngulo(90))
        time.sleep(5)

        #Posicao neutra dos servos 
        posicaoInicial()
        time.sleep(4)

    elif opcao == '2': #medo 
        #UA1
        pwm.set_pwm(m6, 0, definirAngulo(110))
        pwm.set_pwm(m7, 0, definirAngulo(80))

        #UA2  #conflito com UA1
        #UA4 #conflito com UA1
        #UA5 #conflito com UA7

        #UA7
        pwm.set_pwm(m10, 0, definirAngulo(60))
        pwm.set_pwm(m11, 0, definirAngulo(100))

        #UA20

        #UA26
        pwm.set_pwm(m3, 0, definirAngulo(80))

        time.sleep(5)
        #Posicao neutra dos servos 
        posicaoInicial()
        time.sleep(4)


    elif opcao == '3': #nojo
        #UA9 #seria a UA4
        pwm.set_pwm(m6, 0, definirAngulo(150))
        pwm.set_pwm(m7, 0, definirAngulo(20))

        #UA15
        pwm.set_pwm(m12, 0, definirAngulo(180))
        pwm.set_pwm(m13, 0, definirAngulo(90))

        time.sleep(5)
        #Posicao neutra dos servos 
        posicaoInicial()
        time.sleep(4)


    elif opcao == '4': #raiva
        #UA4
        pwm.set_pwm(m6, 0, definirAngulo(150))
        pwm.set_pwm(m7, 0, definirAngulo(20))

        #UA5 #conflito com UA7

        #UA7
        pwm.set_pwm(m10, 0, definirAngulo(60))
        pwm.set_pwm(m11, 0, definirAngulo(100))

        #UA23
        pwm.set_pwm(m12, 0, definirAngulo(180))
        pwm.set_pwm(m13, 0, definirAngulo(90))

        time.sleep(5)
        #Posicao neutra dos servos 
        posicaoInicial()
        time.sleep(4)

    elif opcao == '5': #surpresa
        #UA1
        pwm.set_pwm(m6, 0, definirAngulo(110))
        pwm.set_pwm(m7, 0, definirAngulo(80))

        #UA2  #conflito com UA1

        #UA5
        pwm.set_pwm(m10, 0, definirAngulo(40))
        pwm.set_pwm(m11, 0, definirAngulo(120))
        
        pwm.set_pwm(m3, 0, definirAngulo(50))

        time.sleep(5)
        #Posicao neutra dos servos 
        posicaoInicial()
        time.sleep(4)
    
    elif opcao == '6': #tristeza
        #UA1
        pwm.set_pwm(m6, 0, definirAngulo(110))
        pwm.set_pwm(m7, 0, definirAngulo(80))

        #UA4 #conflito com UA1

        #UA15
        pwm.set_pwm(m12, 0, definirAngulo(180))
        pwm.set_pwm(m13, 0, definirAngulo(90))

        time.sleep(5)
        #Posicao neutra dos servos 
        posicaoInicial()
        time.sleep(4)



    
