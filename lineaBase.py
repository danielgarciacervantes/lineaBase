#! python3
#lineaBase.py - Pasa líneas base automáticamente
import pyautogui, time, pyperclip

#Lista de conjuntos

conjuntos = ['CBJ', 'CMN', 'CVP', 'CS3', 'CRÑ', 'CSI', 'USV', 'UNL', 'JUU', 'URC', 'USI', 'CR7', 'UFB', 'CFB', 'UR7']
#conjuntosNoUtilizados = ['UED', 'P2U', 'UB4', 'CB4', 'CHM']
APPROVED_COST = "Approved Cost Budget"

def lineaBase(org):
    #Dar tiempo para enfocar primer cuadro de formato
    time.sleep(5)
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.4

    #Loop según lista de conjuntos
    for conj in range(conjuntos.index(org), len(conjuntos)):
    #Escribir conjunto -> Tab -> "Ap" -> Tab -> C -> Click en ejecutar *2 -> Click en donde se pone el nombre
        pyperclip.copy(conjuntos[conj])
        pyautogui.hotkey("ctrl", "v")
        pyautogui.typewrite(['tab'])
        if conj == 0 or conj == conjuntos.index(org):
            pyperclip.copy(APPROVED_COST)
            pyautogui.hotkey("ctrl", "v")
        pyautogui.typewrite(['tab'])
        pyautogui.moveTo(533,542,0.2)
        pyautogui.click(clicks=2, interval=0.2)
        pyautogui.moveTo(225,135,0.2)
        pyautogui.click()

def main():
    org = input('Escribe la organización inicial: ').upper()
    if org == '':
        org = conjuntos[0]
    lineaBase(org)

if __name__ == '__main__':
    main()

#TO DO: Incluir abrir Oracle

#Esto busca los botones, pero tarda demasiado puto tiempo :(
#Opción viable: Detectar posiciones de los clicks una sola vez al inicio del script
'''#Lista de conjuntos

conjuntos = ['CBJ', 'CHM', 'CMN', 'CVP', 'CS3', 'CB4', 'CRÑ', 'CSI', 'UED', 'P2U', 'USV', 'UNL', 'JUU', 'URC', 'UB4', 'USI']
APPROVED_COST = "Approved Cost Budget"

#Dar tiempo para enfocar ventana
time.sleep(5)
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.1

#Loop sobre número de conjuntos:
for x in range(len(conjuntos)):
#Click en NroProyecto + 100 pixeles
    nroProyectoCoord = pyautogui.locateCenterOnScreen('nroProyecto.png')
    pyautogui.click(nroProyectoCoord[0] + 100 ,nroProyectoCoord[1])
#Si primer loop: Escribir conjunto -> Tab -> Approved cost budget -> Tab
    if x == 0:
        pyperclip.copy(conjuntos[x])
        pyautogui.hotkey("ctrl", "v")
        pyautogui.typewrite(['tab'])
        pyperclip.copy(APPROVED_COST)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.typewrite(['tab'])
#Otros loops: Escribir conjunto -> Tab -> Esperar -> Tab
    else:
        pyperclip.copy(conjuntos[x])
        pyautogui.hotkey("ctrl", "v")
        pyautogui.typewrite(['tab'])
        pyautogui.typewrite(['tab'])
#Si Ejecutar: Click en Ejecutar -> Click en Aplicar línea base
    while True:
        if pyautogui.locateCenterOnScreen('ejecutar.png') != None:
            pyautogui.click(pyautogui.locateCenterOnScreen('ejecutar.png'))
            while True:
                if pyautogui.locateCenterOnScreen('aplicarLineaAct.png') != None:
                    pyautogui.click(pyautogui.locateCenterOnScreen('aplicarLineaAct.png'))
                    break
            break
#Si Aplicar línea base (Desactivado) -> Continuar loop
        if pyautogui.locateCenterOnScreen('aplicarLineaDes.png') != None:
            break
#Repetir loop'''
