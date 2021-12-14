#!/usr/bin/python
# -*- coding: UTF-8 -*-

#######################################################
#                      TWO-TS
# Trabalho de Mestrado em Ciência da Computação da Universidade Federal do ABC (UFABC);
# Título do Trabalho: Two-Ts: Reprodução de Expressões Faciais em Cabeça Robótica com Tecnologia 3D;
# Discente: Tamires dos Santos;
# Orientador: Wagner Tanaka Botelho;
#
# Descrição:  Movimentos da TWO-TS virtual (Fusion 360).
#
# Princiapis referências: https://modthemachine.typepad.com/my_weblog/2016/08/drive-robot-arm-in-fusion.html
# 
# Data de Modificação: 27/05/2021
#######################################################

import adsk.core, adsk.fusion, adsk.cam, traceback
import math
import time

app = adsk.core.Application.get()
if app:
    ui = app.userInterface
    
# Variaveis 
handlers = [] #ref para os eventos
commandName = "Unidade de Acoes"

joint1Name = None
joint2Name = None
joint3Name = None
joint4Name = None
joint5Name = None
joint6Name = None
joint7Name = None
joint8Name = None
joint9Name = None
joint10Name = None
joint11Name = None

jointpalpebraInfEsqName = None
jointpalpebraSupEsqName = None
jointpalpebraInfDirName = None
jointpalpebraSupDirName = None

jointMaxilarName = None

jointSobEsqName = None
jointSobDirName  = None

bocaSupDirName = None
bocaSupEsqName = None
bocaInfDirName = None
bocaInfEsqName = None

joint1 = None
joint2 = None
joint3 = None
joint4 = None
joint5 = None
joint6 = None
joint7 = None
joint8 = None
joint9 = None
joint10 = None
joint11 = None

jointpalpebraInfEsq = None
jointpalpebraSupEsq = None
jointpalpebraInfDir = None
jointpalpebraSupDir = None

jointMaxilar = None

jointSobEsq = None
jointSobDir  = None

bocaSupDir = None
bocaSupEsq = None
bocaInfDir = None
bocaInfEsq = None

## UAs
ua51 = 0 #rotacao esquerda
ua52 = 0 #rotacao direita
ua53 = 0 #cima
ua54 = 0 #baixo
ua55 = 0 #cabecaEsquerda
ua56 = 0 #cabecaDireita

ua61 = 0 #olhos para esquerda
ua62 = 0 #olhos para direita

palpebraEsquerda = 0 
palpebraDireta = 0 


#emocoes
felicidade = 0
medo = 0 
raiva = 0
nojo = 0
surpresa = 0 
tristeza =0


def calculateJoint(value, signal, joint, position):
    if value >=position:
        for x in range(position,value):  
            revoluteJoint = adsk.fusion.RevoluteJointMotion.cast(joint.jointMotion)
            revoluteJoint.rotationValue = math.radians(x)* signal #em rad
            vp = app.activeViewport
            vp.refresh()
    else:
        for x in range(0,(position - value)): 
            revoluteJoint = adsk.fusion.RevoluteJointMotion.cast(joint.jointMotion)
            z = position -x
            revoluteJoint.rotationValue = math.radians(z)* signal #em rad
            vp = app.activeViewport
            vp.refresh()


