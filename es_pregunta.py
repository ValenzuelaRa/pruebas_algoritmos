def es_pregunta(input_usuario):
    
   pronombres_interrogativos = ['quien', 'que', 'cual', 'cuales', 'cuanto', 'cuantos', 'cuanta', 'cuantas', 'cuando', 'donde', 'por que', 'como']
   
   adjetivos_interrogativos = ['que', 'cual', 'cuales', 'cuanto', 'cuantos', 'cuanta', 'cuántas']
   
   adverbios_interrogativos = ['donde', 'cuando', 'por que', 'como']
   
   particulas_interrogativas = ["no","acaso","verdad","a que","o no","no es cierto","no es verdad","no es asi"]
   
   input_usuario.lower()
   
   palabras = input_usuario.split()
   
   bandera = 0
   
   for palabra in palabras:
       
        if palabra in pronombres_interrogativos:
            print(f'Es pregunta: "{input_usuario}"\n\nContiene la palabra: "{palabra}"\n\nTipo de pregunta: "Pronombres interrogativos"')
            bandera = 1  
        
        elif palabra in adjetivos_interrogativos:
            print(f'Es pregunta: "{input_usuario}"\n\nContiene la palabra: "{palabra}"\n\nTipo de pregunta: "Adjetivos interrogativos"')
            bandera = 2
            
        elif palabra in adverbios_interrogativos:
            print(f'Es pregunta: "{input_usuario}"\n\nContiene la palabra: "{palabra}"\n\nTipo de pregunta: "Adverbios interrogativos"')
            bandera = 3
            
        elif palabra in particulas_interrogativas:
            print(f'Es pregunta: "{input_usuario}"\n\nContiene la palabra: "{palabra}"\n\nTipo de pregunta: "Particulas interrogativas"')
            bandera = 4
        return bandera

pregunta = es_pregunta("que puedo encontrar a mi perro")

print(pregunta)
   
   
   #hola mundo
   