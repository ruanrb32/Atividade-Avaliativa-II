# Atividade-Avaliativa II
 Atividade 2


 # Respostas das Questões de 01 a 09


Atividade Avaliativa II


<b 1. Explique a distância de Manhattan.>

Resposta: É a medida de distância entre dois pontos em um espaço euclidiano com uma grade de pontos.

A Fórmula para calcular a distância entre dois pontos (x1,y1) e (x2,y2) em uma plano bidimensional = |x2-x1|+|y2-y1|

Exemplo: A distância de Manhattan é a soma das diferenças absolutas entre as coordenadas x e y dos dois pontos A(3,7) e B(5,9)

|5-3| + |9-7| = 2+2 = 4



2. Explique a distância euclidiana.

Resposta: É uma medida de distância entre dois pontos em um espaço euclidiano, ela representa a distancia ''em linha reta'' entre dois pontos em um espaço bidimensional ou tridimensional.

A Fórmula para calcular em plano Bidimensional:

d = √(x2-x1)² + (y2-y1)² 

A Fórmula para calcular em plano Tridimensional

d = √(x2-x1)² + (y2-y1)² + (z2-z1)²

''d'' é a distância Euclidiana
''√'' denota a raiz quadrada

3. Explique a distância de Hamming.

Resposta: É uma medida que expressa a diferença entre duas sequências de igual comprimento, contando o número de posições nas quais os símbolos correspondentes são diferentes. 

Exemplo distância de Hamming entre:

"elabore" e "melhore" é 4.
2173896 e 2233796 é 3.
11011 e 10011 é 1.

4. Explique o que é aprendizado não-supervisionado.

Resposta: O aprendizado não supervisionado é um paradigma de aprendizado de máquina em que o algoritmo é treinado em um conjunto de dados que não possui rótulos ou saídas desejadas conhecidas. Em vez de receber um conjunto de dados rotulado, onde o algoritmo é informado sobre a relação entre as entradas e as saídas correspondentes, o aprendizado não supervisionado explora a estrutura ou padrões subjacentes nos dados sem orientação externa. 

5. Explique o que é um cluster.

Resposta: Em termos de aprendizado de máquina e análise de dados, um "cluster" refere-se a um grupo de objetos ou pontos de dados que compartilham características semelhantes entre si, mas que são distintos de outros grupos. Em outras palavras, um cluster é uma coleção de elementos que são mais semelhantes entre si do que com elementos fora desse grupo. Por exemplo, se você tiver um conjunto de dados de clientes com base em suas preferências de compra, um algoritmo de agrupamento pode identificar diferentes clusters de clientes que compartilham padrões de compra semelhantes. Cada cluster representaria um grupo de clientes com características de compra comuns.


6. Explique o funcionamento do algoritmo K-Means.

Resposta: Abaixo o passo a passo do funcionamento do algoritmo K-Means:

Passo 1.Inicialização: Escolha aleatoriamente k pontos de dados do conjunto como os centróides iniciais.
Esses pontos podem ser escolhidos aleatoriamente ou de maneira mais estratégica, dependendo da implementação.

Passo 2.Atribuição de Pontos aos Clusters: Para cada ponto de dados no conjunto, calcule a distância até cada centróide.
Atribua o ponto ao cluster representado pelo centróide mais próximo.

Passo 3.Atualização dos Centróides: Recalcule os centróides de cada cluster como a média dos pontos atribuídos a esse cluster.
O centróide é recalculado usando os pontos que foram atribuídos a esse cluster na etapa anterior.

Passo 4.Repetição: Repita os passos 2 e 3 até que uma condição de parada seja atendida. A condição de parada pode ser um número fixo de iterações, a convergência dos centróides, ou outra métrica definida pelo usuário.

