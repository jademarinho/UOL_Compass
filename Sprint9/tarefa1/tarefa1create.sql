CREATE TABLE Clientes (
  idCliente INTEGER PRIMARY KEY,
  nomeCliente VARCHAR(100),
  cidadeCliente VARCHAR(40),
  estadoCliente VARCHAR(40),
  paisCliente VARCHAR(40)
);

CREATE TABLE Carros (
  idCarro INTEGER PRIMARY KEY,
  modeloCarro VARCHAR(80),
  marcaCarro VARCHAR(80),
  anoCarro INTEGER,
  tipoCombustivel VARCHAR(20) REFERENCES Combustiveis(idCombustivel)
);

CREATE TABLE Combustiveis (
  idCombustivel INTEGER PRIMARY KEY,
  nomeCombustivel VARCHAR(50)
);

CREATE TABLE Vendedores (
  idVendedor INTEGER PRIMARY KEY,
  nomeVendedor VARCHAR(15),
  estadoVendedor VARCHAR(40),
  sexoVendedor SMALLINT
);

CREATE TABLE Locacoes (
  idLocacao INTEGER PRIMARY KEY,
  idCliente INTEGER REFERENCES Clientes(idCliente),
  idCarro INTEGER REFERENCES Carros(idCarro),
  idCombustivel INTEGER REFERENCES Combustiveis(idCombustivel),
  idVendedor INTEGER REFERENCES Vendedores(idVendedor),
  vlrDiaria DECIMAL(18,2),
  qtdDiaria INTEGER,
  dataLocacao DATETIME,
  horaLocacao TIME,
  dataEntrega DATE,
  horaEntrega TIME,
  classiCarro VARCHAR(50)
);

