CREATE TABLE equipment (
    id INT PRIMARY KEY AUTO_INCREMENT,
    inv_number VARCHAR(50) UNIQUE,
    name VARCHAR(100),
    type VARCHAR(50),
    department VARCHAR(100),
    year INT,
    status VARCHAR(20)
);

CREATE TABLE maintenance_request (
    id INT PRIMARY KEY AUTO_INCREMENT,
    equipment_id INT,
    description TEXT,
    priority VARCHAR(20),
    status VARCHAR(20),
    created_at DATETIME,
    FOREIGN KEY (equipment_id) REFERENCES equipment(id)
);