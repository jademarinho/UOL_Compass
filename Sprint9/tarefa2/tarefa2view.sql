-- View da dimensão "Tempo"
CREATE VIEW DimTempo AS
SELECT dataLocacao, horaLocacao
FROM Locacoes
GROUP BY dataLocacao, horaLocacao;

-- View da dimensão "Cliente"
CREATE VIEW DimCliente AS
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM Clientes;

-- View da dimensão "Vendedor"
CREATE VIEW DimVendedor AS
SELECT idVendedor, nomeVendedor, estadoVendedor, sexoVendedor
FROM Vendedores;

-- View do fato "Locacoes"
CREATE VIEW FatLocacoes AS
SELECT idLocacao, idCliente, idCarro, idCombustivel, idVendedor, vlrDiaria, qtdDiaria, dataLocacao, horaLocacao, dataEntrega, horaEntrega, classiCarro
FROM Locacoes;

-- View do fato "Locacoes" com informações correspondentes das dimensões 
CREATE VIEW FatLocacoes1 AS
SELECT L.idLocacao, C.nomeCliente, C.cidadeCliente, C.estadoCliente, C.paisCliente,
       Ca.marcaCarro, Ca.modeloCarro, Ca.anoCarro, V.nomeVendedor, V.estadoVendedor, V.sexoVendedor,
       L.vlrDiaria, L.qtdDiaria, L.dataLocacao, L.horaLocacao, L.dataEntrega, L.horaEntrega, L.classiCarro
FROM Locacoes L
JOIN Clientes C ON L.idCliente = C.idCliente
JOIN Carros Ca ON L.idCarro = Ca.idCarro
JOIN Vendedores V ON L.idVendedor = V.idVendedor;

