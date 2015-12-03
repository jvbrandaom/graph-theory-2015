T5c: Solução computacional do SUDOKU com algoritmos de coloração em grafos (Sudoku problem solver)
==================================================================================================

TODO: responder as perguntas

O programa deve, a partir de um tabuleiro de SUDOKU, criar um grafo de incompatibilidade através 
das regras do jogo. Considere a seguinte instância do jogo:

![sudoku](.readme-img/Sudoku.png)

A regra básica do jogo é: preencha os números de forma que não haja repetição na mesma linha, 
coluna ou quadradinho (3 x 3).


METODOLOGIA

Em outras palavras, o modelo a ser gerado é um grafo G com 81 vértices (quadrado 9 x 9), um 
para cada casa do tabuleiro. Cada célula do tabuleiro deve ser nomeada como um vértice, 
percorrendo o tabuleiro linha a linha (v1, v2, v3,..., v81). A partir do grafo nulo inicial 
(apenas vértices), arestas devem ser adicionadas da seguinte forma:

<ol type="i">
    <li>Se um vértice vi pertence a mesma linha que um vértice diferente vj 
        então a aresta (vi, vj) deve ser adicionada a G
    </li>
    <li>Se um vértice vi pertence a mesma coluna que um vértice diferente vj 
        então a aresta (vi, vj) deve ser adicionada a G
    </li>
    <li>Se um vértice vi pertence ao mesmo quadrado (3 x 3) que um vértice diferente 
        vj então a aresta (vi, vj) deve ser adicionada a G
    </li>
</ol>

Logo após a geração do grafo, a pré-coloração inicial (dada pelos quadradinhos já preenchidos 
do tabuleiro) deve ser realizada. Por exemplo, no caso ilustrado pela figura acima, as cores 
dos vértices da primeira linha serão: v1 = 9, v2 = 5, v6 = 1, v9 = 8. De posse do grafo e da 
pré-coloração inicial, o objetivo do trabalho consiste em desenvolver um solucionador automático 
para esse jogo utilizando o algoritmo para coloração de vértices conhecido como Welsh & Powell. 
Note que a pré-coloração faz com que as listas iniciais de possíveis cores dos vértices do grafo 
sejam diferentes. Na prática, para um vértice vi, devemos inicialmente remover de sua lista todas 
as cores encontradas em seus vizinhos. A heurística a ser adotada consiste em começar a colorir 
os vértices cujas listas de cores são as menores possíveis, pois assim praticamente não há dúvidas 
sobre a cor que devem receber. Por exemplo, se inicialmente um vértice possui uma lista de cores 
com apenas 1 cor, devemos iniciar por ele pois só há obrigatoriamente uma opção válida. Se em algum 
momento a lista de um vértice se esvazia ou tem apenas cores já assumidas pelos vizinhos, então 
não há solução válida por esse caminho e possivelmente para o tabuleiro em questão. Em geral, 
nesses casos é necessário aumentar a pré-coloração inicial, isto é, preencher mais 
quadrados inicialmente.


QUESTIONAMENTOS

<ol type="a">
    <li>
        O que podemos dizer sobre os graus do grafo G resultante?
    </li>
    <li>
        Utilizando o tabuleiro acima, obtenha uma solução aplicando 
        o algoritmo de Welsh & Powell.
    </li>
    <li>
        Reaplique o algoritmo mais três vezes e compare as 4 soluções obtidas. 
        São iguais ou diferentes?
    </li>
    <li>
        Ainda considerando o tabuleiro acima, note que inicialmente existem 
        45 valores iniciais. Remova 2 valores quaisquer de cada linha (18 no total), 
        totalizando 27 células preenchidas. Execute o método. 
        Foi possível obter uma solução válida? 
        Compare a solução com as obtidas anteriormente.
    </li>
    <li>
        O que acontece se a pré-coloração inicial tiver apenas 9 valores (1 por linha)?
    </li>
</ol>

Pense em estratégias/heurísticas que podem auxiliar no processo de coloração. 
Em [http://rachacuca.com.br/logica/sudoku/](http://rachacuca.com.br/logica/sudoku/) 
você pode encontrar algumas.


INDO ALÉM

Pesquise na internet sobre o jogo, mais precisamente, sobre o unicidade da solução em termos do número mínimo de elementos preenchidos iniciais. Em outras palavras, será que existe um número mínimo de quadradinhos que precisam ser preenchidos inicialmente para garantir que o jogo possui solução e ela seja a única possível?