# Disciplina: Lógica e Programação de Computadores
# Aluno: Claudia Rayara Alves da Silva
# Escritório de Projetos - Fase 02

import csv
import matplotlib.pyplot as plt

# Dicionário para mapear nomes de meses para números
mesesDic = {
    'janeiro': 1, 'fevereiro': 2, 'março': 3, 'abril': 4, 'maio': 5, 'junho': 6,
    'julho': 7, 'agosto': 8, 'setembro': 9, 'outubro': 10, 'novembro': 11, 'dezembro': 12
}

# Dicionário para mapear números de mês para nomes de mês
nomesMesesDic = {
    1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho',
    7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
}

# Função para validar e converter entrada de mês
def obterMes(mes):
    mes_lower = mes.lower()
    if mes_lower in mesesDic:
        return mesesDic[mes_lower]
    try:
        mes = int(mes)  # Tenta converter para número
        if mes < 1 or mes > 12:
            raise ValueError
        return mes
    except ValueError:
        return None

# Função para validar e converter entrada de ano
def obterAno(ano):
    try:
        ano = int(ano)
        if ano < 1961 or ano > 2016:
            raise ValueError("Ano inválido! Por favor, digite um ano entre 1961-2016.")
        return ano
    except ValueError as e:
        print(e)
        return None

# Função para carregar os dados do arquivo CSV
def carregaDados(nomeArq):
    dados = []
    with open(nomeArq, 'r') as arquivo:
        leitor = csv.reader(arquivo)
        cabecalho = next(leitor)  # Lê o cabeçalho
        for linha in leitor:
            dados.append(linha)
    return cabecalho, dados

# Função para filtrar dados por período e tipo
def filtrarDados(dados, mesI, anoI, mesF, anoF, opcao):
    tiposDados = {
        1: ['precipitacao', 'temperatura', 'horas_insolacao', 'temperatura_media', 'umidade_vento'],
        2: ['precipitacao'],
        3: ['temperatura'],
        4: ['umidade_vento']
    }
    
    if opcao not in tiposDados:
        print("Opção inválida! Por favor, escolha uma opção válida.")
        return []

    resultado = []
    tipoSelecionado = tiposDados[opcao]

    for linha in dados:
        data = linha[0].split('/')
        mes, ano = int(data[1]), int(data[2])
        if (mesI <= mes <= mesF) and (anoI <= ano <= anoF):
            linhaFiltrada = [linha[0]]  # Inicializar a linha filtrada com a data
            for tipo in tipoSelecionado:
                if tipo == 'precipitacao' and linha[1]:
                    linhaFiltrada.append(linha[1])
                elif tipo == 'temperatura' and linha[2] and linha[3]:
                    linhaFiltrada.append(linha[2])
                    linhaFiltrada.append(linha[3])
                elif tipo == 'horas_insolacao' and linha[4]:
                    linhaFiltrada.append(linha[4])
                elif tipo == 'temperatura_media' and linha[5]:
                    linhaFiltrada.append(linha[5])
                elif tipo == 'umidade_vento' and linha[6] and linha[7]:
                    linhaFiltrada.append(linha[6])
                    linhaFiltrada.append(linha[7])
            resultado.append(linhaFiltrada)
    return resultado

# Função para exibir dados em formato de texto
def exibirDadosTxt(cabecalho, dados, opcao):
    if opcao == 1:
        print('\t'.join(cabecalho))
    elif opcao == 2:
        print('\t'.join(cabecalho[:2]))  # Precipitação
    elif opcao == 3:
        print('\t'.join([cabecalho[0]] + cabecalho[2:4]))  # Temperatura
    elif opcao == 4:
        print('\t'.join([cabecalho[0]] + cabecalho[6:8]))  # Umidade e Vento

    for linha in dados:
        print('\t'.join(linha))

# Função para encontrar o mês menos chuvoso
def encontrarMesMenosChuvoso(dados):
    precipitacaoMesAno = {}
    for linha in dados:
        data = linha[0].split('/')
        mes, ano = int(data[1]), int(data[2])
        precipitacao = float(linha[1]) if linha[1] else 0.0
        chave = (mes, ano)
        if chave in precipitacaoMesAno:
            precipitacaoMesAno[chave] += precipitacao
        else:
            precipitacaoMesAno[chave] = precipitacao
    
    # Encontrar o mês menos chuvoso
    mesMenosChuvoso = None
    menorPrecipitacao = float('inf')
    for chave, precipitacao in precipitacaoMesAno.items():
        if precipitacao < menorPrecipitacao:
            menorPrecipitacao = precipitacao
            mesMenosChuvoso = chave
    
    return mesMenosChuvoso, menorPrecipitacao

# Nome do arquivo CSV
nomeArq = 'Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv'

# Carregar dados do arquivo CSV
cabecalho, dados = carregaDados(nomeArq)

pedindoEntrada = True  # Variável para controlar se devemos continuar pedindo entradas