7. Explique o que é aprendizado supervisionado.

 Resposta: É definido pelo uso de conjuntos de dados rotulados para treinar algoritmos que classificam dados ou preveem resultados com precisão. À medida que os dados de input são inseridos no modelo, ele adapta sua ponderação até que o modelo seja ajustado adequadamente, o que ocorre como parte do processo de validação cruzada. O aprendizado supervisionado ajuda as organizações a resolver diversos problemas do mundo real em grande escala, um exemplo de aprendizado supervisonado é a classificação de spam em uma pasta separada da sua caixa de entrada.

8. Explique o funcionamento do algoritmo KNN.

Resposta: Abaixo o passo a passo do funcionamento do algoritmo KNN

Passo 1 -> Entrada de Dados: O conjunto de dados consiste em pares de entradas e rótulos (para classificação) ou saídas (para regressão).

Passo 2 -> Escolha do Parâmetro k: O número k é um parâmetro crucial no algoritmo KNN. Ele representa o número de vizinhos mais próximos que serão considerados ao fazer uma previsão.

Passo 3 -> Cálculo da Distância: Para um novo ponto de dados que precisa ser classificado ou para o qual se deseja prever um valor, o algoritmo calcula a distância entre esse ponto e todos os pontos de dados no conjunto de treinamento. A métrica de distância comum é a distância euclidiana, mas outras métricas podem ser usadas dependendo do problema.

Passo 4 -> Identificação dos Vizinhos Mais Próximos: O algoritmo seleciona os k pontos de dados mais próximos ao novo ponto com base na distância calculada.

Passo 5 -> Classificação ou Regressão: Para classificação, o rótulo mais comum entre os k vizinhos é atribuído ao novo ponto.
Para regressão, a saída é frequentemente calculada como a média ou a mediana dos valores alvo dosk vizinhos.

Conclusão: O ponto é classificado ou sua saída é prevista com base na maioria dos rótulos ou valores dos k vizinhos mais próximos.

9. Comente sobre uma área de aplicação da IA na indústria automobilística.

Resposta: Veículos Autônomos: A IA é fundamental para o desenvolvimento de veículos autônomos. Algoritmos avançados de aprendizado de máquina e visão computacional são usados para interpretar dados de sensores, como câmeras, radares e lidar, permitindo que os veículos tomem decisões em tempo real e naveguem de forma autônoma.

Assistência ao Motorista: Sistemas de assistência ao motorista, como controle de cruzeiro adaptativo, assistência de estacionamento e alertas de colisão, fazem uso de técnicas de IA para monitorar o ambiente ao redor do veículo, interpretar padrões e tomar decisões para melhorar a segurança e a conveniência.

Manutenção Preditiva: A IA é usada para analisar dados dos sensores do veículo e prever quando peças podem falhar ou precisar de manutenção. Isso permite a implementação de estratégias de manutenção preditiva, reduzindo os custos e aumentando a eficiência operacional.

Personalização do Veículo:A IA é aplicada para analisar o comportamento do motorista, preferências e dados de uso para personalizar a experiência do veículo. Isso pode incluir ajuste automático de configurações, sugestões de rotas personalizadas e recomendações de entretenimento.

Segurança Viária: Algoritmos de visão computacional e aprendizado de máquina são usados para monitorar o comportamento do motorista e identificar sinais de fadiga, distração ou comportamento perigoso. Sistemas de alerta podem então intervir para evitar acidentes.

Otimização da Cadeia de Suprimentos: A IA é aplicada na otimização da cadeia de suprimentos, ajudando a prever a demanda por peças, gerenciar inventário de forma eficiente e melhorar a eficácia geral da produção.

Desenvolvimento de Veículos: A IA é usada no processo de design e desenvolvimento de veículos para simulação avançada, otimização de design, e prototipagem virtual, acelerando o ciclo de desenvolvimento e reduzindo custos.

Análise de Dados e Conectividade: A coleta e análise de dados gerados pelos veículos conectados são facilitadas por algoritmos de IA. Isso fornece insights valiosos para os fabricantes sobre o desempenho dos veículos, preferências dos motoristas e necessidades de manutenção.

