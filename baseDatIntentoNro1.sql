CREATE TABLE estados (
    id_est INT PRIMARY KEY,
    nom_est VARCHAR(50) NOT NULL
);

CREATE TABLE tipo_acceso (
    id_tip_acc INT PRIMARY KEY,
    nom_tip_acc VARCHAR(50) NOT NULL
);

CREATE TABLE Proyectos (
    id_pro INT PRIMARY KEY AUTO_INCREMENT,
    nom_pro VARCHAR(50) NOT NULL,
    des_pro VARCHAR(255) NOT NULL,
    fec_ini_pro DATE NOT NULL,
    id_est INT NOT NULL,
    FOREIGN KEY (id_est) REFERENCES estados(id_est)
);

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
    sal_emp INT(10) NOT NULL ,
    id_est INT NOT NULL, -- ¡AQUI! Especificamos si el empleado está habilitado o no.
    id_pro INT NULL, -- ¡ESTA COLUMNA! Almacena el proyecto actual del empleado. NULL si no está asignado.
    id_tip_acc INT NOT NULL, -- ¡ESTE! Es el tipo de acceso que tiene el empleado en su usuario.
    nom_usu VARCHAR(50) UNIQUE NULL, -- Nombre de usuario para login. UNIQUE para que no se repita. Puede ser NULL.
    con_usu VARCHAR(255) NULL, -- Contraseña (hasheada). Puede ser NULL.
    FOREIGN KEY (id_est) REFERENCES estados(id_est),
    FOREIGN KEY (id_pro) REFERENCES Proyectos(id_pro),
    FOREIGN KEY (id_tip_acc) REFERENCES tipo_acceso(id_tip_acc)
);
-- HABILITADO: Es empleado activo de la empresa
-- DESHABILITADO: Es un empleado que fue desvinculado de la empresa
INSERT INTO estados (id_est, nom_est) VALUES (1, 'HABILITADO');
INSERT INTO estados (id_est, nom_est) VALUES (2, 'DESHABILITADO');

-- GESTION DE PROYECTOS: Encargados del CRUD de los proyectos
-- GERENTE: Encargado del CRUD de los empleados y asignarlos a los proyectos
INSERT INTO tipo_acceso (id_tip_acc, nom_tip_acc) VALUES (1, 'GESTION DE PROYECTOS');
INSERT INTO tipo_acceso (id_tip_acc, nom_tip_acc) VALUES (2, 'GERENTE');
INSERT INTO tipo_acceso (id_tip_acc, nom_tip_acc) VALUES (3, 'EMPLEADO SIN ACCESO');

-- Insertamos un par de proyectos de ejemplo
INSERT INTO Proyectos (nom_pro, des_pro, fec_ini_pro, id_est) VALUES 
('DESARROLLO ECOLOGICO', 'Proyecto para la reforestación de áreas verdes en la zona sur.', '2023-01-15', 1),
('SISTEMA DE INVENTARIO', 'Implementación de un nuevo sistema de inventario para bodegas.', '2023-03-01', 1);


-- Insertamos empleados de ejemplo con diferentes roles y estados

-- Un Gerente con acceso al sistema
INSERT INTO empleados (rut_emp, nom_emp, app_emp, apm_emp, dir_emp, tel_emp, ema_emp, fec_nac_emp, fec_ini_emp, sal_emp, id_est, id_pro, id_tip_acc, nom_usu, con_usu) VALUES 
('11111111-1', 'Wilmer', 'Alvarez', 'Riera', 'Av. Principal 123', '+56911111111', 'ricardo.alva@empresa.com', '1980-05-20', '2010-03-01', 2500000, 1, NULL, 2, 'walvarez', 'gerente'),
-- Un empleado de RRHH/Gestión de Proyectos con acceso al sistema
('22222222-2', 'Carolina', 'Mora', 'Perez', 'Calle Falsa 456', '+56922222222', 'carolina.mora@empresa.com', '1985-08-15', '2015-06-10', 1500000, 1, NULL, 1, 'cmora', 'rrhh'),
-- Un empleado sin acceso, habilitado y sin proyecto (listo para ser asignado)
('33333333-3', 'Juan', 'Gonzalez', 'Rojas', 'Pasaje Los Lirios 789', '+56933333333', 'juan.gonzalez@empresa.com', '1990-11-30', '2020-09-01', 800000, 1, NULL, 3, NULL, NULL);