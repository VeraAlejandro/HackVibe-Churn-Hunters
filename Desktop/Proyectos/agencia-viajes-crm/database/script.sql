CREATE DATABASE travel_agency_crm;

USE travel_agency_crm;

-- TABLE USERS 
CREATE TABLE USERS(
	user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(30) NOT NULL UNIQUE,
    password_hash VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    role ENUM('ADMIN', 'EMPLOYEE') DEFAULT 'EMPLOYEE',
    is_activate BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- TABLE CLIENTS
CREATE TABLE CLIENTS(
	client_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(14),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- TABLE DESTINATIONS 
CREATE TABLE DESTINATIONS(
	destination_id INT AUTO_INCREMENT PRIMARY KEY,
    destination_name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);

-- TABLE TRAVEL_PACKAGES 
CREATE TABLE TRAVEL_PACKAGES(
	package_id INT AUTO_INCREMENT PRIMARY KEY,
    package_name VARCHAR(100),
    price DECIMAL(10,2) CHECK (price > 0),
    available_slots INT CHECK (available_slots >= 0),
    start_date DATE,
    end_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fk_destination_id INT,
	
    -- relations 
    CONSTRAINT fkTP_destination_id FOREIGN KEY (fk_destination_id) REFERENCES DESTINATIONS(destination_id)   
);  

-- TABLE BOOKINGS
CREATE TABLE BOOKINGS(
	booking_id INT AUTO_INCREMENT PRIMARY KEY,
    fk_client_id INT,
    fk_package_id INT,
    booking_date DATE DEFAULT (CURRENT_DATE),
    status ENUM('PENDING','CONFIRMED','CANCELLED') DEFAULT 'PENDING',
    
    -- relations 
    CONSTRAINT fkB_client_id FOREIGN KEY (fk_client_id) REFERENCES CLIENTS(client_id),
    CONSTRAINT fkP_package_id FOREIGN KEY (fk_package_id) REFERENCES TRAVEL_PACKAGES(package_id)
);

-- TABLE PAYMENTS
CREATE TABLE PAYMENTS(
	payment_id INT AUTO_INCREMENT PRIMARY KEY,
    fk_booking_id INT,
    amount DECIMAL(10,2) CHECK (amount > 0),
    payment_date DATE,
    payment_method VARCHAR(50),
    
    -- relations 
    CONSTRAINT fkPY_booking_id FOREIGN KEY (fk_booking_id) REFERENCES BOOKINGS(booking_id)
);

-- INDEX OP 
CREATE INDEX idx_clients_email ON CLIENTS(email);
CREATE INDEX idx_packages_destination ON TRAVEL_PACKAGES(fk_destination_id);
CREATE INDEX idx_bookings_client ON BOOKINGS(fk_client_id);