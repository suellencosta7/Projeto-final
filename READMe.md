
### Programa de bolsas
![d](https://github.com/suellencosta7/Projeto-final/blob/main/imgs/icon-compass.png) ***Compass UOL em parceria com a UniCesumar*** <br>
 
 
 * Etapa supervisionada por Augusto Schnorr


   "AWS Data Egineering" empregado pela Compass.uol.<br>
    O desafio foi : _Usar o aquivo CSV como base, tranzendo novas informações da API TBDB ou Twiter de acordo com o tema escolhido_.



---
              
 **Apresentação** ![movie](https://github.com/suellencosta7/Mini_Projetos.Front/blob/main/imgs/icons8-projetor-de-filme-32.png)

_*Popularidade e premiações dos filmes entre 2020 a 2022*_ <br>
_Animação e Comédia_

<br>Para este projeto, escolhi múltiplas análises, com intuido em aproveitar ao máximo as técnicas de ETL. Escolhi três bases de dados; aquivo CSV,API TMDB e IMDB.
Para início, extrair os filmes mais populares disponíveis no arquivo _'movies.csv_' levando como critério de julgamento a pontuação de nota média e votação. Com 
os _filmes mais polulares entre 2020 a 2022_ em mão, extrair os dados de população dos mesmo vindo da API TMDB. <br>
Para complentar, extrair da IMDB os filmes que tiveram alguma premiação ou reconhecimento.
O foco desta analise é extrair os filmes mais populares com o máximo de informações que o julgam como tal. <br>
<br>

---
<br>

**Por que do tema?**

_Trabalhar com múltiplas análises_: Quero através de uma análise criar outra, 'brincar com dados' juntando ambas para conclusão do tema.

---
**Desenvolvimento - Codificando** <br>
<br>
     Transformar a ideia em código, foi um dos maiores desafios, [aqui](https://github.com/suellencosta7/Projeto-final/blob/main/arquivos/documentation.md) explico detalhadamente a função do meu código.<br> 
<br> 
Em resumo, na primeira parte busco do CSV filmes com os _gêneros_ que preciso,pois neste arquivo há diferentes generos e informações, excluir colunas desnecessária focando nos dados de _nota,votação e ano de lançamento_ .<br> 
<br> 
Com os filmes em mãos, começaram as requisições, busquei o que faltava na _TMDB_ por filme, ou seja, os filmes que vieram do CSV, se tornou uma lista como parâmetro
no [for](https://wiki.python.org/moin/ForLoop) que foi percorrendo na API TBDB  trazendo somente o que eu precisava, o filme específico e os dados de populariddade.
O mesmo foi feito na IMDB, porém extraindo somente filmes que foram premiados e qual premiação foi.  <br> 
<br>