# Definicao das funcoes de cada botao
class MyInputChangedHandler(adsk.core.InputChangedEventHandler):
    def __init__(self):
        super().__init__()

    def notify(self, args):
        eventArgs = adsk.core.InputChangedEventArgs.cast(args)
        commandInput = eventArgs.input
        
        global ua51, ua52, ua53, ua54, ua55, ua56, ua61, ua62
        
        global joint1, joint2, joint3, joint4, joint5, joint6, joint7, joint8, joint9, joint10, joint11
        
        global palpebraEsquerda, palpebraDireta, jointpalpebraInfEsq,  jointpalpebraSupEsq, jointpalpebraSupDir, jointpalpebraInfDir

        global jointMaxilar

        global jointSobEsq, jointSobDir

        global bocaSupDir, bocaSupEsq, bocaInfDir, bocaInfEsq

        global felicidade, medo, raiva, nojo, surpresa, tristeza
        

        if commandInput.id == commandName + '_51':
            ua51 = commandInput.value
            if ua51 == True:
                value = 15
                signal = 1
                position = 0
                calculateJoint(5, signal, joint1, position)

                app = adsk.core.Application.get()
                product = app.activeProduct
                design = adsk.fusion.Design.cast(product)
                root =design.rootComponent
                olho = root.occurrences.itemByName("Estrutura_olhos v34:1")
                trans = olho.transform
                ui.messageBox('Delay')
                rotx = adsk.core.Matrix3D.create()
                rotx.setToRotation(math.radians(-10),adsk.core.Vector3D.create(0,1,0), adsk.core.Point3D.create(trans.translation.x,trans.translation.y,trans.translation.z))
                trans.transformBy(rotx)
                olho.transform = trans
                calculateJoint(value, signal, joint1, 5)
                ui.messageBox("Delay")
                rotx = adsk.core.Matrix3D.create()
                rotx.setToRotation(math.radians(-10),adsk.core.Vector3D.create(0,1,0), adsk.core.Point3D.create(trans.translation.x,trans.translation.y,trans.translation.z))
                trans.transformBy(rotx)
                olho.transform = trans
                time.sleep(3)
                

        elif commandInput.id == commandName + '_52':
            ua52 = commandInput.value
            if ua52 == True:
                value = 15
                signal = -1
                position = 0
                calculateJoint(5, signal, joint1, position)
                # time.sleep(3)
                app = adsk.core.Application.get()
                product = app.activeProduct
                design = adsk.fusion.Design.cast(product)
                root =design.rootComponent
                olho = root.occurrences.itemByName("Estrutura_olhos v34:1")
                trans = olho.transform
                ui.messageBox('Delay')
                rotx = adsk.core.Matrix3D.create()
                rotx.setToRotation(math.radians(10),adsk.core.Vector3D.create(0,1,0), adsk.core.Point3D.create(trans.translation.x,trans.translation.y,trans.translation.z))
                trans.transformBy(rotx)
                olho.transform = trans
                calculateJoint(value, signal, joint1, 5)
                ui.messageBox("Delay")
                rotx = adsk.core.Matrix3D.create()
                rotx.setToRotation(math.radians(10),adsk.core.Vector3D.create(0,1,0), adsk.core.Point3D.create(trans.translation.x,trans.translation.y,trans.translation.z))
                trans.transformBy(rotx)
                olho.transform = trans
                time.sleep(3)


        elif commandInput.id == commandName + '_55':
            ua55 = commandInput.value
            if ua55 == True:
                value = 25
                signal = -1
                position = 0
                calculateJoint(value, signal, joint3, position)
                #time.sleep()
                value = 145
                signal = 1
                position = 170
                calculateJoint(value, signal, joint2, position)
                app = adsk.core.Application.get()
                product = app.activeProduct
                design = adsk.fusion.Design.cast(product)
                root =design.rootComponent
                olho = root.occurrences.itemByName("Estrutura_olhos v34:1")
                trans = olho.transform
                ui.messageBox('Delay')
                rotx = adsk.core.Matrix3D.create()
                rotx.setToRotation(math.radians(-8),adsk.core.Vector3D.create(0,0,1), adsk.core.Point3D.create(trans.translation.x,trans.translation.y,trans.translation.z))
                trans.transformBy(rotx)
                olho.transform = trans
                ui.messageBox("Delay")
                time.sleep(4)


        elif commandInput.id == commandName + '_56':
            ua56 = commandInput.value
            if ua56 == True:
                value = 25
                signal = -1
                position = 0
                calculateJoint(value, signal, joint5, position)
                value = -155
                signal = 1
                position = -180
                calculateJoint(value, signal, joint4, position)
                app = adsk.core.Application.get()
                product = app.activeProduct
                design = adsk.fusion.Design.cast(product)
                root =design.rootComponent
                olho = root.occurrences.itemByName("Estrutura_olhos v34:1")
                trans = olho.transform
                ui.messageBox('Delay')
                rotx = adsk.core.Matrix3D.create()
                rotx.setToRotation(math.radians(8),adsk.core.Vector3D.create(0,0,1), adsk.core.Point3D.create(trans.translation.x,trans.translation.y,trans.translation.z))
                trans.transformBy(rotx)
                olho.transform = trans
                ui.messageBox("Delay")
                time.sleep(4)

            
        elif commandInput.id == commandName + '_53':
            ua53 = commandInput.value
            if ua53 == True:
                value = 25
                signal = -1
                position = 0
                calculateJoint(value, signal, joint5, position)
                value = 25
                signal = -1
                position = 0
                calculateJoint(value, signal, joint3, position)
                value = 145
                signal = 1
                position = 170
                calculateJoint(value, signal, joint2, position)
                value = -155
                signal = 1
                position = -180
                calculateJoint(value, signal, joint4, position)
                app = adsk.core.Application.get()
                product = app.activeProduct
                design = adsk.fusion.Design.cast(product)
                root =design.rootComponent
                olho = root.occurrences.itemByName("Estrutura_olhos v34:1")
                trans = olho.transform
                ui.messageBox('Delay')
                rotx = adsk.core.Matrix3D.create()
                rotx.setToRotation(math.radians(-8),adsk.core.Vector3D.create(1,0,0), adsk.core.Point3D.create(trans.translation.x,trans.translation.y,trans.translation.z))
                trans.transformBy(rotx)
                olho.transform = trans
                ui.messageBox("Delay")
                time.sleep(4)
        
        elif commandInput.id == commandName + '_54':
            ua54 = commandInput.value
            if ua54 == True:
                value = 25
                signal = 1
                position = 0
                calculateJoint(value, signal, joint5, position)
                value = 25
                signal = 1
                position = 0
                calculateJoint(value, signal, joint3, position)
                value = 195
                signal = 1
                position = 170
                calculateJoint(value, signal, joint2, position)
                value = -155
                signal = -1
                position = -180
                calculateJoint(value, signal, joint4, position)
                app = adsk.core.Application.get()
                product = app.activeProduct
                design = adsk.fusion.Design.cast(product)
                root =design.rootComponent
                olho = root.occurrences.itemByName("Estrutura_olhos v34:1")
                trans = olho.transform
                ui.messageBox('Delay')
                rotx = adsk.core.Matrix3D.create()
                rotx.setToRotation(math.radians(8),adsk.core.Vector3D.create(1,0,0), adsk.core.Point3D.create(trans.translation.x,trans.translation.y,trans.translation.z))
                trans.transformBy(rotx)
                olho.transform = trans
                ui.messageBox("Delay")
                time.sleep(4)
        

        elif commandInput.id == commandName + '_61':
            ua61 = commandInput.value
            if ua61 == True:
                value = 5
                signal = -1
                position = 0
                calculateJoint(value, signal, joint8, position)
                value = 10
                signal = 1
                position = 0
                calculateJoint(value, signal, joint11, position)
                time.sleep(2)
                value = 20
                signal = -1
                position = 5
                calculateJoint(value, signal, joint8, position)
                time.sleep(4)
            

        elif commandInput.id == commandName + '_62':
            ua62 = commandInput.value
            if ua62 == True:
                value = 10
                signal = 1
                position = 0
                calculateJoint(value, signal, joint8, position)
                value = 10
                signal = -1
                position = 0
                calculateJoint(value, signal, joint11, position)
                time.sleep(2)
                value = 20
                signal = -1
                position = 10
                calculateJoint(value, signal, joint11, position)
                time.sleep(4)
        

        elif commandInput.id == commandName + '_palpebraEsq':
            palpebraEsquerda = commandInput.value
            if palpebraEsquerda == True:
                value = 30
                signal = 1
                position = 0
                calculateJoint(value, signal, jointpalpebraSupEsq, position)
                value = 30
                signal = 1
                position = 0
                calculateJoint(value, signal, jointpalpebraInfEsq, position)
                time.sleep(3)


        elif commandInput.id == commandName + '_palpebraDir':
            palpebraDireita = commandInput.value
            if palpebraDireita == True:
                value = 30
                signal = -1
                position = 0
                calculateJoint(value, signal, jointpalpebraSupDir, position)
                value = 25
                signal = -1
                position = 0
                calculateJoint(value, signal, jointpalpebraInfDir, position)
                time.sleep(3)

        
        elif commandInput.id == commandName + '_maxilar':
            maxilar = commandInput.value
            if maxilar == True:
                value = 5
                signal = -1
                position = 0
                calculateJoint(value, signal, jointMaxilar, position)
                time.sleep(8)
                value = 15
                signal = -1
                position = 0
                calculateJoint(value, signal, jointMaxilar, position)
                time.sleep(4)


        elif commandInput.id == commandName + '_sobDir':
            sobDir = commandInput.value
            if sobDir == True:
                value = 20
                signal = -1
                position = 0
                calculateJoint(value, signal, jointSobDir, position)
                time.sleep(3)


        elif commandInput.id == commandName + '_sobEsq':
            sobEsq = commandInput.value
            if sobEsq == True:
                value = 20
                signal = -1
                position = 0
                calculateJoint(value, signal, jointSobEsq, position)
                time.sleep(3)
        

        elif commandInput.id == commandName + '_sobs':
            sobs = commandInput.value
            if sobs == True:
                value = 10
                signal = -1
                position = 0
                calculateJoint(value, signal, jointSobDir, position)
                time.sleep(1)
                value = 10
                signal = -1
                position = 0
                calculateJoint(value, signal, jointSobEsq, position)
                time.sleep(4)
                

        elif commandInput.id == commandName + '_felicidade':
            felicidade = commandInput.value
            if felicidade == True:
                value = 15
                signal = 1
                position = 0
                calculateJoint(value, signal, jointpalpebraSupEsq, position)
                value = 15
                signal = 1
                position = 0
                calculateJoint(value, signal, jointpalpebraInfEsq, position)
                value = 15
                signal = -1
                position = 0
                calculateJoint(value, signal, jointpalpebraSupDir, position)
                value = 15
                signal = -1
                position = 0
                calculateJoint(value, signal, jointpalpebraInfDir, position)
                value = 20
                signal = -1
                position = 0
                calculateJoint(value, signal, bocaSupDir, position)
                value = 20
                signal = 1
                position = 0
                calculateJoint(value, signal, bocaSupEsq, position)
                value = 20
                signal = 1
                position = 0
                calculateJoint(value, signal, bocaInfDir, position)
                value = 20
                signal = -1
                position = 0
                calculateJoint(value, signal, bocaInfEsq, position)
                time.sleep(4)


        elif commandInput.id == commandName + '_medo':
            ui.messageBox("Delay")
            medo = commandInput.value
            if medo == True:
                value = 7
                signal = 1
                position = 0
                calculateJoint(value, signal, jointSobDir, position)
                time.sleep(1)
                value = 7
                signal = 1
                position = 0
                calculateJoint(value, signal, jointSobEsq, position)
                time.sleep(1)
                value = 20
                signal = 1
                position = 0
                calculateJoint(value, signal, jointpalpebraSupEsq, position)
                time.sleep(1)
                value = 20
                signal = 1
                position = 0
                calculateJoint(value, signal, jointpalpebraInfEsq, position)
                time.sleep(1)
                value = 20
                signal = -1
                position = 0
                calculateJoint(value, signal, jointpalpebraSupDir, position) 
                time.sleep(1)            
                value = 20
                signal = -1
                position = 0
                calculateJoint(value, signal, jointpalpebraInfDir, position)
                time.sleep(1)
                value = 5
                signal = -1
                position = 0
                calculateJoint(value, signal, jointMaxilar, position)
                time.sleep(1)
                value = 20
                signal = 1
                position = 0
                calculateJoint(value, signal, bocaInfDir, position)
                time.sleep(1)
                value = 20
                signal = -1
                position = 0
                calculateJoint(value, signal, bocaInfEsq, position)
                time.sleep(4)
                       

        elif commandInput.id == commandName + '_nojo':
            ui.messageBox("Delay")
            nojo = commandInput.value
            if nojo == True:
                value = 10
                signal = 1
                position = 0
                calculateJoint(value, signal, jointSobDir, position)
                time.sleep(1)
                value = 10
                signal = 1
                position = 0
                calculateJoint(value, signal, jointSobEsq, position)
                value = 20
                signal = -1
                position = 0
                calculateJoint(value, signal, bocaSupDir, position)
                value = 20
                signal = 1
                position = 0
                calculateJoint(value, signal, bocaSupEsq, position)
                time.sleep(4)


        elif commandInput.id == commandName + '_raiva':
            ui.messageBox("Delay")
            raiva= commandInput.value
            if raiva== True:
                value = 10
                signal = -1
                position = 0
                calculateJoint(value, signal, jointSobDir, position)
                time.sleep(1)
                value = 10
                signal = -1
                position = 0
                calculateJoint(value, signal, jointSobEsq, position)
                value = 20
                signal = 1
                position = 0
                calculateJoint(value, signal, jointpalpebraSupEsq, position)
                time.sleep(1)
                value = 20
                signal = 1
                position = 0
                calculateJoint(value, signal, jointpalpebraInfEsq, position)
                time.sleep(1)
                value = 20
                signal = -1
                position = 0
                calculateJoint(value, signal, jointpalpebraSupDir, position) 
                time.sleep(1)            
                value = 20
                signal = -1
                position = 0
                calculateJoint(value, signal, jointpalpebraInfDir, position)
                time.sleep(1)
                value = 20
                signal = 1
                position = 0
                calculateJoint(value, signal, bocaSupDir, position)
                value = 20
                signal = -1
                position = 0
                calculateJoint(value, signal, bocaSupEsq, position)
                value = 20
                signal = -1
                position = 0
                calculateJoint(value, signal, bocaInfDir, position)
                value = 20
                signal = 1
                position = 0
                calculateJoint(value, signal, bocaInfEsq, position)
                time.sleep(4)


        elif commandInput.id == commandName + '_surpresa':
            ui.messageBox("Delay")
            surpresa = commandInput.value
            if surpresa == True:
                value = 10
                signal = -1
                position = 0
                calculateJoint(value, signal, jointSobDir, position)
                time.sleep(1)
                value = 10
                signal = -1
                position = 0
                calculateJoint(value, signal, jointSobEsq, position)
                value = 5
                signal = -1
                position = 0
                calculateJoint(value, signal, jointMaxilar, position)
                value = 20
                signal = 1
                position = 0
                calculateJoint(value, signal, bocaInfDir, position)
                value = 20
                signal = -1
                position = 0
                calculateJoint(value, signal, bocaInfEsq, position)
                time.sleep(4)


        elif commandInput.id == commandName + '_tristeza':
            ui.messageBox("Delay")
            tristeza = commandInput.value
            if tristeza == True:
                value = 7
                signal = 1
                position = 0
                calculateJoint(value, signal, jointSobDir, position)
                time.sleep(1)
                value = 7
                signal = 1
                position = 0
                calculateJoint(value, signal, jointSobEsq, position)
                value = 20
                signal = -1
                position = 0
                calculateJoint(value, signal, bocaInfDir, position)
                value = 20
                signal = 1
                position = 0
                calculateJoint(value, signal, bocaInfEsq, position)
                time.sleep(4)

      

