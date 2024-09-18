CREATE TABLE Center ( 
    center_id INT PRIMARY KEY AUTO_INCREMENT, 
    center_name VARCHAR(50) NOT NULL 
);

CREATE TABLE Employees ( 
    employee_id INT PRIMARY KEY AUTO_INCREMENT, 
    employee_name VARCHAR(100) NOT NULL, 
    center_id INT, 
    FOREIGN KEY (center_id) REFERENCES Center(center_id) 
);


CREATE TABLE ITSpecialists (
    specialist_id INT PRIMARY KEY AUTO_INCREMENT,
    specialist_name VARCHAR(100) NOT NULL,
    center_id INT,
    FOREIGN KEY (center_id) REFERENCES Center(center_id)
);

-- Creating Tickets Table
CREATE TABLE Tickets (
    ticket_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT,
    center_id INT,
    problem_description TEXT NOT NULL,
    problem_type ENUM('hardware', 'software') NOT NULL,
    device_type ENUM('Laptop', 'Mobile', 'Printer', 'Access Point') NOT NULL,
    Status ENUM('pending', 'in process', 'completed') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id),
    FOREIGN KEY (center_id) REFERENCES Center(center_id)
);

-- Creating SoftwareTickets Table
CREATE TABLE SoftwareTickets (
    ticket_id INT PRIMARY KEY,
    os_version VARCHAR(50),
    affected_app ENUM('Office', 'Adobe Acrobat', 'Chrome', 'X-Gate', 'P&L', 'QuickBooks', 'BOB'),
    error_code VARCHAR(50),
    Screenshot BLOB,
    FOREIGN KEY (ticket_id) REFERENCES Tickets(ticket_id) ON DELETE CASCADE
);

-- Creating HardwareTickets Table
CREATE TABLE HardwareTickets (
    ticket_id INT PRIMARY KEY,
    device_sn VARCHAR(100),
    picture BLOB,
    FOREIGN KEY (ticket_id) REFERENCES Tickets(ticket_id) ON DELETE CASCADE
);


INSERT INTO Center (name) VALUES ('HQ'), ('Shatila'), ('Nabaa'), ('Tripoli'), ('Bekaa');

INSERT INTO ITSpecialists (name, center_id) VALUES
('Firas', (SELECT center_id FROM Center WHERE name = 'HQ')),
('Wael', (SELECT center_id FROM Center WHERE name = 'Bekaa')),
('Hussein', (SELECT center_id FROM Center WHERE name = 'Shatila'));
