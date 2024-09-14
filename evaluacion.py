# FUNCION PARA VALIDAR CONTRASEÑA
def validarPassword(password):
    isMayus=False
    isMinus= False
    isNumber=False
    isMayorOcho=False
    isEspecial=False
    # MAS DE OCHO CARACTERES
    if len(password)>= 8:
        isMayorOcho=True
    for letra in password:
        # VERIFICA MAYUSCULA
        if letra.isupper():
            isMayus=True
        # VERIFICA MINUSCULA
        if letra.islower():
            isMinus= True
        # VERIFICAR NUMEROS
        if letra.isdigit():
            isNumber=True
        # VERIFICA CARACTERES ESPECIALES
        if letra == '!' or letra == '@' or letra == '#' or letra == '$' or letra == '%' or letra == '^' or letra == '&' or letra == '*':
            isEspecial=True
    # VERIFICA SI SE CUMPLEN TODAS LAS CONDICIONES
    if not isMayus or not isMinus or not isNumber or not isMayorOcho or not isEspecial:
        print("CONTRASEÑA INVALIDA, INGRESE UN FORMATO CORRECTO")
        
    else:
        print("CONTRASEÑA VALIDA") 
        
    pass            

# PIDE LA CONTRASEÑA
passw = str(input("Por favor ingrese su contraseña: "))

# VALIDAR CONTRASÑEA
validarPassword(passw)

