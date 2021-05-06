instructions = [
    'SET FOREIGN_KEY_CHECKS=0;',
    'DROP TABLE IF EXISTS Usuario;',
    'DROP TABLE IF EXISTS Recordatorio;',
    'DROP TABLE IF EXISTS Medicamento;',
    'DROP TABLE IF EXISTS Cita;',
    'SET FOREIGN_KEY_CHECKS=1;',
    """
        CREATE TABLE Usuario(
            id INT PRIMARY KEY AUTO_INCREMENT,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            address VARCHAR(100) NOT NULL,
            phone VARCHAR(10) NOT NULL,
            birthdate DATE NOT NULL,
            role INT NOT NULL,
            Family VARCHAR(100) NOT NULL
        );
    """,
    """
        CREATE TABLE Recordatorio(
            id INT PRIMARY KEY AUTO_INCREMENT,
            created_by INT NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            description TEXT NOT NULL,
            completed BOOLEAN NOT NULL,
            FOREIGN KEY (created_by) REFERENCES Usuario (id)
        );
    """,
    """
        CREATE TABLE Medicamento(
            id INT PRIMARY KEY AUTO_INCREMENT,
            created_by INT NOT NULL,
            medicine VARCHAR(100) NOT NULL,
            description TEXT NOT NULL,
            dose VARCHAR(100) NOT NULL,
            posology VARCHAR(100) NOT NULL,
            price DOUBLE NOT NULL,
            amount INT NOT NULL,
            FOREIGN KEY (created_by) REFERENCES Usuario (id)
        );
    """,
    """
        CREATE TABLE Familia(
            created_by INT NOT NULL,
            Family VARCHAR(100) primary key NOT NULL,
            FOREIGN KEY (created_by) REFERENCES Usuario (id),
            FOREIGN KEY (Family) REFERENCES Usuario(username)
        );
    """,
    """
        CREATE TABLE Mensaje(
            id INT PRIMARY KEY AUTO_INCREMENT,
            created_by INT NOT NULL,
            Family_Initials VARCHAR(100) NOT NULL,
            Contentmsg VARCHAR(100) NOT NULL,
            FOREIGN KEY (created_by) REFERENCES Usuario (id),
            FOREIGN KEY (Family_Initials) REFERENCES Familia(Family)
        );
    """,
    """
        CREATE TABLE Cita(
            id INT PRIMARY KEY AUTO_INCREMENT,
            created_by INT NOT NULL,
            date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            doctor VARCHAR(100) NOT NULL,
            specialization VARCHAR(100) NOT NULL,
            companion VARCHAR(100) NOT NULL,
            FOREIGN KEY (created_by) REFERENCES Usuario (id)
        );
    """
]