###  ![Icon.Compass](https://github.com/suellencosta7/Trilha_Aprendizado/blob/main/icon-compass.png) Popularidade e premiações dos filmes entre 2020 a 2023 
##### Gênero: _Animação e Comédia_ ![Icon.movie](https://github.com/suellencosta7/Mini_Projetos.Front/blob/main/imgs/icons8-projetor-de-filme-32.png)

---

## Explicação por partes 

Essa parte do projeto, extrair informações da API com base no CSV para serem armazenados no [_data-lake_](https://aws.amazon.com/pt/big-data/datalakes-and-analytics/what-is-a-data-lake/) <b3>
hospedado no [_Simple Storage Service (S3)_](https://aws.amazon.com/pt/s3/).<br>

Para realizar esta etapa,usei dois serviços, [Lambda](https://aws.amazon.com/pt/lambda/) e S3, conectando ambos da seguinte forma:<BR> 
<br>
![conexao](https://github.com/suellencosta7/Projeto-final/blob/main/imgs/conex%C3%A3oBucket.PNG)

<br>

Com os dados de usuário IAM configurados, é possível conectar com o S3, criando uma instância  <br>
usando a [lib BOTO3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) (biblioteca de software desenvolvida pela AWS para interagir com os serviços usando Python). <br>
Usando o [boto3.client](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html):<br>
<br>
*service_name*=: 'Especifica o serviço' 
<br>
*aws_access_key_id*= 'Chave de acesso IAM'
<br>
*aws_secret_access_key*= 'Chave secreta IAM'
<br>
region_name= 'região'
<br>

--- 
### Corpo 

Após conectar o Lambda com o S3, adicionei o meu código. Primeiro importei o arquivo _movies.csv_ do s3, com a função [get-object](https://docs.aws.amazon.com/cli/latest/reference/s3api/get-object.html) ,<br>
extrair os filmes específicos para depois trabalhar com a extração na API. <br>

<br>

![CSV](https://github.com/suellencosta7/Projeto-final/blob/main/imgs/readCSV.PNG) <br>


Para extrair os filmes necessários do CSV, criei um [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) com a função [loc](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html) para selecionar colunas e linhas do que <br>
precisaria.<br>

![DATAFRAME](https://github.com/suellencosta7/Projeto-final/blob/main/imgs/DataFrames.PNG)

 ## API TMDB

Após extrair todas as informações do CSV para a análise de popularidade, filtrei somente os nomes dos filmes, que serviram <br>
de parâmetro para as [requisições na API](https://docs.python.org/3/library/urllib.request.html).<br>

*Lógica do loop* : O for recebe como parâmetro a lista de filmes(2020-2023) específico que será percorrida dentro da _ API_, cada<br> filme, um json é criado no lote. Este lote contém popularidade e nome no filme, os controladores são as variáveis _popularity_ e _title_.<br>
Quando completam 100 filmes,ambas são zeradas e um novo lote é criado.
 <br>


![REQUISIÇÃO](https://github.com/suellencosta7/Mini_Projetos.Front/blob/main/imgs/extracao_loop.PNG)

<br>

Para salvar os lotes no S3 usei a função [put_object](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html) da biblioteca *Boto3* para enviar um objeto (arquivo) para o bucket.<br> 
 <br>

![save](https://github.com/suellencosta7/Projeto-final/blob/main/imgs/CondicaoSave.PNG) <br>

![lotes](https://github.com/suellencosta7/Projeto-final/blob/main/imgs/JSONS.PNG)

### IMDB
O mesmo ocorreu na IMDB, mas desta vez ele trouxe somente os filmes que tiveram premiação e qual foi <br>
![IMDB]()
