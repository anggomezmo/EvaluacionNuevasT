def validarPassword(password):
    isMayus=False
    isMinus= False
    isNumber=False
    isMayorOcho=False
    isEspecial=False
    if len(password)>= 8:
        isMayorOcho=True
    for letra in password:
        if letra.isupper():
            isMayus=True
        if letra.islower():
            isMinus= True
        if letra.isdigit():
            isNumber=True
        if letra == '!' or letra == '@' or letra == '#' or letra == '$' or letra == '%' or letra == '^' or letra == '&' or letra == '*':
            isEspecial=True
    
    if not isMayus or not isMinus or not isNumber or not isMayorOcho or not isEspecial:
        print("CONTRASEÑA INVALIDA, INGRESE UN FORMATO CORRECTO")
        
    else:
        print("CONTRASEÑA VALIDA") 
        
    pass            


passw = str(input("Por favor ingrese su contraseña: "))
validarPassword(passw)

