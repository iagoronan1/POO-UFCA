from hospede import Hospede
from quarto import Quarto
from reserva import Reserva

quartos = []
hospedes = []
reservas = []


def cadastrar_quarto():
    print("\n=== Cadastro de Quarto ===")
    numero = int(input("Número do quarto: "))
    tipo = input("Tipo (simples/duplo/luxo): ")
    capacidade = int(input("Capacidade: "))
    tarifa = float(input("Tarifa base: "))

    quarto = Quarto(numero, tipo, capacidade, tarifa)
    quartos.append(quarto)
    print("Quarto cadastrado com sucesso!\n")


def listar_quartos():
    print("\n=== Quartos Cadastrados ===")
    for q in quartos:
        print(q)


def cadastrar_hospede():
    print("\n=== Cadastro de Hóspede ===")
    nome = input("Nome: ")
    documento = input("Documento (CPF): ")
    email = input("E-mail: ")

    hospede = Hospede(nome, documento, email)
    hospedes.append(hospede)
    print("Hóspede cadastrado com sucesso!\n")


def listar_hospedes():
    print("\n=== Hóspedes ===")
    for h in hospedes:
        print(h)


def criar_reserva():
    print("\n=== Criar Reserva ===")
    doc = input("Documento do hóspede: ")
    numero_quarto = int(input("Número do quarto: "))
    entrada = input("Data de entrada (AAAA-MM-DD): ")
    saida = input("Data de saída (AAAA-MM-DD): ")
    qtd = int(input("Número de hóspedes: "))

    hospede = None
    for h in hospedes:
        if h.documento == doc:
            hospede = h
            break

    if hospede is None:
        print("Hóspede não encontrado!")
        return

    quarto = None
    for q in quartos:
        if q.numero == numero_quarto:
            quarto = q
            break

    if quarto is None:
        print("Quarto não encontrado!")
        return

    if qtd > quarto.capacidade:
        print("Erro: mais hóspedes do que a capacidade do quarto!")
        return

    reserva = Reserva(hospede, quarto, entrada, saida, qtd)
    reservas.append(reserva)
    print("Reserva criada com sucesso!\n")


def listar_reservas():
    print("\n=== Reservas ===")
    for r in reservas:
        print(r)


def menu():
    while True:
        print("\n===== SISTEMA DE HOTEL =====")
        print("1 - Cadastrar quarto")
        print("2 - Listar quartos")
        print("3 - Cadastrar hóspede")
        print("4 - Listar hóspedes")
        print("5 - Criar reserva")
        print("6 - Listar reservas")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_quarto()
        elif opcao == "2":
            listar_quartos()
        elif opcao == "3":
            cadastrar_hospede()
        elif opcao == "4":
            listar_hospedes()
        elif opcao == "5":
            criar_reserva()
        elif opcao == "6":
            listar_reservas()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")


# iniciar o sistema
menu()