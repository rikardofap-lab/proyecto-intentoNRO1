-- 1. ESTRUCTURA DE TABLAS
CREATE TABLE estados (
    id_est INT PRIMARY KEY,
    nom_est VARCHAR(50) NOT NULL
);

CREATE TABLE tipo_acceso (
    id_tip_acc INT PRIMARY KEY,
    nom_tip_acc VARCHAR(50) NOT NULL
);

CREATE TABLE sexos(
    id_sex INT PRIMARY KEY,
    nom_sex VARCHAR(50) NOT NULL
);

-- 2. ESTRUCTURA DE PROYECTOS
CREATE TABLE Proyectos (
    id_pro INT PRIMARY KEY AUTO_INCREMENT,
    nom_pro VARCHAR(50) NOT NULL,
    des_pro VARCHAR(255) NOT NULL,
    fec_ini_pro DATE NOT NULL,
    id_est INT NOT NULL,
    FOREIGN KEY (id_est) REFERENCES estados(id_est)
);

-- 3. ESTRUCTURA DE EMPLEADOS
CREATE TABLE empleados (
    id_emp INT PRIMARY KEY AUTO_INCREMENT,
    rut_emp VARCHAR(12) NOT NULL,
    nom_emp VARCHAR(50) NOT NULL,
    app_emp VARCHAR(50) NOT NULL,
    apm_emp VARCHAR(50) NOT NULL,
    dir_emp VARCHAR(100) NOT NULL,
    tel_emp VARCHAR(20) NOT NULL,
    ema_emp VARCHAR(100) NOT NULL,
    fec_nac_emp DATE NOT NULL,
    fec_ini_emp DATE NOT NULL,
    sal_emp INT(10) NOT NULL,
    id_est INT NOT NULL,
    id_pro INT NULL,
    id_tip_acc INT NOT NULL,
    nom_usu VARCHAR(50) UNIQUE NULL,
    con_usu VARCHAR(255) NULL,
    id_sex INT(1) NOT NULL, 
    FOREIGN KEY (id_sex) REFERENCES sexos(id_sex),    
    FOREIGN KEY (id_est) REFERENCES estados(id_est),
    FOREIGN KEY (id_pro) REFERENCES Proyectos(id_pro),
    FOREIGN KEY (id_tip_acc) REFERENCES tipo_acceso(id_tip_acc)
);

-- 4. INSERCIÓN DE DATOS 
INSERT INTO estados (id_est, nom_est) VALUES (1, 'HABILITADO'), (2, 'DESHABILITADO');

INSERT INTO tipo_acceso (id_tip_acc, nom_tip_acc) VALUES 
(1, 'GESTION DE PROYECTOS'), 
(2, 'GERENTE'), 
(3, 'EMPLEADO SIN ACCESO');

INSERT INTO sexos (id_sex, nom_sex) VALUES (1, 'MASCULINO'), (2, 'FEMENINO'), (3, 'OTRO');

-- 5. INSERCIÓN DE PROYECTOS BASE
INSERT INTO Proyectos (nom_pro, des_pro, fec_ini_pro, id_est) VALUES 
('DESARROLLO ECOLOGICO', 'Proyecto para la reforestación de áreas verdes en la zona sur.', '2023-01-15', 1),
('SISTEMA DE INVENTARIO', 'Implementación de un nuevo sistema de inventario para bodegas.', '2023-03-01', 1);

-- 6. INSERCIÓN DE EMPLEADOS 
INSERT INTO empleados (rut_emp, nom_emp, app_emp, apm_emp, dir_emp, tel_emp, ema_emp, fec_nac_emp, fec_ini_emp, sal_emp, id_est, id_pro, id_tip_acc, nom_usu, con_usu, id_sex) VALUES 
-- Wilmer (Gerente, Masculino)
('11111111-1', 'Wilmer', 'Alvarez', 'Riera', 'Av. Principal 123', '+56911111111', 'ricardo.alva@empresa.com', '1980-05-20', '2010-03-01', 2500000, 1, NULL, 2, 'walvarez', 'gAAAAABo_B2RqLFvoz30WKQ1WA0e6Svo5IWH-e8d7lsJmU6rO9...', 1),

-- Carolina (Gestión Proyectos, Femenino)
('22222222-2', 'Carolina', 'Mora', 'Perez', 'Calle Falsa 456', '+56922222222', 'carolina.mora@empresa.com', '1985-08-15', '2015-06-10', 1500000, 1, NULL, 1, 'cmora', 'gAAAAABo_CKeUEbZHbyWlz0OJHZalzFLsNdPJxYZFuq78Lniw-...', 2),

-- Juancho (Empleado Sin Acceso, Masculino)
('33333333-3', 'Juancho', 'Gonzalez', 'Rojas', 'Pasaje Los Lirios 789', '+56933333333', 'juan.gonzalez@empresa.com', '1990-11-30', '2020-09-01', 800000, 1, NULL, 3, NULL, NULL, 1),

-- Bob Marley (Añadido desde tus tests, Masculino)
('44444444-4', 'Bob', 'Marley', 'Alvarez', 'Jamaica', '+56123456789', 'ganya@fumodesdelos14.cl', '1978-04-05', '2000-01-01', 600000, 1, NULL, 3, NULL, NULL, 1),

-- Benjamin (Gestión Proyectos, Masculino )
('55555555-5', 'Benjamin', 'Medina', 'Colina', 'Coltauco', '+56345678910', 'benja@inakapmail.cl', '2003-08-05', '2025-10-25', 600000, 1, NULL, 1, 'B55555555-5', 'gAAAAABo_OGYZDNELy_XPw4v-bPII7dg__2YltYbsHyYp0nWDH6GYjksYbXZy8N3DLnEvDjw5Y5z9rWvDduGHcRL5kVEgVlc8g==', 1);