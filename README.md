## Disciplina: Lógica de Programação - Escritório de Projetos: Fase 01.
Projeto realizado para o Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas: Full-Stack e Mobile.

## Introdução:
O projeto é individual e está organizado em duas fases. Em ambas as fases, você trabalhará com dados meteorológicos. Na primeira fase, você desenvolverá um programa que realiza análises a partir de dados informados pelo usuário. Já na segunda fase, sua implementação receberá como entrada dados vindos de um arquivo.

## Enunciado da Fase 02:
Novamente vamos trabalhar com dados meteorológicos, mas agora os dados serão de um arquivo texto. Nesta fase, você trabalhará com um conjunto de dados (em formato csv e disponibilizado na plataforma) contendo informações climáticas diárias do município brasileiro de Porto Alegre, entre os anos 1961 e 2016. O arquivo contém 18.564 registros com os campos: data, precipitação (volume de chuva em milímetros por m2), temperatura máxima (em graus celsius), temperatura mínima (em graus celsius), umidade relativa do ar (% entre 0 e 100) e a velocidade do vento (em m/s). 

**Seu programa deve ser capaz de realizar:**
* Carga e preparação de dados: trabalhar com arquivos de dados, realizando a sua leitura, filtragem das informações relevantes e armazenamento em estruturas de dados adequadas para consulta.
* Análise e visualização de dados: análises estatísticas diversas sobre os dados armazenados, por meio da implementação de algoritmos e geração de gráficos para a visualização dos resultados.

**O código entregue em linguagem Python deve permitir:**
Leitura do arquivo: os dados do arquivo devem ser carregados para memória e disponibilizados em uma lista de listas/tuplas/dicionário.   

**Observações:**
* É a partir da aula 08 que explicamos como realizar a leitura de arquivo texto e a carga dos dados em listas. No entanto, a manipulação de estruturas de dados está nas aulas anteriores à aula 08. Por isso, é importante você assistir e realizar as práticas na sequência sugerida. Nossos exemplos são todos com arquivo CSV e não há necessidade de uso de bibliotecas específicas, além das abordadas na disciplina. Além das funções de manipulação de arquivo, funções strings, como split, serão essenciais para a carga dos dados em lista/dicionário. No entanto, você pode usar outras bibliotecas se já conhecê-las.
* Crie quantas estruturas de dados (listas, dicionários, ...) que você julgar conveniente e não esqueça de organizar seu código em funções.
* Comente no seu código decisões tomadas quanto ao tratamento dos dados. Não use caminhos absolutos para o arquivo .csv, implemente considerando que o arquivo está na mesma pasta do seu programa.
* Não defina caminhos específicos dentro do seu código para acesso ao arquivo .csv. Se você entregar com caminhos absolutos o trabalho não será avaliado.
* Não modifique o arquivo .csv dado. Seu programa é que deve tratar os dados lidos do arquivo.

**a. Visualização de intervalo de dados em modo texto:** a partir de entradas do usuário, sua implementação deve permitir a visualização dos dados que foram carregados do arquivo. O usuário deve informar o período que quer ver, ou seja, deve indicar o mês e ano iniciais, bem como o mês e ano finais que deseja visualizar os dados. Permita também que o usuário informe se quer ver para o período informado:
1. Todos os dados;
2. Apenas os de precipitação;
3. Apenas os de temperatura;
4. Apenas os de umidade e vento;

**Observações:**
* Valide os dados de entrada;
* Você pode escolher a forma de apresentação dos dados, porém não esqueça de incluir um cabeçalho para os dados exibidos;

**b. Mês menos chuvoso:** o mês/ano com menor precipitação, considerando todos os dados do arquivo. Exiba também a menor precipitação na tela. Utilize obrigatoriamente um dicionário e implemente ao menos uma função. Lembre-se de considerar todos os dados do arquivo! 

**c. Média da temperatura mínima de um determinado mês (auge do inverno) nos últimos 11 anos (2006 a 2016):**
1. O programa deve escrever a média da temperatura mínima de um mês informado pelo usuário (valide a entrada) e a média geral da temperatura mínima para todo o período (11 anos). Se o mês informado for 8, ou seja, agosto, o programa exibir a temperatura mínima média do mês de agosto de cada ano (agosto/2006, agosto/2007, ...agosto/2016);
2. O programa também deve escrever qual é a média geral da temperatura mínima que engloba todos os meses de agosto desse período de 11 anos. 

Implemente ao menos uma função para estes itens e use dicionário. 

**d. Gráfico de barras (vertical ou horizontal) com as médias de temperatura mínima de um determinado mês nos últimos 11 anos:** 
Gere um gráfico com as médias calculadas do mês informado em cada ano do período conforme o item d. Não esqueça de rotular os eixos e usar legendas para deixar o seu gráfico informativo e bem elaborado.
