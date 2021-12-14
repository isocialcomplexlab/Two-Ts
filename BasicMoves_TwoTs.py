#!/usr/bin/python
# -*- coding: UTF-8 -*-

#######################################################
#                      TWO-TS
# Trabalho de Mestrado em Ciência da Computação da Universidade Federal do ABC (UFABC);
# Título do Trabalho: Two-Ts: Reprodução de Expressões Faciais em Cabeça Robótica com Tecnologia 3D;
# Discente: Tamires dos Santos;
# Orientador: Wagner Tanaka Botelho;
#
# Descrição: Movimentações básica da TWO-TS. 
#
# Princiapis referências: https://github.com/adafruit/Adafruit_Python_PCA9685/blob/master/examples/simpletest.py
# 
# Data de Modificação: 12/05/2021
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

# Comprimento do Pulso 
minPulso = 650
maxPulso = 2350

def definirAngulo(angulo):
    larguraPulso = 0
    valorAnalogico = 0
    larguraPulso = (angulo - 0)*(maxPulso-minPulso)/180 +minPulso
    valorAnalogico = int(float(larguraPulso) / 1000000 * 50 * 4096)
    return valorAnalogico


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
pwm.set_pwm(m13, 0, definirAngulo(180))


while True:
    print("1 - Cima")
    print("2 - Baixo")
    print("3 - Esquerda")
    print("4 - Direita")
    print("5 - Rotação para direita")
    print("6 - Rotação para esquerda")
    print("7 - Maxilar")
    print("8 - Sorriso")
    print("9 - Sobrancelha esquerda")
    print("10 - Sobrancelha direita")
    print("11 - Olhos para esquerda")
    print("12 - Olhos para direita")
    print("13 - Piscar olho esquerdo")
    print("14 - Piscar olho direito")
    print("15 - Sorriso triste")
    
    opcao = input()
    time.sleep(2)

    if opcao == '1':
        pwm.set_pwm(m1, 0, definirAngulo(50))
        pwm.set_pwm(m2, 0, definirAngulo(70))
        time.sleep(1)
        pwm.set_pwm(m1, 0, definirAngulo(10))
        pwm.set_pwm(m2, 0, definirAngulo(120))
        time.sleep(1)
        pwm.set_pwm(m1, 0, definirAngulo(50))
        pwm.set_pwm(m2, 0, definirAngulo(70))
        time.sleep(1)

    elif opcao == '2':
        pwm.set_pwm(m1, 0, definirAngulo(50))
        pwm.set_pwm(m2, 0, definirAngulo(70))
        time.sleep(1)
        pwm.set_pwm(m1, 0, definirAngulo(90))
        pwm.set_pwm(m2, 0, definirAngulo(20))
        time.sleep(1)
        pwm.set_pwm(m1, 0, definirAngulo(50))
        pwm.set_pwm(m2, 0, definirAngulo(70))
        time.sleep(1)

    elif opcao == '3':
        pwm.set_pwm(m1, 0, definirAngulo(50))
        pwm.set_pwm(m2, 0, definirAngulo(70))
        time.sleep(1)
        pwm.set_pwm(m1, 0, definirAngulo(10))
        pwm.set_pwm(m2, 0, definirAngulo(20))
        time.sleep(1)
        pwm.set_pwm(m1, 0, definirAngulo(50))
        pwm.set_pwm(m2, 0, definirAngulo(70))
        time.sleep(1)

    elif opcao == '4':
        pwm.set_pwm(m1, 0, definirAngulo(50))
        pwm.set_pwm(m2, 0, definirAngulo(70))
        time.sleep(1)
        pwm.set_pwm(m1, 0, definirAngulo(100))
        pwm.set_pwm(m2, 0, definirAngulo(120))
        time.sleep(1)
        pwm.set_pwm(m1, 0, definirAngulo(50))
        pwm.set_pwm(m2, 0, definirAngulo(70))
        time.sleep(1)

    elif opcao == '5':
        pwm.set_pwm(m0, 0, definirAngulo(100))
        time.sleep(1)
        pwm.set_pwm(m0, 0, definirAngulo(70))
        time.sleep(1)
        pwm.set_pwm(m0, 0, definirAngulo(100))
        time.sleep(1)

    elif opcao == '6':
        pwm.set_pwm(m0, 0, definirAngulo(100))
        time.sleep(1)
        pwm.set_pwm(m0, 0, definirAngulo(130))
        time.sleep(1)
        pwm.set_pwm(m0, 0, definirAngulo(100))
        time.sleep(1)
        
    elif opcao == '7':
        pwm.set_pwm(m3, 0, definirAngulo(0))
        time.sleep(1)
        pwm.set_pwm(m3, 0, definirAngulo(90))
        time.sleep(1)
        pwm.set_pwm(m3, 0, definirAngulo(0))
        time.sleep(1)
        
    elif opcao == '8':
        pwm.set_pwm(m4, 0, definirAngulo(100))
        pwm.set_pwm(m5, 0, definirAngulo(90))
        time.sleep(1)
        pwm.set_pwm(m4, 0, definirAngulo(10))
        pwm.set_pwm(m5, 0, definirAngulo(180))
        time.sleep(1)
        pwm.set_pwm(m4, 0, definirAngulo(100))
        pwm.set_pwm(m5, 0, definirAngulo(90))
        time.sleep(1)
        
    elif opcao == '9':
        pwm.set_pwm(m6, 0, definirAngulo(130))
        time.sleep(1)
        pwm.set_pwm(m6, 0, definirAngulo(110))
        time.sleep(1)
        pwm.set_pwm(m6, 0, definirAngulo(130))
        time.sleep(1)
        pwm.set_pwm(m6, 0, definirAngulo(150))
        time.sleep(1)
        pwm.set_pwm(m6, 0, definirAngulo(130))
        time.sleep(1)
        
    elif opcao == '10':
        pwm.set_pwm(m7, 0, definirAngulo(50))
        time.sleep(1)
        pwm.set_pwm(m7, 0, definirAngulo(80))
        time.sleep(1)
        pwm.set_pwm(m7, 0, definirAngulo(50))
        time.sleep(1)
        pwm.set_pwm(m7, 0, definirAngulo(20))
        time.sleep(1)
        pwm.set_pwm(m7, 0, definirAngulo(50))
        time.sleep(1)
        
    elif opcao == '11':
        pwm.set_pwm(m8, 0, definirAngulo(90))
        pwm.set_pwm(m9, 0, definirAngulo(90))
        time.sleep(1)
        pwm.set_pwm(m8, 0, definirAngulo(60))
        pwm.set_pwm(m9, 0, definirAngulo(60))
        time.sleep(1)
        pwm.set_pwm(m8, 0, definirAngulo(90))
        pwm.set_pwm(m9, 0, definirAngulo(90))
        time.sleep(1)
        
    elif opcao == '12':
        pwm.set_pwm(m8, 0, definirAngulo(90))
        pwm.set_pwm(m9, 0, definirAngulo(90))
        time.sleep(1)
        pwm.set_pwm(m8, 0, definirAngulo(120))
        pwm.set_pwm(m9, 0, definirAngulo(120))
        time.sleep(1)
        pwm.set_pwm(m8, 0, definirAngulo(90))
        pwm.set_pwm(m9, 0, definirAngulo(90))
        time.sleep(1)
        
    elif opcao == '13':
        pwm.set_pwm(m10, 0, definirAngulo(20))
        time.sleep(1)
        pwm.set_pwm(m10, 0, definirAngulo(100))
        time.sleep(1)
        pwm.set_pwm(m10, 0, definirAngulo(20))
        time.sleep(1)
    
    elif opcao == '14':
        pwm.set_pwm(m11, 0, definirAngulo(120))
        time.sleep(1)
        pwm.set_pwm(m11, 0, definirAngulo(70))
        time.sleep(1)
        pwm.set_pwm(m11, 0, definirAngulo(120))
        time.sleep(1)
    
    elif opcao == '15':
        pwm.set_pwm(m12, 0, definirAngulo(90))
        pwm.set_pwm(m13, 0, definirAngulo(180))
        time.sleep(1)
        pwm.set_pwm(m12, 0, definirAngulo(180))
        pwm.set_pwm(m13, 0, definirAngulo(90))
        time.sleep(1)
        pwm.set_pwm(m12, 0, definirAngulo(90))
        pwm.set_pwm(m13, 0, definirAngulo(180))
        time.sleep(1)
        
