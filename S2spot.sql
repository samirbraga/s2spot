IF OBJECT_ID('S2spot', 'U') IS NOT NULL 
DROP DATABASE S2spot;

CREATE DATABASE S2spot ON

PRIMARY(
	NAME = 'S2spot',
	FILENAME = 'C:\FBD\S2spot.mdf',
	SIZE = 5120KB,
	FILEGROWTH = 1024KB
),

FILEGROUP S2spot_fg01(
	NAME = 'S2spot_001',
	FILENAME = 'C:\FBD\S2spot_001.ndf',
	SIZE = 1024KB,
	FILEGROWTH = 30%
),

(
	NAME ='S2spot_002',
	FILENAME = 'C:\FBD\S2spot_002.ndf',
	SIZE = 1024KB,
	MAXSIZE = 3072KB,
	FILEGROWTH = 15%
),

FILEGROUP S2spot_fg02(
	NAME = 'S2spot_003',
	FILENAME = 'C:\FBD\S2spot_003.ndf',
	SIZE = 2048KB,
	MAXSIZE = 5120KB,
	FILEGROWTH = 1024KB
)

LOG ON(
	NAME = 'S2spot_log',
	FILENAME = 'C:\FBD\S2spot_log.ldf',
	SIZE = 1024KB,
	FILEGROWTH = 10%
);

USE S2spot

CREATE TABLE Playlist(
	cod smallint not null,
	nome varchar(50) not null unique,
	data_criacao date not null default CONVERT(date, SYSDATETIME()),
	tempo_total real not null default 0.0,
	CONSTRAINT PKPlaylist PRIMARY KEY(cod)
) ON S2spot_fg02

CREATE TABLE Gravadora(
	cod smallint not null,
	nome varchar(50) not null,
	rua varchar(30) not null,
	cidade varchar(30) not null,
	uf varchar(3) not null,
	pais varchar(10) not null,
	numero int not null,
	homepage varchar(50) not null
	CONSTRAINT PKGravadora PRIMARY KEY (cod)
) ON S2spot_fg01

CREATE TABLE Telefones_Gravadora(
	codgrav smallint not null,
	numero varchar(15) not null,
	CONSTRAINT PKTelefoneGrav PRIMARY KEY(codgrav, numero),
	CONSTRAINT FKTelefoneGrav FOREIGN KEY (codgrav) REFERENCES Gravadora ON DELETE CASCADE
	ON UPDATE CASCADE
) ON S2spot_fg01

CREATE TABLE Interprete(
	cod smallint not null,
	nome varchar(40) not null,
	tipo varchar(30) not null,
	CONSTRAINT PKInterprete PRIMARY KEY (cod)
) ON S2spot_fg01

CREATE TABLE Periodo_Musical(
	cod smallint not null,
	descricao varchar(20) not null,
	ano_inicio int not null,
	ano_fim int not null 
	CONSTRAINT PKPerMusical PRIMARY KEY (cod)
) ON S2spot_fg01

CREATE TABLE Compositor(
	cod smallint not null,
	pr_msc smallint not null,
	nome varchar(40) not null,
	cidade varchar(30) not null,
	pais varchar(30) not null,
	dt_nasc date not null,
	dt_morte date
	CONSTRAINT PKComp PRIMARY KEY (cod),
	CONSTRAINT FKPerMsc FOREIGN KEY (pr_msc) REFERENCES Periodo_Musical ON DELETE NO ACTION
) ON S2spot_fg01

CREATE TABLE Tipo_Comp(
	cod smallint not null,
	descricao varchar(30) not null,
	CONSTRAINT PKTComp PRIMARY KEY (cod)	
) ON S2spot_fg01

CREATE TABLE Album(
	cod smallint not null,
	codgrav smallint not null,
	pr_compra real not null,
	data_compra date not null DEFAULT CONVERT(date, SYSDATETIME()),
	data_grav date not null,
	tipo_compra	varchar(20) not null, 
	descricao varchar(30) not null,
	CONSTRAINT PKAlbum PRIMARY KEY (cod),
	CONSTRAINT FKGrav FOREIGN KEY (codgrav) REFERENCES Gravadora ON DELETE NO ACTION,
	CONSTRAINT CHKDataComp CHECK (data_compra >= '2000.01.01'),
	CONSTRAINT CHKTipoComp CHECK (tipo_compra = 'cd' OR tipo_compra = 'vinil' OR tipo_compra = 'download'),  
) ON S2spot_fg01

