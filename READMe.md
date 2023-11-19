
### Programa de bolsas
![d](https://github.com/suellencosta7/Trilha_Aprendizado/blob/main/icon-compass.png) ***Compass UOL em parceria com a UniCesumar*** <br>
 
 *Sprint 8*: Supervisionada por Augusto Schnorr


   "AWS Data Egineering" empregado pela Compass.uol, repositório criado para obter organização
e acompanhamento de todo programa.<br>
<br>
    Cada Sprint, tem o seu *Readme*, ou seja, informações pessoais e desenvolvimento da mesma.<br>
Para esta, as informações pessoais foram retiradas para focar nas informações do projeto. <br>
   

---
              
 **Apresentação** ![movie](https://github.com/suellencosta7/Mini_Projetos.Front/blob/main/imgs/icons8-projetor-de-filme-32.png)

_*Popularidade e premiações dos filmes e atores entre 2020 a 2023*_ <br>
_Animação e Comédia_

<br>Para este projeto, escolhi uma análise ampla, quero trazer os filmes mais populares disponíveis no arquivo _'movies.csv_'. 
Como critério de julgamento da popularidade de um filme, considerei a média e quantidade de votação, completando essa análise com 
os dados de popularidade vindo da *_API TMDB_*. <br>
<br>
     A análise, será dividida em partes, após extrair informações que julgam um filme como popular (CSV e TMDB) e limpeza
de dados, uma nova análise será feita, quem são eles? <br>
<br>
     Descobrindo quem são, inicio uma nova extração, agora na IMDB (através do ID disponível no CSV) os filmes populares, tiveram 
premiações(filmes e atores)? Se sim, quais? 
_Essa parte da análise, escolhir trazer da IMDB porque não estão disponiveis na TMDB_.<br>
<br>
     *Endpoint*, para trabalhar na TMDB, ecolhi a que eu conseguisse trazer por filme, assim trago os dados que preciso diretamente.<br>
Sem precisar de paginação.


**Por que do tema?**

_Trabalhar com múltiplas análises_: Quero através de uma análise criar outra, 'brincar com dados' juntando ambas terei a conclusão do tema.

---
**Desenvolvimento - Codificando** <br>
<br>
     Transformar a ideia em código, foi um dos maiores desafios, [aqui](https://github.com/suellencosta7/Trilha_Aprendizado/blob/main/Sprint8/ETL_API_TMDB/documentation.md) explico detalhadamente a função do meu código.<br> 
<br> 
Em resumo, na primeira parte busco do CSV filmes com os gêneros que preciso, excluído colunas desnecessária e focando nos dados de <br>
votação e ano de lançamento.<br> 
<br> 
Com os filmes em mãos, começaram as requisições, busquei o que faltava na _TMDB_ por filme, ou seja, os filmes que vieram do CSV, se tornou uma lista como parâmetro
no for que foi percorrendo na API e trazendo somente o que eu precisava, o filme específico e os dados de populariddade. <br> 
<br>
O foco é trabalhar diretamente nos filmes que tenho no CSV, tranzendo novas informações, não mais filme.

---
**BONUS**
<br>
* O que teve na sprint: <br>

     [x] **Análise e extração de informações do CSV e API** <br> 
     [x] **Alimentação no data-lake via _Lambda-S3_** <br> 
     [x] **Atividades práticas com Python e Spark**<br> 
     
<br>

**Resumo pessoal** <br>
<br>
Tive várias dificuldades, dentre elas, elaboração do código, tanto localmente, quanto na nuvem, exercícios do Spark, mas a maior 
que enfrentei nesta fase, foi a organização com os dados _(ETL/API)_. Gastei muito tempo para entender como trabalhar com a API
e o que fazer com o 'excesso de informação' disponível e criar uma análise  com base no arquivo ja existente. <br> 
<br>
Obtive muita informação e pouco destino, perdi tempo, código e rendimento. <br>
<br>
Maior aprendizado, saber gerenciar tempo e tarefas, deixar claro o que o código deve fazer antes de existir e criar melhorias,<br>
novas funções, após sua 1° versão.
