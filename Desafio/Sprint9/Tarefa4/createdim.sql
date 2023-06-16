/*
Dimensões:

Dimensão "Filme":

id
tituloprincipal
titulooriginal
tempominutos
anolancamento
genero
notamedia
numerovotos
imdb_id
Dimensão "País de Produção":

id
production_countries
Dimensão "Avaliação":

id
vote_average
Dimensão "Contagem de Votos":

id
vote_count */

-- Criação da tabela "Filme"
CREATE TABLE Filme AS
SELECT
  CAST(csv.id AS VARCHAR) AS id,
  CAST(csv.tituloPrincipal AS VARCHAR) AS tituloprincipal,
  CAST(csv.tituloOriginal AS VARCHAR) AS titulooriginal,
  CAST(csv.tempoMinutos AS INT) AS tempominutos,
  CAST(csv.anoLancamento AS INT) AS anolancamento,
  CAST(csv.genero AS VARCHAR) AS genero,
  CAST(csv.notaMedia AS DECIMAL(10, 2)) AS notamedia,
  CAST(csv.numeroVotos AS INT) AS numerovotos,
  CAST(json.imdb_id AS VARCHAR) AS imdb_id,
  json.production_countries AS production_countries
FROM csvrefined2 AS csv
JOIN "AwsDataCatalog"."jsonrefined"."12" AS json
ON csv.id = json.imdb_id;

-- Criação da tabela "Avaliacao"
CREATE TABLE Avaliacao AS
SELECT
  ROW_NUMBER() OVER () AS id,
  id AS filme_id,
  CAST(json.vote_average AS DECIMAL(10, 2)) AS vote_average
FROM joincsvjson6 AS json;

-- Criação da tabela "ContagemVotos"
CREATE TABLE ContagemVotos AS
SELECT
  ROW_NUMBER() OVER () AS id,
  id AS filme_id,
  CAST(json.vote_count AS INT) AS vote_count
FROM joincsvjson6 AS json;
