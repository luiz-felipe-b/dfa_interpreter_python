import json

# classe automato
class automato():
    def __init__(self, estados, sigma, delta, estado_inicial, estados_finais):
        self.estados = estados
        self.sigma = sigma
        self.delta = delta
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.aceita = False

    def demonstrar_trans(self, simbolo, estado_atual, proximo_estado):
        estado_atual = estado_atual.replace('q', '')
        proximo_estado = proximo_estado.replace('q', '')
        print(f"({estado_atual}, '{simbolo}') -> {proximo_estado}")

    # função de validar a cadeia
    def iniciar_valid(self, cadeia):
        self.aceita = False
        cadeia_lista = [str(x) for x in cadeia]
        estado_atual = self.estado_inicial
        for sim in cadeia_lista:
            for e in self.delta:
                if (sim == e["simbolo"]) and (estado_atual == e["estado_atual"]):
                    estado_atual = e["proximo_estado"]
                    self.demonstrar_trans(e["simbolo"], e["estado_atual"], e["proximo_estado"])
                    break
        if self.estados_finais.count(estado_atual) > 0:
            self.aceita = True
        else:
            self.aceita = False
        if self.aceita == True:
            print("A cadeia '" + str(cadeia) + "' foi aceita pelo autômato.")
        else:
            print("A cadeia '" + str(cadeia) + "' for rejeitada pelo autômato.")
# função de validar automato
def validar_automato(automato):
    for d in automato.delta:
        if automato.estados.count(d['estado_atual']) < 1:
            print('O estado ' + d['estado_atual'] + ' não pertence ao conjunto de estados do autômato.')
            return False
        elif automato.estados.count(d['proximo_estado']) < 1:
            print('Não foi possível realizar a transição de estado ' + d['estado atual'] + ' com entrada ' + d['simbolo'])
            return False
        elif automato.sigma.count(d['simbolo']) < 1:
            print('O símbolo ' + d['simbolo'] + ' não pertence ao alfabeto do autômato.')
            return False
        else:
            return True

documento_encontrado = False
finalizar = False
print('| Interpretador de Autômatos Finitos Determinísticos |')
print("Digite '/sair' para finalizar o programa.")
while documento_encontrado == False and finalizar == False:
    # definir JSON a ser aberto
    doc = str(input('Digite o nome do documento JSON a ser usado como descrição de autômato: '))
    if doc != '/sair':
        if len(doc) > 5:
            if doc[len(doc) - 5] != '.' and doc[len(doc) - 4] != 'j' and doc[len(doc) - 3] != 's' and doc[len(doc) - 2] != 'o' and doc[len(doc) - 1] != 'n':
                doc = doc + '.json'
        else:
            doc = doc + '.json'
        # abrir arquivo JSON de descrição do autômato
        try:
            with open(doc, "r") as f:
                desc_automato = json.load(f)
                documento_encontrado = True
                print(f'Documento {doc} foi encontrado com sucesso.')
        except:
            print(f'Documento {doc} não pôde ser encontrado.')
    else:
        print('Programa finalizado pelo usuário.')
        finalizar = True
if documento_encontrado == True:
    # criar automato e validar o automato
    automato_valido = False
    automato_atual = automato(desc_automato["estados"], desc_automato["sigma"], desc_automato["delta"], desc_automato["estado_inicial"], [desc_automato["estados_finais"]])
    automato_valido = validar_automato(automato_atual)
    # validar a cadeia inserida
    if automato_valido == True:
        while finalizar == False:
            cadeia = str(input('Digite a cadeia: '))
            if cadeia != '/sair':
                automato_atual.iniciar_valid(cadeia)
            else:
                print('Programa finalizado pelo usuário.')
                finalizar = True
