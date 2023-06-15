INSERT OR REPLACE INTO Clientes (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao;

INSERT OR REPLACE INTO Carros (idCarro, modeloCarro, marcaCarro, anoCarro, tipoCombustivel)
SELECT idCarro, modeloCarro, marcaCarro, anoCarro, tipoCombustivel
FROM tb_locacao;

INSERT OR REPLACE INTO Combustiveis (idCombustivel, nomeCombustivel)
SELECT idCombustivel, tipoCombustivel
FROM tb_locacao;

INSERT OR REPLACE INTO Vendedores (idVendedor, nomeVendedor, estadoVendedor, sexoVendedor)
SELECT idVendedor, nomeVendedor, estadoVendedor, sexoVendedor
FROM tb_locacao;

INSERT OR REPLACE INTO Locacoes (idLocacao, idCliente, idCarro, idCombustivel, idVendedor, vlrDiaria, qtdDiaria, dataLocacao, horaLocacao, dataEntrega, horaEntrega, classiCarro)
SELECT idLocacao, idCliente, idCarro, idCombustivel, idVendedor, vlrDiaria, qtdDiaria, dataLocacao, horaLocacao, dataEntrega, horaEntrega, classiCarro
FROM tb_locacao;
