
--If database exists, drop it and create a new one
DROP DATABASE IF EXISTS BiblotekDB;
GO
CREATE DATABASE BiblotekDB;
GO



USE BiblotekDB;
GO

DROP TABLE IF EXISTS Bogkategori;
GO
CREATE TABLE Bogkategori (
    --Primary key
    BogkategoriID int NOT NULL IDENTITY(1,1) PRIMARY KEY,
    Bogkategori nvarchar(50)
);
GO


DROP TABLE IF EXISTS Bøger;
GO
CREATE TABLE Bøger (
	BogID int IDENTITY(1,1) PRIMARY KEY,
	Titel nvarchar(50),
	Forfatter nvarchar(50),
	Forlag nvarchar(50),
	ISBN nvarchar(50),
	Udgivelsesår int,
	BogkategoriID int FOREIGN KEY REFERENCES Bogkategori(BogkategoriID)
);
GO

DROP TABLE IF EXISTS Brugere;
GO
CREATE TABLE Brugere (
	Brugernavn nvarchar(50) PRIMARY KEY,
	Adgangskode nvarchar(50),
	Fornavn nvarchar(50),
	Efternavn nvarchar(50),
	Adresse nvarchar(50),
	Postnummer int,
	ByNavn nvarchar(50),
	Telefon int,
	Email nvarchar(50),
	Admin bit
);
GO

DROP TABLE IF EXISTS Forfattere;
GO
CREATE TABLE Forfattere (
	ForfatterID int IDENTITY(1,1) PRIMARY KEY,
	Fornavn nvarchar(50),
	Efternavn nvarchar(50),
	Fødselsår int
);
GO

DROP TABLE IF EXISTS Forlag;
GO
CREATE TABLE Forlag (
	ForlagID int IDENTITY(1,1) PRIMARY KEY,
	Navn nvarchar(50),
	Adresse nvarchar(50),
	Postnummer int,
	Email nvarchar(50)
);
GO

DROP TABLE IF EXISTS users;
GO
CREATE TABLE users (
    username nvarchar(50),
    Upassword nvarchar(50)
)
GO

--Insert username and password into users table
INSERT INTO users VALUES ('LøjAdmin', 'LøjSuppe123');




--Make stored procedures


--Make a stored procedure that inserts a new book into the database
CREATE OR ALTER PROCEDURE InsertBog(
    @Titel nvarchar(50),
    @Forfatter nvarchar(50),
    @Forlag nvarchar(50),
    @Sidetal int,
    @ISBN nvarchar(50),
    @Udgivelsesår int,
    @BogkategoriID int
)
AS
BEGIN
    INSERT INTO Bøger (Titel, Forfatter, Forlag, Sidetal, ISBN, Udgivelsesår, BogkategoriID)
    VALUES (@Titel, @Forfatter, @Forlag, @Sidetal, @ISBN, @Udgivelsesår, @BogkategoriID);
END
GO

--Make a stored procedure that inserts a new user into the database
CREATE OR ALTER  PROCEDURE InsertBruger(
    @Brugernavn nvarchar(50),
    @Adgangskode nvarchar(50),
    @Fornavn nvarchar(50),
    @Efternavn nvarchar(50),
    @Adresse nvarchar(50),
    @Postnummer int,
    @ByNavn nvarchar(50),
    @Telefon int,
    @Email nvarchar(50)

)
AS
BEGIN
    INSERT INTO Brugere (Brugernavn, Adgangskode, Fornavn, Efternavn, Adresse, Postnummer,  [ByNavn], Telefon, Email)
    VALUES (@Brugernavn, @Adgangskode, @Fornavn, @Efternavn, @Adresse, @Postnummer, @ByNavn, @Telefon, @Email);
END

GO
--Make a stored procedure that inserts a new author into the database
CREATE OR ALTER PROCEDURE InsertForfatter(
    @Fornavn nvarchar(50),
    @Efternavn nvarchar(50),
    @Fødselsår int
)
AS
BEGIN
    INSERT INTO Forfattere (Fornavn, Efternavn, Fødselsår)
    VALUES (@Fornavn, @Efternavn, @Fødselsår);
END
GO


--Make a stored procedure that inserts a new publisher into the database
CREATE OR ALTER PROCEDURE InsertForlag(
    @Navn nvarchar(50),
    @Adresse nvarchar(50),
    @Postnummer int,
    @Email nvarchar(50)
)
AS
BEGIN
    INSERT INTO Forlag (Navn, Adresse, Postnummer, Email)
    VALUES (@Navn, @Adresse, @Postnummer, @Email);
END
GO

--Make a stored procedure that inserts a new category into the database
CREATE OR ALTER PROCEDURE InsertBogkategori(
    @Bogkategori nvarchar(50)
)
AS
BEGIN
    INSERT INTO Bogkategori (Bogkategori)
    VALUES (@Bogkategori);
END
GO

--Make a stored procedure that updates a book in the database
CREATE OR ALTER PROCEDURE UpdateBog(
    @BogID int,
    @Titel nvarchar(50),
    @Forfatter nvarchar(50),
    @Forlag nvarchar(50),
    @Sidetal int,
    @ISBN nvarchar(50),
    @Udgivelsesår int,
    @BogkategoriID int
)
AS
BEGIN
    UPDATE Bøger
    SET Titel = @Titel,
    Forfatter = @Forfatter,
    Forlag = @Forlag,
    Sidetal = @Sidetal,
    ISBN = @ISBN,
    Udgivelsesår = @Udgivelsesår,
    BogkategoriID = @BogkategoriID
    WHERE BogID = @BogID;
END
GO

--Make a stored procedure that updates a user in the database
CREATE OR ALTER PROCEDURE UpdateBruger(
    @Brugernavn nvarchar(50),
    @Adgangskode nvarchar(50),
    @Fornavn nvarchar(50),
    @Efternavn nvarchar(50),
    @Adresse nvarchar(50),
    @Postnummer int,
    @ByNavn nvarchar(50),
    @Telefon int,
    @Email nvarchar(50)
)
AS
BEGIN
    UPDATE Brugere
    SET Brugernavn = @Brugernavn,
    Adgangskode = @Adgangskode,
    Fornavn = @Fornavn,
    Efternavn = @Efternavn,
    Adresse = @Adresse,
    Postnummer = @Postnummer,
    ByNavn = @ByNavn,
    Telefon = @Telefon,
    Email = @Email
    WHERE Brugernavn = @Brugernavn;
END

GO


--Use stored procedure that inserts a new book into the database
EXEC InsertBog 'Harry Potter', 'J.K. Rowling', 'Viking Press', 400, '9780747532743', 1997, 1;
--Use stored procedure that inserts a new user into the database
EXEC InsertBruger 'admin', 'admin', 'Admin', 'Admin', 'Adminvej', '1234', 'Adminby', '12345678', '1';