class MyExecutePreviewHandler(adsk.core.CommandEventHandler):
    def __init__(self):
        super().__init__()

    def notify(self, args):
        eventArgs = adsk.core.CommandEventArgs.cast(args)
        inputs = eventArgs.command.commandInputs
        eventArgs.isValidResult = True
        

# Criacao dos botoes
class MyCommandCreatedHandler(adsk.core.CommandCreatedEventHandler):    
    def __init__(self):
        super().__init__()        
    def notify(self, args):
        try:
            command = adsk.core.Command.cast(args.command)
        
            onInputChanged = MyInputChangedHandler()
            command.inputChanged.add(onInputChanged)
            handlers.append(onInputChanged)

            onExecutePreview = MyExecutePreviewHandler()
            command.executePreview.add(onExecutePreview)
            handlers.append(onExecutePreview)
        
            onDestroy = MyCommandDestroyHandler()
            command.destroy.add(onDestroy)
            handlers.append(onDestroy)
            
            inputs = command.commandInputs

            inputs.addBoolValueInput(commandName + '_51', 'UA 51', True, '', False) 
            inputs.addBoolValueInput(commandName + '_52', 'UA 52', True, '', False) 
            inputs.addBoolValueInput(commandName + '_53', 'UA 53', True, '', False) 
            inputs.addBoolValueInput(commandName + '_54', 'UA 54', True, '', False) 
            inputs.addBoolValueInput(commandName + '_55', 'UA 55', True, '', False) 
            inputs.addBoolValueInput(commandName + '_56', 'UA 56', True, '', False) 
            inputs.addBoolValueInput(commandName + '_61', 'UA 61', True, '', False)
            inputs.addBoolValueInput(commandName + '_62', 'UA 62', True, '', False) 
            inputs.addBoolValueInput(commandName + '_palpebraEsq', 'Palpebra Esquerda', True, '', False) 
            inputs.addBoolValueInput(commandName + '_palpebraDir', 'Palpebra Direita', True, '', False)
            inputs.addBoolValueInput(commandName + '_maxilar', 'Maxilar', True, '', False) 
            inputs.addBoolValueInput(commandName + '_sobDir', 'Sob. Direita', True, '', False)
            inputs.addBoolValueInput(commandName + '_sobEsq', 'Sob. Esquerda', True, '', False)
            inputs.addBoolValueInput(commandName + '_sobs', 'Sobrancelhas', True, '', False)

            inputs.addBoolValueInput(commandName + '_felicidade', 'Felicidade', True, '', False)
            inputs.addBoolValueInput(commandName + '_medo', 'medo', True, '', False)
            inputs.addBoolValueInput(commandName + '_nojo', 'nojo', True, '', False)
            inputs.addBoolValueInput(commandName + '_raiva', 'raiva', True, '', False)
            inputs.addBoolValueInput(commandName + '_surpresa', 'surpresa', True, '', False)
            inputs.addBoolValueInput(commandName + '_tristeza', 'tristeza', True, '', False)

            command.isAutoExecute = True
                
        except:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))              
            
            