while pedindoEntrada:
    # Solicitar entrada do usuário para o período e tipos de dados
    while True:
        mesI = input('Informe o mês inicial: ')
        mesI = obterMes(mesI)
        if mesI is not None:
            break
        else:
            print("Mês inválido! Por favor, digite um mês válido.")

    while True:
        anoI = input('Informe o ano inicial: ')
        anoI = obterAno(anoI)
        if anoI is not None:
            break

    while True:
        mesF = input('Informe o mês final: ')
        mesF = obterMes(mesF)
        if mesF is not None:
            break
        else:
            print("Mês inválido! Por favor, digite um mês válido.")

    while True:
        anoF = input('Informe o ano final: ')
        anoF = obterAno(anoF)
        if anoF is not None:
            break

    # Solicitar entrada para o tipo de dados
    while True:
        tiposDados = {
            1: 'Todos os dados',
            2: 'Precipitação',
            3: 'Temperatura',
            4: 'Umidade e Vento'
        }
        print("Escolha o tipo de dados que deseja visualizar:")
        for key, value in tiposDados.items():
            print(f"{key} - {value}")

        opcao = input('Digite o número da opção desejada ou "Fim" para encerrar: ').strip().lower()
        if opcao == "fim":
            pedindoEntrada = False  # Definir como False para encerrar o loop
            break  # Sair do loop interno
        elif opcao.isdigit():
            opcao = int(opcao)
            if opcao in tiposDados:
                dados_filtrados = filtrarDados(dados, mesI, anoI, mesF, anoF, opcao)
                exibirDadosTxt(cabecalho, dados_filtrados, opcao)
            else:
                print("Opção inválida! Por favor, digite uma opção válida.")
        else:
            print("Opção inválida! Por favor, digite uma opção válida.")

# Encontrar o mês menos chuvoso após a conclusão da visualização
mesMenosChuvoso, menorPrecipitacao = encontrarMesMenosChuvoso(dados)
if mesMenosChuvoso:
    mes, ano = mesMenosChuvoso
    nome_mes = nomesMesesDic[mes]  # Obter o nome do mês
    print(f"Mês menos chuvoso: {nome_mes}/{ano}")
    print(f"Menor precipitação: {menorPrecipitacao} mm")
else:
    print("Não foi possível encontrar o mês menos chuvoso.")

# Dicionário com os nomes dos meses
nomesMeses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro",
}

# Função para converter datas de 'DD/MM/YYYY' para 'DD-MM-YYYY'
def converter_data(data):
    dia, mes, ano = data.split('/')
    return f"{dia}-{mes}-{ano}"

# Converter as datas no formato correto
for linha in dados:
    linha[0] = converter_data(linha[0])

# Filtrar os dados para o período de 2006 a 2016
dadosPeriodo = [linha for linha in dados if '2006' <= linha[0].split('-')[2] <= '2016']

# Função para calcular a média da temperatura mínima de um mês
def mediaTempMinMes(dados, mes):
    mediasAno = {}  # Dicionário para armazenar as médias por ano

    for linha in dados:
        data = linha[0].split('-')
        ano = int(data[2])
        if int(data[1]) == mes:
            temperaturaMin = float(linha[3].replace(',', '.'))  # Índice 3 é a temperatura mínima
            if ano not in mediasAno:
                mediasAno[ano] = []  # Inicializa a lista de temperaturas para o ano
            mediasAno[ano].append(temperaturaMin)

    mediasAnuais = {}
    for ano, temperaturas in mediasAno.items():
        media = sum(temperaturas) / len(temperaturas)
        mediasAnuais[ano] = media

    return mediasAnuais

# Solicitar ao usuário o mês desejado
while True:
    try:
        mes = int(input("Digite o número do mês para obter a média da temperatura mínima de cada ano no período entre 2006 a 2016: "))
        if 1 <= mes <= 12:
            break
        else:
            print("Mês inválido. Digite um número de 1 a 12.")
    except ValueError:
        print("Entrada inválida. Digite um número de 1 a 12.")

# Calcular a média do mês informado
mediaMensal = mediaTempMinMes(dadosPeriodo, mes)
if mediaMensal:
    print(f'Média da Temperatura Mínima para o mês {nomesMeses[mes]}:')
    for ano, media in mediaMensal.items():
        print(f'{ano}: {media:.2f}°C')
else:
    print(f'Não há dados disponíveis para o mês {nomesMeses[mes]} nos últimos 11 anos.')

# Função para criar o gráfico de barras
def criarGrafico(dados, mes):
    anos = list(range(2006, 2017))
    medias = [mediaMensal.get(ano, 0.0) for ano in anos]  # Se o ano estiver ausente, assume média 0.0

    plt.bar(anos, medias, color='pink')
    plt.xlabel('Ano')
    plt.ylabel('Temperatura Mínima Média (°C)')
    plt.title(f'Média de Temperatura Mínima em {nomesMeses[mes]} nos Últimos 11 Anos')
    plt.xticks(anos)
    plt.show()

# Criar o gráfico de barras
criarGrafico(dadosPeriodo, mes)