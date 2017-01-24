insert into cliente (cpf, nomeCli) values
(123456789, 'João'),
(333445555, 'Maria'),
(999887777, 'Tiago'),
(987654321, 'Ana'),
(666884444, 'Rita');

insert into peca (codPeca, descricao) values
('1a678234','Memoria HyperX Fury DDR4 16GB'),
('3g098365','Placa de Video EVGA Nvidia GeForce GTX 1080 8GB'),
('5t345098','XFX Radeon HD 5450 Placa gráfica'),
('4r092183','Processador Intel Deca Core I7-6950X'),
('8h023902','HD SATA3 SSD 120GB 2.5');

insert into computador (numSerie, modelo, cpfCli) values
('2340kjh234','All in One Samsung',999887777),
('0938dfg123','Apple iMac',666884444),
('3233jjd213','Notebook Positivo',123456789),
('0939dks523','Notebook Dell',333445555),
('3248las798','All in One HP', 987654321);

insert into upgrade_revisao (numSerieComputador, dataProgramada, dataUltimoUpgrade, dataExecutada) values
('2340kjh234','20161110', '20150302','20161109'),
('3248las798','20161223',NULL,'20161221'),
('0939dks523','20161004','20140501','20161002');

insert into peca_upgrade_revisao(numSerieMaquina,dataProgramadaServico,codPecaServico,quantidade) values
('2340kjh234', '20161110', '1a678234', 1),
('3248las798','20161223', '4r092183', 1),
('0939dks523', '20161004', '8h023902', 2);