CREATE TABLE Faixa(
	cod smallint not null,
	cod_alb smallint not null,
	tipo_comp smallint not null,
	tempo_exec SMALLINT not null,
	tipo_grav varchar(3) not null,
	descricao varchar(50) not null,
	CONSTRAINT PKFaixa PRIMARY KEY NONCLUSTERED (cod, cod_alb),
	CONSTRAINT FKAlbum FOREIGN KEY (cod_alb) REFERENCES Album ON DELETE CASCADE,
	CONSTRAINT FKTipoComp FOREIGN KEY (tipo_comp) REFERENCES Tipo_Comp ON DELETE NO ACTION,
	CONSTRAINT CHKTipoGrav CHECK (tipo_grav = 'ADD' OR tipo_grav = 'DDD') 
) ON S2spot_fg02

CREATE TABLE Alb_Faixa(
	cod_faixa smallint not null,
	cod_alb smallint not null,
	CONSTRAINT PKAlbFaixa PRIMARY KEY (cod_faixa, cod_alb),
	CONSTRAINT FKFaixa FOREIGN KEY (cod_faixa, cod_alb) REFERENCES Faixa 
) ON S2spot_fg02

CREATE TABLE Faixa_Inter(
	cod_faixa smallint not null,
	cod_alb smallint not null,
	cod_inter smallint not null,
	CONSTRAINT PKFaixInter PRIMARY KEY (cod_faixa, cod_alb, cod_inter),
	CONSTRAINT FKInter FOREIGN KEY (cod_inter) REFERENCES Interprete ON DELETE CASCADE,
	CONSTRAINT FKFaixaInt FOREIGN KEY (cod_faixa, cod_alb) REFERENCES Faixa ON DELETE CASCADE
) ON S2spot_fg01

CREATE TABLE Faixa_Comp(
	cod_faixa smallint not null,
	cod_alb smallint not null,
	cod_comp smallint not null,
	CONSTRAINT PKFaixComp PRIMARY KEY (cod_faixa, cod_alb, cod_comp),
	CONSTRAINT FKComp FOREIGN KEY (cod_comp) REFERENCES Compositor ON DELETE CASCADE,
	CONSTRAINT FKFaixaComp FOREIGN KEY (cod_faixa, cod_alb) REFERENCES Faixa ON DELETE CASCADE
) ON S2spot_fg02

CREATE TABLE Playlist_Faixa(
	cod_play smallint not null,
	cod_faixa smallint not null,
	cod_alb smallint not null,
	CONSTRAINT PKPlayFaixa PRIMARY KEY (cod_play, cod_faixa, cod_alb),
	CONSTRAINT FKPlayFaixa FOREIGN KEY (cod_faixa, cod_alb) REFERENCES Alb_Faixa ON DELETE CASCADE
) ON S2spot_fg02

GO

-- Índices - Questão 4 --
CREATE CLUSTERED INDEX Index_alb ON Faixa(cod_alb)
WITH (FILLFACTOR = 100, PAD_INDEX = ON)

CREATE INDEX Index_tpComp ON Faixa(tipo_comp)
WITH (FILLFACTOR = 100, PAD_INDEX = ON)

-- Gatilhos --
GO
CREATE TRIGGER gat_faixaDDD ON Faixa_Comp 
AFTER INSERT
AS
BEGIN
	DECLARE @num_faixas_barrocas INT

	SELECT @num_faixas_barrocas=count(*) FROM Faixa f INNER JOIN Faixa_Comp fc ON f.cod=fc.cod_faixa
	INNER JOIN Compositor c ON fc.cod_comp=c.cod
	INNER JOIN Periodo_Musical pm ON c.pr_msc=pm.cod
	WHERE pm.descricao<>'barroco' AND f.cod_alb=(SELECT cod_alb FROM inserted)
	IF (@num_faixas_barrocas) = 0
	BEGIN
		IF EXISTS(SELECT * FROM Faixa f 
		          INNER JOIN inserted i 
				  ON i.cod_alb = f.cod_alb
				  AND f.tipo_grav = 'ADD')
		BEGIN
			RAISERROR ('Faixas do tipo "Barroco" só podem ser criadas caso seja DDD', 10, 6)
			ROLLBACK TRANSACTION
			DELETE FROM Faixa WHERE cod=(SELECT cod_faixa FROM inserted)  
		END
	END
