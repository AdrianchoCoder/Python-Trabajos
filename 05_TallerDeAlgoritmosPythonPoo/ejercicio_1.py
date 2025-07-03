class Persona:
    contador_identificador = 1  

    def __init__(self, numero_documento="", nombre_completo="", edad_persona=0, genero='M', peso_kilogramos=0.0, altura_centimetros=0.0):
        self._numero_documento = numero_documento
        self._nombre_completo = nombre_completo
        self._edad_persona = edad_persona
        self._genero = self._validar_genero(genero)
        self._peso_kilogramos = peso_kilogramos
        self._altura_centimetros = altura_centimetros
        self._identificador_sistema = self._generar_identificador()

    @classmethod
    def crear_con_datos_basicos(cls, numero_documento, nombre_completo, edad_persona, genero):
        return cls(numero_documento, nombre_completo, edad_persona, genero)

    @classmethod
    def crear_por_defecto(cls):
        return cls()

    def _generar_identificador(self):
        identificador_actual = Persona.contador_identificador
        Persona.contador_identificador += 1
        return identificador_actual

    def _validar_genero(self, genero):
        if genero.upper() not in ['M', 'F']:
            return 'M'
        return genero.upper()

    def calcular_indice_masa_corporal(self):
        if self._altura_centimetros <= 0:
            return -1

        altura_metros = self._altura_centimetros / 100
        indice_masa_corporal = self._peso_kilogramos / (altura_metros ** 2)
        
        if indice_masa_corporal < 18.5:
            return -1
        elif 18.5 <= indice_masa_corporal <= 24.9:
            return 0
        elif 25.0 <= indice_masa_corporal <= 29.9:
            return 1
        elif 30.0 <= indice_masa_corporal <= 39.9:
            return 2
        else:
            return 3

    def es_mayor_de_edad(self):
        return self._edad_persona >= 18

    def mostrar_informacion_completa(self):
        texto_genero = "Masculino" if self._genero == 'M' else "Femenino"
        resultado_imc = self.calcular_indice_masa_corporal()
        categorias_peso = {
            -1: "Por debajo del peso",
            0: "Normal",
            1: "Con sobrepeso",
            2: "Obesidad",
            3: "Obesidad extrema o de alto riesgo"
        }
        categoria_peso_texto = categorias_peso.get(resultado_imc, "Desconocido")

        print(f"\nHola {self._nombre_completo}, tu código dentro del sistema es {self._identificador_sistema}.")
        print(f"Tu identificación es {self._numero_documento}. Tu edad es {self._edad_persona} años.")
        print(f"Tu género es {texto_genero}. Tu Peso es {self._peso_kilogramos} kg y tu Altura es {self._altura_centimetros} cm.")
        print(f"Al calcular tu IMC concluimos que tu peso está: {categoria_peso_texto}.")
        print("Mayor de edad:", "Sí" if self.es_mayor_de_edad() else "No")

    # Métodos setter
    def establecer_documento(self, nuevo_documento): 
        self._numero_documento = nuevo_documento
    
    def establecer_nombre(self, nuevo_nombre): 
        self._nombre_completo = nuevo_nombre
    
    def establecer_edad(self, nueva_edad): 
        self._edad_persona = nueva_edad
    
    def establecer_genero(self, nuevo_genero): 
        self._genero = self._validar_genero(nuevo_genero)
    
    def establecer_peso(self, nuevo_peso): 
        self._peso_kilogramos = nuevo_peso
    
    def establecer_altura(self, nueva_altura): 
        self._altura_centimetros = nueva_altura

    # Métodos getter
    def obtener_documento(self): 
        return self._numero_documento
    
    def obtener_nombre(self): 
        return self._nombre_completo
    
    def obtener_edad(self): 
        return self._edad_persona
    
    def obtener_genero(self): 
        return self._genero
    
    def obtener_peso(self): 
        return self._peso_kilogramos
    
    def obtener_altura(self): 
        return self._altura_centimetros


def solicitar_datos_persona_completa():
    numero_documento = input("Documento: ")
    nombre_completo = input("Nombre: ")
    edad_persona = int(input("Edad: "))
    genero = input("Sexo (M/F): ")
    peso_kilogramos = float(input("Peso (kg): "))
    altura_centimetros = float(input("Altura (cm): "))
    return Persona(numero_documento, nombre_completo, edad_persona, genero, peso_kilogramos, altura_centimetros)


def ejecutar_programa_principal():
    print("\n INGRESA DATOS PARA LA PRIMERA PERSONA ")
    primera_persona = solicitar_datos_persona_completa()

    print("\nSEGUNDA PERSONA")
    documento_segunda_persona = input("Documento: ")
    nombre_segunda_persona = input("Nombre: ")
    edad_segunda_persona = int(input("Edad: "))
    genero_segunda_persona = input("Sexo (M/F): ")
    segunda_persona = Persona.crear_con_datos_basicos(documento_segunda_persona, nombre_segunda_persona, edad_segunda_persona, genero_segunda_persona)

    print("\n TERCERA PERSONA ")
    tercera_persona = Persona.crear_por_defecto()
    tercera_persona.establecer_documento("123456")
    tercera_persona.establecer_nombre("Carlos Pérez")
    tercera_persona.establecer_edad(30)
    tercera_persona.establecer_genero("M")
    tercera_persona.establecer_peso(80)
    tercera_persona.establecer_altura(175)

    lista_personas = [primera_persona, segunda_persona, tercera_persona]
    for numero_persona, persona_actual in enumerate(lista_personas, 1):
        print(f"\n INFORMACIÓN DE LA PERSONA {numero_persona}")
        persona_actual.mostrar_informacion_completa()

    while True:
        respuesta_usuario = input("\n¿Deseas ingresar otra persona? (S/N): ").upper()
        if respuesta_usuario == 'S':
            nueva_persona = solicitar_datos_persona_completa()
            nueva_persona.mostrar_informacion_completa()
        else:
            print("Fin del programa.")
            break


if __name__ == "__main__":
    ejecutar_programa_principal()