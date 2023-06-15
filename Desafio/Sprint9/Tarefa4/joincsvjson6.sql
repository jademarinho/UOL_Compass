CREATE TABLE joincsvjson6 AS
SELECT DISTINCT
    CAST(csv.id AS VARCHAR) AS id,
    CAST(csv.tituloPrincipal AS VARCHAR) AS tituloPrincipal,
    CAST(csv.tituloOriginal AS VARCHAR) AS tituloOriginal,
    CAST(csv.tempoMinutos AS INT) AS tempoMinutos,
    CAST(csv.anoLancamento AS INT) AS anoLancamento,
    CAST(csv.genero AS VARCHAR) AS genero,
    CAST(csv.notaMedia AS DECIMAL(10, 2)) AS notaMedia,
    CAST(csv.numeroVotos AS INT) AS numeroVotos,
    json.imdb_id,
    json.production_countries,
    CAST(json.vote_average AS DECIMAL(10, 2)) AS vote_average,
    CAST(json.vote_count AS INT) AS vote_count
FROM csvrefined2 AS csv
JOIN "AwsDataCatalog"."jsonrefined"."12" AS json
ON csv.id = json.imdb_id;