END

GO
CREATE TRIGGER gat_qntde_faixa ON Faixa
AFTER INSERT
AS
BEGIN
	DECLARE @qtde_faixas INT

	SELECT @qtde_faixas = COUNT(*) FROM Album a
	INNER JOIN Faixa f ON a.cod = f.cod_alb

	IF (@qtde_faixas) >= 64
	BEGIN
		RAISERROR ('Quantidade de faixas acima do permitido', 10, 6)
		ROLLBACK TRANSACTION
	END
END
 
GO
CREATE TRIGGER gat_prc_alb ON Album
AFTER INSERT, UPDATE
AS
BEGIN
	DECLARE @media_preco REAL

	SELECT @media_preco=AVG(pr_compra) FROM Album a
 	INNER JOIN Faixa f ON a.cod = f.cod_alb
	WHERE EXISTS(SELECT * FROM Album a INNER JOIN Faixa f ON a.cod = f.cod_alb WHERE f.tipo_grav = 'DDD')

	IF(SELECT pr_compra FROM inserted ) > 3 * @media_preco
	BEGIN
		RAISERROR ('Preco de compra acima do permitido', 10, 6)
		ROLLBACK TRANSACTION
	END
END

GO
CREATE TRIGGER gat_rest_per_musical ON Periodo_Musical
AFTER INSERT, UPDATE
AS
BEGIN
	IF ((SELECT count(*) FROM inserted WHERE descricao NOT IN ('barroco', 'idade media', 'renascenca', 'classico', 'romantico', 'moderno')) > 0)
	BEGIN
		RAISERROR ('Descrição de Período Musical inexistente.', 10, 6)
		ROLLBACK TRANSACTION
	END
END

GO
CREATE TRIGGER gat_pl_tempo_total ON Playlist_Faixa
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
	DECLARE @tempo_duracao int
	DECLARE @cod_play smallint

	IF EXISTS (SELECT * FROM deleted)
	BEGIN
		SELECT @cod_play = cod_play FROM deleted

		SELECT @tempo_duracao = sum(tempo_exec) FROM
		Faixa f INNER JOIN Playlist_Faixa pf ON f.cod = pf.cod_faixa AND f.cod_alb = pf.cod_alb
		INNER JOIN Playlist p ON p.cod = pf.cod_play 
		GROUP BY pf.cod_alb, pf.cod_faixa, pf.cod_play
		HAVING pf.cod_play = @cod_play;

		SET @tempo_duracao = @tempo_duracao - (SELECT f2.tempo_exec FROM deleted d 
		INNER JOIN Faixa f2 ON d.cod_faixa = f2.cod AND d.cod_alb = f2.cod_alb)

		UPDATE Playlist SET tempo_total = @tempo_duracao WHERE cod = @cod_play
	END
	ELSE
	BEGIN
		SELECT @cod_play=cod_play FROM inserted

		SELECT @tempo_duracao = sum(tempo_exec) FROM Faixa f 
		INNER JOIN Playlist_Faixa pf ON f.cod = pf.cod_faixa AND f.cod_alb = pf.cod_alb
		INNER JOIN Playlist p ON p.cod = pf.cod_play 
		GROUP BY pf.cod_alb, pf.cod_faixa, pf.cod_play
		HAVING pf.cod_play = @cod_play;

		SET @tempo_duracao = @tempo_duracao + (SELECT f2.tempo_exec FROM inserted i 
		INNER JOIN Faixa f2 ON i.cod_faixa = f2.cod AND i.cod_alb = f2.cod_alb)

		UPDATE Playlist SET tempo_total = @tempo_duracao WHERE cod=@cod_play
	END
