### Tarefa 1: Modelagem Relacional - Normalização

1. Primeiro criamos as tabelas de interesse, no meu caso criei (Clientes, Carros, Combustiveis, Vendedores, Locacoes) com os itens a serem normalizados e subsequentemente o data type adequado para a informaçãoo que ia ser armazenada. [link](tarefa1/tarefa1create.sql) Caso ela seja alguma das chaves (primaria ou estrangeira), ela precisa ser referenciada.

2. Tabelas criadas, a IDE que utilizei criou o o desenho da Modelagem Lógica. [Diagrama](Sprint9\tarefa1\tarefa1diagrama.jpg)

3. Agora precisa inserir os dados, agora normalizados, dentro das tabelas. [link](Sprint9\tarefa1\tarefa1insert.sql)

### Tarefa 2: Modelagem Dimensional - Criação de Modelo

1. Primeiro criei as Dimensões (Tempo, Cliente, Vendedor) e a Dimensão Locação facilitando a visualização [link](Sprint9\tarefa2\tarefa2view.sql)

2. As dimensões e Locação. [link](Sprint9\tarefa2\tarefa2views.jpg)

3. Dimensão Clientes [link](Sprint9\tarefa2\tarefa2dimcliente.jpg)

> O desafio tem sua pasta propria porque ele passa de uma sprint para outra, então toda a parte III está /Desafio/Sprint9

### Tarefa 3: Desafio Parte 3 - Processamento da Trusted

O objetivo dessa tarefa é persistir os dados na camada Trusted do meu bucket no formato PARQUET em DOIS Jobs. 
Temos dois dados a serem persistidos, o CSV e o JSON.

Primeiro o CSV, com delimiter '|' [link](Desafio\Sprint9\Tarefa3\csvtoparquet.py)
Sucesso ao rodar o job [link](Desafio\Sprint9\Tarefa3\csvtoparquet1.jpg)
Job Details [link](Desafio\Sprint9\Tarefa3\csvtoparquet2.jpg)
E os PARQUET na pasta Trusted [link](Desafio\Sprint9\Tarefa3\csvtoparquet3.jpg)

Agora o JSON [link](Desafio\Sprint9\Tarefa3\jsontoparquet.py)
Job Details [link](Desafio\Sprint9\Tarefa3\jsontoparquet2.jpg)
Sucesso do job [link](Desafio\Sprint9\Tarefa3\jsontoparquet3.jpg)

### Tarefa 4: Desafio Parte 3 - Modelagem de dados da Refined

Este desafio tem como objetivo deixar os dados prontos para analise, colocar os devidos data types no banco de dados e fazer a Modelagem Dimensional.

Minha curiosidade me trouxe a pesquisar veio relacionada a duração dos filmes nos ultimos anos, por exemplo, Senhor dos Anéis: O Retorno do Rei (2003), Vingadores: Ultimato de (2019) e tem 3 horas e 20 minutos de duração e Avatar: O caminho da Água (2022), que não teve notas tão boas quanto as anteriores dessa lista.
O objeto da minha pesquisa é relacionar a Duração do filme x As Notas e Votos x Ao longo de anos e decadas.

Então primeiro iremos criar os banco de dados no AWS Glue Data Catalog a serem refinados. No menu: 


Data Catalog > Crawlers > Create crawler
1. Crawler details: Define o nome e a descrição
2. Data Sourse config: Not yet. Add a data source: Coloca a pasta do S3 da Trusted dos dados a serem passados, um job para cada um, do JSON e do CSV.
3. Escolhe o IAM Role que tem as credenciais necessárias para realizar o job.
4. Output configuration: Define o nome da database de saída desse Crawler. 
5. Confere os dados e confirma no botão laranja na lateral direita da tela.

Aqui um dos crawlers executados com sucesso e suas configs. [link](Desafio\Sprint9\Tarefa4\crawlercsv.jpg)

Com isso as databases csv e json vão estar aptas a serem vistas no AWS Athena para realizar os demais refinamentos.

Com meu objetivo em mente selecionei as tabelas relacionadas as minhas pesquisas e criei as views localmente para gerar o Diagrama das tabelas para analise futura. [link](Desafio\Sprint9\Tarefa4\modRefined.jpg)

Aqui o codigo SQL que cria a nova tabela refinada com o JOIN necessario de csv com a json para analise.[link](Desafio\Sprint9\Tarefa4\joincsvjson6.sql)
Notas: função CAST para alterar os data types e poder realizar os calculos nas analises futuras.

As Dimensões são 'tempominutos', 'ano, 'decada' e as Medidas são 'vote_average' e 'vote_count'. [Tempo x Notas]

Aqui esta as queries SQL que usei para VIEW os dados no AWS Athena e conferir se os dados estavam vindo como esperados.
*Extra: para minha surpresa o banco de dados CSV possui mais votos que o banco de dados JSON resultante da API.*
As queries tem comentarios sobre o que elas fazem e as views que quero obter, tais como: 
- Persistir dados nota media, numerovotos do csv e json vote_avarege, vote_count.
- Atualizar notas e numero de votos do json 
- Declara os países em que foram produzidos os filmes.
- Agrupa as colunas quantidade de filmes, "vote_average" e "vote_count" por ano e década.
- Agrupa ids e decadas.

### Tarefa 5: Desafio Parte 3 - Processamento da Refined

Objetivo agora é gerar o PARQUET na camada REFINED no Spark script editor.
Aqui o sprint [link](Desafio\Sprint9\Tarefa5\dftorefined.py)
Aqui a pasta no S3 com os arquivos [link](Desafio\Sprint9\Tarefa5\s3parquets.jpg)
Depois fiz download e li no meu notebook localmente para ver se os PARQUET tinham sidos feitos corretamente. [link](Desafio\Sprint9\Tarefa5\abrindoparquet3.ipynb)

Motto da sprint: Descomplicado é melhor. Usar a tecnologia ao meu favor e explorando novos jeitos de fazer para a atividade
