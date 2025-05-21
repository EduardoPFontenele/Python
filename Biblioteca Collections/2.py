from collections import deque, OrderedDict

def criar_filas():

    emergencia = deque(["João", "Maria", "Carlos"])
    consultas = deque(["Pedro", "Ana"])

    return OrderedDict([("Emergência", emergencia), ("Consultas", consultas)])

def atender_pacientes(filas, atendidos):

    if filas["Emergência"]:

        atendidos.append(filas["Emergência"].popleft())
        filas.move_to_end("Consultas")
    
    if filas["Emergência"]:
        atendidos.append(filas["Emergência"].popleft())
    
    if filas["Consultas"]:
        atendidos.append(filas["Consultas"].popleft())

def exibir_resultados(filas, atendidos):

    print(f"* Filas após atendimentos: {filas}")
    print(f"* Atendidos: {atendidos}")

def main():

    atendidos = []

    filas = criar_filas()
    atender_pacientes(filas, atendidos)
    exibir_resultados(filas, atendidos)

if __name__ == "__main__":
    main()