class MyCommandDestroyHandler(adsk.core.CommandEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
            commandDefinitions = ui.commandDefinitions
            cmdDef = commandDefinitions.itemById(commandName)
            if cmdDef:
                cmdDef.deleteMe                
            adsk.terminate()
            
        except:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))        
            
            
def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        if not design:
            ui.messageBox('It is not supported in current workspace, please change to MODEL workspace and try again.')
            return
        
        global joint1, joint2, joint3, joint4, joint5, joint6, joint7, joint8, joint9, joint10, joint11
        
        global joint1Name, joint2Name, joint3Name, joint4Name, joint5Name, joint6Name, joint7Name, joint8Name, joint9Name
        global joint10Name, joint11Name
        global jointpalpebraInfEsq, jointpalpebraSupEsq, jointpalpebraInfEsqName, jointpalpebraSupEsqName
        global jointpalpebraInfDir, jointpalpebraSupDir, jointpalpebraInfDirName, jointpalpebraSupDirName
        global jointMaxilar, jointMaxilarName
        global jointSobDir, jointSobEsq, jointSobDirName, jointSobEsqName
        global bocaSupDirName, bocaSupEsqName, bocaInfDirName, bocaInfEsqName
        global bocaSupDir, bocaSupEsq, bocaInfDir, bocaInfEsq

        root = design.rootComponent
