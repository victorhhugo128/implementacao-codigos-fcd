def clock(ciclos: int) -> None:
    parte_cima = "\t"
    parte_meio = "\t"
    parte_baixo = "\t"
    high = " __"
    low = "   "
    for ciclo in range(ciclos):
        parte_cima += high + low
        parte_meio += "|" + "  |  "
        parte_baixo += "|  |__"       
    print(parte_cima)
    print(parte_meio)
    print(parte_baixo)
    
def informacao(bits: str) -> None:
    parte_cima = "\t"
    parte_meio = "\t"
    parte_baixo = "\t"
    for ciclo in range(len(bits)):
        if bits[ciclo] == "0":
            if bits[ciclo - 1] == "0" and ciclo != 0:
                parte_cima += "      "  
                parte_meio += "      "
                parte_baixo += " _____"
                continue
            parte_cima += "      "
            parte_meio += "|     "
            parte_baixo += "|_____"
        elif bits[ciclo] == "1":
            if bits[ciclo - 1] == "1" and ciclo != 0:
                parte_cima += " _____"
                parte_meio += "      "
                parte_baixo += "      "
                continue
            parte_cima += " _____"
            parte_meio += "|     "
            parte_baixo += "|     "
    print(parte_cima)
    print(parte_meio)
    print(parte_baixo)
    
    return 

def pseudoternary_display(bits: str) -> None:
    controle = True
    bits_pseudoternary = ""
    for bit in bits:
        if bit == "1":
            bits_pseudoternary += "0"
        else:
            if controle:
                bits_pseudoternary += "+"
                controle = False
            else:
                bits_pseudoternary += "-"
                controle = True
    
    parte_meio = "\t"
    parte_positiva1 = "\t"
    parte_positiva2 = "\t"
    parte_negativa1 = "\t"
    parte_negativa2 = "\t"
    
    for ciclo in range(len(bits_pseudoternary)):
        if bits_pseudoternary[ciclo] == "0":
            if ciclo == 0 or bits_pseudoternary[ciclo - 1] == "0":
                parte_positiva2 += "      "
                parte_positiva1 += "      "
                parte_meio += " _____"
                parte_negativa1 += "      "
                parte_negativa2 += "      "
                continue
            if bits_pseudoternary[ciclo - 1] == "+":
                parte_positiva2 += "      "
                parte_positiva1 += "|     "
                parte_meio += "|_____"
                parte_negativa1 += "      "
                parte_negativa2 += "      "
                continue
            elif bits_pseudoternary[ciclo - 1] == "-":
                parte_positiva2 += "      "
                parte_positiva1 += "      "
                parte_meio += " _____"
                parte_negativa1 += "|     "
                parte_negativa2 += "|     "
                continue
        elif bits_pseudoternary[ciclo] == "+":
            if ciclo == 0 or bits_pseudoternary[ciclo - 1] == "+":
                parte_positiva2 += " _____"
                parte_positiva1 += "      "
                parte_meio += "      "
                parte_negativa1 += "      "
                parte_negativa2 += "      "
                continue
            if bits_pseudoternary[ciclo - 1] == "0":
                parte_positiva2 += " _____"
                parte_positiva1 += "|     "
                parte_meio += "|     "
                parte_negativa1 += "      "
                parte_negativa2 += "      "
                continue
            elif bits_pseudoternary[ciclo - 1] == "-":
                parte_positiva2 += " _____"
                parte_positiva1 += "|     "
                parte_meio += "|     "
                parte_negativa1 += "|     "
                parte_negativa2 += "|     "
                continue
        elif bits_pseudoternary[ciclo] == "-":
            if ciclo == 0 or bits_pseudoternary[ciclo - 1] == "-":
                parte_positiva2 += "      "
                parte_positiva1 += "      "
                parte_meio += "      "
                parte_negativa1 += "      "
                parte_negativa2 += " _____"
                continue
            if bits_pseudoternary[ciclo - 1] == "0":
                parte_positiva2 += "      "
                parte_positiva1 += "      "
                parte_meio += "      "
                parte_negativa1 += "|     "
                parte_negativa2 += "|_____"
                continue
            elif bits_pseudoternary[ciclo - 1] == "+":
                parte_positiva2 += "      "
                parte_positiva1 += "|     "
                parte_meio += "|     "
                parte_negativa1 += "|     "
                parte_negativa2 += "|_____"
                continue
                
    print(parte_positiva2)
    print(parte_positiva1)
    print(parte_meio)
    print(parte_negativa1)
    print(parte_negativa2)            
    
