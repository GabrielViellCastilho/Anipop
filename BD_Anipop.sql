-- Criação do banco de dados
CREATE DATABASE BD_Anipop;

-- Selecionar o banco de dados criado
USE BD_Anipop;

-- Criação da tabela de Usuários


CREATE TABLE Avatar(
    AvatarID INT AUTO_INCREMENT PRIMARY KEY,
    Caminho_Imagem VARCHAR(255) NOT NULL
);
CREATE TABLE EnderecoUsuario (
    EnderecoID INT PRIMARY KEY AUTO_INCREMENT,
    Rua VARCHAR(255) NOT NULL,
    Numero VARCHAR(10),
    Bairro VARCHAR(100),
    Cidade VARCHAR(100) NOT NULL,
    Estado VARCHAR(50) NOT NULL,
    CEP VARCHAR(20) NOT NULL
);

CREATE TABLE Usuarios (
    UsuarioID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    Senha VARCHAR(255) NOT NULL,
    DataCriacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    AvatarID INT DEFAULT 1,
    EnderecoID INT,
    FOREIGN KEY (AvatarID) REFERENCES Avatar(AvatarID),
    FOREIGN KEY (EnderecoID) REFERENCES EnderecoUsuario(EnderecoID)
);


-- Criação da tabela de Categorias
CREATE TABLE Categorias (
    CategoriaID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Descricao TEXT
);

-- Criação da tabela de Produtos
CREATE TABLE Produtos (
    ProdutoID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Descricao TEXT,
    Preco DECIMAL(10, 2) NOT NULL,
    QuantidadeEstoque INT NOT NULL,
    CategoriaID INT,
    FOREIGN KEY (CategoriaID) REFERENCES Categorias(CategoriaID)
);

-- Criação da tabela de Pedidos
CREATE TABLE Pedidos (
    PedidoID INT AUTO_INCREMENT PRIMARY KEY,
    UsuarioID INT,
    DataPedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Status VARCHAR(50),
    Total DECIMAL(10, 2),
    FOREIGN KEY (UsuarioID) REFERENCES Usuarios(UsuarioID)
);

-- Criação da tabela de Itens do Pedido
CREATE TABLE ItensPedido (
    ItemPedidoID INT AUTO_INCREMENT PRIMARY KEY,
    PedidoID INT,
    ProdutoID INT,
    Quantidade INT,
    Preco DECIMAL(10, 2),
    FOREIGN KEY (PedidoID) REFERENCES Pedidos(PedidoID),
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID)
);

-- Criação da tabela de Imagens dos Produtos
CREATE TABLE ImagensProduto (
    ImagemID INT AUTO_INCREMENT PRIMARY KEY,
    ProdutoID INT,
    Imagem BLOB,
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID)
);

INSERT INTO Avatar (Caminho_Imagem) VALUES
('imagens/icones_perfil/Icone_Padrao.png'),
('imagens/icones_perfil/One_Piece/avatars-big_mom.png'),
('imagens/icones_perfil/One_Piece/avatars-brook.png'),
('imagens/icones_perfil/One_Piece/avatars-chopper.png'),
('imagens/icones_perfil/One_Piece/avatars-franky.png'),
('imagens/icones_perfil/One_Piece/avatars-jinbei.png'),
('imagens/icones_perfil/One_Piece/avatars-kaido.png'),
('imagens/icones_perfil/One_Piece/avatars-kid.png'),
('imagens/icones_perfil/One_Piece/avatars-law.png'),
('imagens/icones_perfil/One_Piece/avatars-luffy.png'),
('imagens/icones_perfil/One_Piece/avatars-nami.png'),
('imagens/icones_perfil/One_Piece/avatars-perona.png'),
('imagens/icones_perfil/One_Piece/avatars-robin.png'),
('imagens/icones_perfil/One_Piece/avatars-sanji.png'),
('imagens/icones_perfil/One_Piece/avatars-shanks.png'),
('imagens/icones_perfil/One_Piece/avatars-usopp.png'),
('imagens/icones_perfil/One_Piece/avatars-yamato.png'),
('imagens/icones_perfil/One_Piece/avatars-zoro.png'),
('imagens/icones_perfil/One_Piece/egghead-brook.png'),
('imagens/icones_perfil/One_Piece/egghead-chopper.png'),
('imagens/icones_perfil/One_Piece/egghead-franky.png'),
('imagens/icones_perfil/One_Piece/egghead-jimbei.png'),
('imagens/icones_perfil/One_Piece/egghead-luffy.png'),
('imagens/icones_perfil/One_Piece/egghead-nami.png'),
('imagens/icones_perfil/One_Piece/egghead-robin.png'),
('imagens/icones_perfil/One_Piece/egghead-sanji.png'),
('imagens/icones_perfil/One_Piece/egghead-usopp.png'),
('imagens/icones_perfil/One_Piece/egghead-zoro.png'),
('imagens/icones_perfil/One_Piece/one-piece-chopper-1.png'),
('imagens/icones_perfil/One_Piece/one-piece-chopper-2.png'),
('imagens/icones_perfil/One_Piece/one-piece-chopper-3.png'),
('imagens/icones_perfil/One_Piece/one-piece-franky-1.png'),
('imagens/icones_perfil/One_Piece/one-piece-franky-2.png'),
('imagens/icones_perfil/One_Piece/one-piece-franky-3.png'),
('imagens/icones_perfil/One_Piece/one-piece-jimbei-1.png'),
('imagens/icones_perfil/One_Piece/one-piece-jimbei-2.png'),
('imagens/icones_perfil/One_Piece/one-piece-jimbei-3.png'),
('imagens/icones_perfil/One_Piece/one-piece-jimbei-4.png'),
('imagens/icones_perfil/One_Piece/one-piece-luffy-1.png'),
('imagens/icones_perfil/One_Piece/one-piece-luffy-2.png'),
('imagens/icones_perfil/One_Piece/one-piece-luffy-3.png'),
('imagens/icones_perfil/One_Piece/one-piece-luffy-4.png'),
('imagens/icones_perfil/One_Piece/one-piece-luffy-5.png'),
('imagens/icones_perfil/One_Piece/one-piece-nico-robin-1.png'),
('imagens/icones_perfil/One_Piece/one-piece-nico-robin-2.png'),
('imagens/icones_perfil/One_Piece/one-piece-nico-robin-3.png'),
('imagens/icones_perfil/One_Piece/one-piece-roronoa-zoro-1.png'),
('imagens/icones_perfil/One_Piece/one-piece-roronoa-zoro-2.png'),
('imagens/icones_perfil/One_Piece/one-piece-sanji-1.png'),
('imagens/icones_perfil/One_Piece/one-piece-sanji-2.png'),
('imagens/icones_perfil/One_Piece/one-piece-sanji-3.png'),
('imagens/icones_perfil/One_Piece/one-piece-usopp-1.png'),
('imagens/icones_perfil/One_Piece/one-piece-usopp-2.png');