######
        pescoco = root.occurrences.itemByName("Montagem_pescoco v14:1")

        joint1Name = pescoco.component.joints.itemByName("joint1")
        joint1 = joint1Name.createForAssemblyContext(pescoco)
        
        joint2Name= pescoco.component.joints.itemByName("joint2")
        joint2 = joint2Name.createForAssemblyContext(pescoco)
        
        joint3Name = pescoco.component.joints.itemByName("joint3")
        joint3 = joint3Name.createForAssemblyContext(pescoco)

        joint4Name = pescoco.component.joints.itemByName("joint4")
        joint4 = joint4Name.createForAssemblyContext(pescoco)

        joint5Name = pescoco.component.joints.itemByName("joint5")
        joint5 = joint5Name.createForAssemblyContext(pescoco)

######
        olho = root.occurrences.itemByName("Estrutura_olhos v34:1")

        joint6Name = olho.component.asBuiltJoints.itemByName("joint6")
        joint6 = joint6Name.createForAssemblyContext(olho)

        joint7Name = olho.component.joints.itemByName("joint7")
        joint7 = joint7Name.createForAssemblyContext(olho)

        joint8Name = olho.component.asBuiltJoints.itemByName("joint8")
        joint8 = joint8Name.createForAssemblyContext(olho)

        joint9Name = olho.component.asBuiltJoints.itemByName("joint9")
        joint9 = joint9Name.createForAssemblyContext(olho)

        joint10Name = olho.component.joints.itemByName("joint10")
        joint10 = joint10Name.createForAssemblyContext(olho)

        joint11Name = olho.component.joints.itemByName("joint12")
        joint11 = joint11Name.createForAssemblyContext(olho)

        jointpalpebraSupEsqName = olho.component.asBuiltJoints.itemByName("jointpalpebraSupEsq")
        jointpalpebraSupEsq = jointpalpebraSupEsqName.createForAssemblyContext(olho)

        jointpalpebraInfEsqName = olho.component.asBuiltJoints.itemByName("jointpalpebraInfEsq")
        jointpalpebraInfEsq = jointpalpebraInfEsqName.createForAssemblyContext(olho)

        jointpalpebraSupDirName = olho.component.asBuiltJoints.itemByName("jointpalpebraSupDir")
        jointpalpebraSupDir = jointpalpebraSupDirName.createForAssemblyContext(olho)

        jointpalpebraInfDirName = olho.component.asBuiltJoints.itemByName("jointpalpebraInfDir")
        jointpalpebraInfDir = jointpalpebraInfDirName.createForAssemblyContext(olho)

        jointMaxilarName = olho.component.asBuiltJoints.itemByName("maxilar")
        jointMaxilar = jointMaxilarName.createForAssemblyContext(olho)

        jointSobDirName = olho.component.joints.itemByName("sobDireita")
        jointSobDir = jointSobDirName.createForAssemblyContext(olho)

        jointSobEsqName = olho.component.asBuiltJoints.itemByName("sobEsq")
        jointSobEsq = jointSobEsqName.createForAssemblyContext(olho)

        bocaSupDirName = olho.component.asBuiltJoints.itemByName("labioSupDir")
        bocaSupDir = bocaSupDirName.createForAssemblyContext(olho)

        bocaSupEsqName = olho.component.asBuiltJoints.itemByName("labioSupEsq")
        bocaSupEsq = bocaSupEsqName.createForAssemblyContext(olho)
        
        bocaInfDirName = olho.component.joints.itemByName("labioInfDir")
        bocaInfDir = bocaInfDirName.createForAssemblyContext(olho)

        bocaInfEsqName = olho.component.joints.itemByName("labioInfEsq")
        bocaInfEsq = bocaInfEsqName.createForAssemblyContext(olho)


        commandDefinitions = ui.commandDefinitions
        cmdDef = commandDefinitions.itemById(commandName)
        if not cmdDef:
            cmdDef = commandDefinitions.addButtonDefinition(
                commandName, commandName, commandName, '') 

        onCommandCreated = MyCommandCreatedHandler()
        cmdDef.commandCreated.add(onCommandCreated)
        handlers.append(onCommandCreated)
        
        inputs = adsk.core.NamedValues.create()
        cmdDef.execute(inputs)

        adsk.autoTerminate(False)

    except:
        ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))