def manchester_code_display(bits: str) -> None:
    
    parte_meio = "\t"
    parte_positiva1 = "\t"
    parte_positiva2 = "\t"
    parte_negativa1 = "\t"
    parte_negativa2 = "\t"
    for ciclo in range(len(bits)):
        if bits[ciclo] == "0":
            if ciclo == 0 or bits[ciclo - 1] == "0":
                parte_positiva2 += "    __"
                parte_positiva1 += "|  |  "
                parte_meio += "|  |  "
                parte_negativa1 += "|  |  "
                parte_negativa2 += "|__|  "
                continue
            if bits[ciclo - 1] == "1":
                parte_positiva2 += "    __"
                parte_positiva1 += "   |  "
                parte_meio += "   |  "
                parte_negativa1 += "   |  "
                parte_negativa2 += " __|  "
                continue
        elif bits[ciclo] == "1":
            if ciclo == 0 or bits[ciclo - 1] == "1":
                parte_positiva2 += " __   "
                parte_positiva1 += "|  |  "
                parte_meio += "|  |  "
                parte_negativa1 += "|  |  "
                parte_negativa2 += "|  |__"
                continue
            if bits[ciclo - 1] == "0":
                parte_positiva2 += " __   "
                parte_positiva1 += "   |  "
                parte_meio += "   |  "
                parte_negativa1 += "   |  "
                parte_negativa2 += "   |__"
                continue
            
    print(parte_positiva2)
    print(parte_positiva1)
    print(parte_meio)
    print(parte_negativa1)
    print(parte_negativa2)      
    
def hdb3_code_display(bits: str) -> None:
    bits_hdb3 = ""
    bits_hdb3_display = ""
    impar = False
    alterna = False # True: próximo sinal 1 = -ve
    posicao = 0
    
    
    while posicao < len(bits):
        if bits[posicao: posicao + 4] == "0000" and posicao + 3 < len(bits):
            if impar:
                bits_hdb3 += "000V"
                if alterna:
                    bits_hdb3_display += "000+"
                else:
                    bits_hdb3_display += "000-"
            else:
                bits_hdb3 += "B00V"
                if alterna:
                    bits_hdb3_display += "-00-"
                    alterna = False
                else:
                    bits_hdb3_display += "+00+"
                    alterna = True
            impar = False
            posicao += 4
            continue
        if bits[posicao] == "0":
            bits_hdb3 += "0"
            bits_hdb3_display += "0"
        elif bits[posicao] == "1":
            if alterna:
                bits_hdb3 += "-"
                bits_hdb3_display += "-" 
                alterna = False
            else:
                bits_hdb3 += "+"
                bits_hdb3_display += "+" 
                alterna = True
            impar = not impar
        posicao += 1
    print(bits_hdb3)
    print(bits_hdb3_display)
    
    parte_meio = "\t"
    parte_positiva1 = "\t"
    parte_positiva2 = "\t"
    parte_negativa1 = "\t"
    parte_negativa2 = "\t"
    
    for ciclo in range(len(bits_hdb3_display)):
        if bits_hdb3_display[ciclo] == "0":
            if ciclo == 0 or bits_hdb3_display[ciclo - 1] == "0":
                parte_positiva2 += "      "
                parte_positiva1 += "      "
                parte_meio += " _____"
                parte_negativa1 += "      "
                parte_negativa2 += "      "
                continue
            if bits_hdb3_display[ciclo - 1] == "+":
                parte_positiva2 += "      "
                parte_positiva1 += "|     "
                parte_meio += "|_____"
                parte_negativa1 += "      "
                parte_negativa2 += "      "
                continue
            elif bits_hdb3_display[ciclo - 1] == "-":
                parte_positiva2 += "      "
                parte_positiva1 += "      "
                parte_meio += " _____"
                parte_negativa1 += "|     "
                parte_negativa2 += "|     "
                continue
        elif bits_hdb3_display[ciclo] == "+":
            if ciclo == 0 or bits_hdb3_display[ciclo - 1] == "+":
                parte_positiva2 += " _____"
                parte_positiva1 += "      "
                parte_meio += "      "
                parte_negativa1 += "      "
                parte_negativa2 += "      "
                continue
            if bits_hdb3_display[ciclo - 1] == "0":
                parte_positiva2 += " _____"
                parte_positiva1 += "|     "
                parte_meio += "|     "
                parte_negativa1 += "      "
                parte_negativa2 += "      "
                continue
            elif bits_hdb3_display[ciclo - 1] == "-":
                parte_positiva2 += " _____"
                parte_positiva1 += "|     "
                parte_meio += "|     "
                parte_negativa1 += "|     "
                parte_negativa2 += "|     "
                continue
        elif bits_hdb3_display[ciclo] == "-":
            if ciclo == 0 or bits_hdb3_display[ciclo - 1] == "-":
                parte_positiva2 += "      "
                parte_positiva1 += "      "
                parte_meio += "      "
                parte_negativa1 += "      "
                parte_negativa2 += " _____"
                continue
            if bits_hdb3_display[ciclo - 1] == "0":
                parte_positiva2 += "      "
                parte_positiva1 += "      "
                parte_meio += "      "
                parte_negativa1 += "|     "
                parte_negativa2 += "|_____"
                continue
            elif bits_hdb3_display[ciclo - 1] == "+":
                parte_positiva2 += "      "
                parte_positiva1 += "|     "
                parte_meio += "|     "
                parte_negativa1 += "|     "
                parte_negativa2 += "|_____"
                continue
            
    print(parte_positiva2)
    print(parte_positiva1)
    print(parte_meio)
    print(parte_negativa1)
    print(parte_negativa2)   
        

teste = "1110000000010100"

clock(len(teste))

informacao(teste)

pseudoternary_display(teste)

manchester_code_display(teste)

hdb3_code_display(teste)