END

GO
CREATE TRIGGER tr_adiciona_alb_faixa ON Faixa
FOR INSERT
AS
BEGIN
	DECLARE @cod_faixa smallint, @cod_alb smallint
	SELECT @cod_faixa=cod, @cod_alb=cod_alb FROM inserted
	INSERT INTO Alb_Faixa VALUES (@cod_faixa, @cod_alb)
END

-- Consultas --
SELECT * FROM Album
WHERE pr_compra>(SELECT avg(pr_compra) FROM Album)

SELECT g.nome FROM Gravadora g inner join Album a ON g.cod=a.codgrav
inner join Faixa f ON f.cod_alb=a.cod 
inner join Playlist_Faixa pf ON f.cod=pf.cod_faixa AND pf.cod_alb=f.cod_alb
inner join Playlist pl ON pl.cod=pf.cod_play
inner join Faixa_Comp fc ON fc.cod_faixa=f.cod AND fc.cod_alb=f.cod_alb
inner join Compositor c ON fc.cod_comp=c.cod
GROUP BY g.cod, g.nome, a.cod
HAVING EXISTS(
	SELECT * FROM Faixa_Comp fc2 inner join Compositor c2 ON fc2.cod_comp=c2.cod
	WHERE fc2.cod_alb=a.cod AND c2.nome='san'
)

SELECT c.nome FROM Compositor c 
inner join Faixa_Comp fc ON c.cod = fc.cod_comp
inner join Faixa f ON f.cod = fc.cod_faixa AND f.cod_alb = fc.cod_alb
inner join Playlist_Faixa pf ON pf.cod_faixa = f.cod AND f.cod_alb = pf.cod_alb
GROUP BY c.nome, c.cod
HAVING count(distinct(f.cod)) = (SELECT max(R.contagem) FROM (SELECT count(*) as contagem from Playlist p
	inner join Playlist_Faixa pf ON p.cod = pf.cod_play
	inner join Faixa_Comp fc ON pf.cod_faixa=fc.cod_faixa AND pf.cod_alb=fc.cod_alb
	where fc.cod_comp=c.cod
	group by fc.cod_comp) as R)

	-- Função necessária para a última consulta--

	-- Retorna nome da playlist que tenha uma faixa diferente de barroco e concerto --
GO
CREATE FUNCTION fun_tp_con(@id_playlist smallint)
RETURNS @table_rasult TABLE (nome_play varchar(40))
AS
BEGIN
	INSERT INTO @table_rasult
	SELECT p.nome FROM Playlist p 
	INNER JOIN Playlist_Faixa pf ON p.cod = pf.cod_play AND p.cod = @id_playlist
	INNER JOIN Faixa f ON pf.cod_faixa = f.cod AND f.cod_alb = pf.cod_alb
	INNER JOIN Tipo_Comp tc ON tc.cod = f.tipo_comp
	INNER JOIN Faixa_Comp fc ON f.cod = fc.cod_faixa AND f.cod_alb = fc.cod_alb
	INNER JOIN Compositor c ON fc.cod_comp = c.cod
	INNER JOIN Periodo_Musical pm ON pm.cod = c.pr_msc 
	WHERE tc.descricao <> 'concerto' OR pm.descricao <> 'barroco'
	RETURN 
END

SELECT p.nome FROM Playlist p 
	INNER JOIN Playlist_Faixa pf ON p.cod = pf.cod_play
	INNER JOIN Faixa f ON pf.cod_faixa = f.cod AND f.cod_alb = pf.cod_alb
	INNER JOIN Tipo_Comp tc ON tc.cod = f.tipo_comp
	INNER JOIN Faixa_Comp fc ON f.cod = fc.cod_faixa AND f.cod_alb = fc.cod_alb
	INNER JOIN Compositor c ON fc.cod_comp = c.cod
	INNER JOIN Periodo_Musical pm ON pm.cod = c.pr_msc 
	WHERE NOT EXISTS(SELECT * FROM dbo.fun_tp_con(p.cod))

