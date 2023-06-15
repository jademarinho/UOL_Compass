-- Persistir dados nota media, numerovotos do csv e json vote_avarege, vote_count.

SELECT id, tituloprincipal, tempominutos, anolancamento, notamedia, numerovotos, vote_average, vote_count
FROM "csvrefined"."joincsvjson6" 
WHERE (genero LIKE '%Action%' AND genero LIKE '%Adventure%')
ORDER BY id
--limit 50

-- note que os numeros do csv são maiores que o esperado, que os dados atualizados do JSON.

-----------------

-- vw_analise_tempo - Tempo minutos relacionado a nota media e a media de votos.

SELECT tempominutos, AVG(vote_average) AS media_notas, AVG(vote_count) AS media_votos
FROM todos_os_dados
GROUP BY tempominutos;

-- vw_analise_ano - Ano lancamento relacionando a media e a media votos.

SELECT anolancamento, AVG(vote_average) AS media_notas, AVG(vote_count) AS media_votos
FROM todos_os_dados
GROUP BY anolancamento;

-- Atualizar notas e numero de votos do json 

SELECT tituloprincipal, tempominutos, anolancamento, vote_average, vote_count
FROM "csvrefined"."joincsvjson6" 
WHERE (genero LIKE '%Action%' AND genero LIKE '%Adventure%')
ORDER BY id
--limit 50;

-----------------

-- Declara os países em que foram produzidos os filmes.

SELECT id ,tituloprincipal, genero, anolancamento, production_countries
FROM "csvrefined"."joincsvjson6" 
WHERE (genero LIKE '%Action%' AND genero LIKE '%Adventure%')
ORDER BY id
-- limit 50;

-----------------

--  Agrupa as colunas quantidade de filmes, "vote_average" e "vote_count" por ano e década.

SELECT
  anolancamento AS ano,
  FLOOR(anolancamento / 10) * 10 AS decada,
  COUNT(*) AS quantidade_filmes,
  AVG(vote_average) AS media_vote_average,
  SUM(vote_count) AS total_vote_count
FROM joincsvjson6
GROUP BY anolancamento, FLOOR(anolancamento / 10) * 10
ORDER BY anolancamento, FLOOR(anolancamento / 10) * 10;

-----------------

-- Agrupa ids e decadas.

SELECT
  id,
  tituloprincipal,
  FLOOR(anolancamento / 10) * 10 AS decada
FROM joincsvjson6
ORDER BY decada;

------------------