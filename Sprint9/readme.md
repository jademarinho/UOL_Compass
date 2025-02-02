### Tarefa 1: Modelagem Relacional - Normalização

1. Primeiro criamos as tabelas de interesse, no meu caso criei (Clientes, Carros, Combustiveis, Vendedores, Locacoes) com os itens a serem normalizados e subsequentemente o data type adequado para a informação que ia ser armazenada. [link](tarefa1/tarefa1create.sql) Caso ela seja alguma das chaves (primaria ou estrangeira), ela precisa ser referenciada.

2. Tabelas criadas, a IDE que utilizei criou o desenho da Modelagem Lógica. [Diagrama](https://github.com/jademarinho/Sprint1/blob/main/Sprint9/tarefa1/tarefa1diagrama.jpg)

3. Agora precisa inserir os dados, agora normalizados, dentro das tabelas. [link](https://github.com/jademarinho/Sprint1/blob/main/Sprint9/tarefa1/tarefa1insert.sql)

### Tarefa 2: Modelagem Dimensional - Criação de Modelo

1. Primeiro criei as Dimensões (Tempo, Cliente, Vendedor) e a Dimensão Locação facilitando a visualização [link](https://github.com/jademarinho/Sprint1/blob/main/Sprint9/tarefa2/tarefa2view.sql)

2. As dimensões e Locação. [link](https://github.com/jademarinho/Sprint1/blob/main/Sprint9/tarefa2/tarefa2views.jpg)

3. Dimensão Clientes [link](https://github.com/jademarinho/Sprint1/blob/main/Sprint9/tarefa2/tarefa2dimcliente.jpg)

> O desafio tem sua pasta própria porque ele passa de uma sprint para outra, então toda a parte III está /Desafio/Sprint9

### Tarefa 3: Desafio Parte 3 - Processamento da Trusted

O objetivo dessa tarefa é persistir os dados na camada Trusted do meu bucket no formato PARQUET em DOIS Jobs. 
Temos dois dados a serem persistidos, o CSV e o JSON.

Primeiro o CSV, com “delimiter '|'” [link](https://github.com/jademarinho/Sprint1/blob/main/Desafio/Sprint9/Tarefa3/csvtoparquet.py)

Sucesso ao rodar o job [link](https://github.com/jademarinho/Sprint1/blob/main/Desafio/Sprint9/Tarefa3/csvtoparquet1.jpg)

Job Details [link](https://github.com/jademarinho/Sprint1/blob/main/Desafio/Sprint9/Tarefa3/csvtoparquet2.jpg)

E os PARQUET na pasta Trusted [link](https://github.com/jademarinho/Sprint1/blob/main/Desafio/Sprint9/Tarefa3/csvtoparquet3.jpg)

Agora o JSON [link](https://github.com/jademarinho/Sprint1/blob/main/Desafio/Sprint9/Tarefa3/jsontoparquet.py)

Job Details [link](https://github.com/jademarinho/Sprint1/blob/main/Desafio/Sprint9/Tarefa3/jsontoparquet2.jpg)

Sucesso do job [link](https://github.com/jademarinho/Sprint1/blob/main/Desafio/Sprint9/Tarefa3/jsontoparquet3.jpg)

### Tarefa 4: Desafio Parte 3 - Modelagem de dados da Refined

Este desafio tem como objetivo deixar os dados prontos para análise, colocar os devidos data types no banco de dados e fazer a Modelagem Dimensional.

Minha curiosidade me trouxe a pesquisar veio relacionada a duração dos filmes nos últimos anos, por exemplo, Senhor dos Anéis: O Retorno do Rei (2003), Vingadores: Ultimato de (2019) e tem 3 horas e 20 minutos de duração e Avatar: O caminho da Água (2022), que não teve notas tão boas quanto as anteriores dessa lista.
O objeto da minha pesquisa é relacionar a Duração do filme x As Notas e Votos x Ao longo de anos e décadas.

Então primeiro iremos criar os bancos de dados no AWS Glue Data Catalog a serem refinados. No menu: 


Data Catalog > Crawlers > Create crawler
1. Crawler details: Define o nome e a descrição
2. Data Sourse config: Not yet. Add a data source: Coloca a pasta do S3 da Trusted dos dados a serem passados, um job para cada um, do JSON e do CSV.
3. Escolhe o IAM Role que tem as credenciais necessárias para realizar o job.
4. Output configuration: Define o nome da database de saída desse Crawler. 
5. Confere os dados e confirma no botão laranja na lateral direita da tela.

Aqui um dos crawlers executados com sucesso e suas configs. [link](https://github.com/jademarinho/Sprint1/blob/main/Desafio/Sprint9/Tarefa4/crawlercsv.jpg)

Com isso as databases csv e json vão estar aptas a serem vistas no AWS Athena para realizar os demais refinamentos.

Com meu objetivo em mente selecionei as tabelas relacionadas as minhas pesquisas e criei as views localmente para gerar o Diagrama das tabelas para análise futura. [link](https://github.com/jademarinho/Sprint1/blob/main/Desafio/Sprint9/Tarefa4/modRefined.jpg) 

Aqui o codigo SQL que cria a nova tabela refinada com o JOIN necessário de csv com a json para análise. [link](https://github.com/jademarinho/Sprint1/blob/main/Desafio/Sprint9/Tarefa4/joincsvjson6.sql)
Notas: função CAST para alterar os data types e poder realizar os cálculos nas análises futuras.

Criação do Modelo normalizada dimensional e as tabelas: [codigo](https://github.com/jademarinho/Sprint1/blob/main/Desafio/Sprint9/Tarefa4/createdim.sql)

Aqui esta as [queries](https://github.com/jademarinho/Sprint1/blob/main/Desafio/Sprint9/Tarefa4/queriessql.sql) SQL que usei para VIEW os dados no AWS Athena e conferir se os dados estavam vindo como esperados.

*Extra: para minha surpresa o banco de dados CSV possui mais votos que o banco de dados JSON resultante da API.*

As queries tem comentários sobre o que elas fazem e as views que quero obter, tais como: 
- Persistir dados nota média, numerovotos do csv e json vote_avarege, vote_count.
- Atualizar notas e número de votos do json 
- Declara os países em que foram produzidos os filmes.
- Agrupa as colunas quantidade de filmes, "vote_average" e "vote_count" por ano e década.
- Agrupa ids e décadas.

### Tarefa 5: Desafio Parte 3 - Processamento da Refined

Objetivo agora é gerar o PARQUET na camada REFINED no Spark script editor.

As pastas dentro do do S3: [link](https://github.com/jademarinho/Sprint1/blob/main/Desafio/Sprint9/Tarefa5/dimfilmes.jpg)

Os arquivos parquet dentro do filmes: [link](https://github.com/jademarinho/Sprint1/blob/main/Desafio/Sprint9/Tarefa5/parquetfilmes.jpg)

Aqui o script [link](https://github.com/jademarinho/Sprint1/blob/main/Desafio/Sprint9/Tarefa5/dftorefined.py)

Aqui a pasta no S3 com os arquivos [link](https://github.com/jademarinho/Sprint1/blob/main/Desafio/Sprint9/Tarefa5/s3parquets.jpg)

Depois fiz download e li no meu notebook localmente para ver se os PARQUET tinham sidos feitos corretamente. [link](https://github.com/jademarinho/Sprint1/blob/main/Desafio/Sprint9/Tarefa5/abrindoparquet3.ipynb)


> Motto da sprint: Descomplicado é melhor. Usar a tecnologia ao meu favor e explorando novos jeitos de fazer para a atividade
