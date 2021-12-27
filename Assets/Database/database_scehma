CREATE TABLE customers(id INTEGER PRIMARY KEY, user_id INTEGER REFERENCES users(id) ON DELETE CASCADE DEFERRABLE);
CREATE TABLE job_titles(id INTEGER PRIMARY KEY, name VARCHAR(45) NOT NULL, description TEXT);
CREATE TABLE employees(id INTEGER PRIMARY KEY, user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
job_title INTEGER REFERENCES job_titles(id) ON DELETE SET NULL, username VARCHAR(45));
CREATE TABLE status(id INTEGER PRIMARY KEY, name VARCHAR(45) UNIQUE NOT NULL, description VARCHAR(45));
CREATE TABLE groups(id INTEGER PRIMARY KEY, name VARCHAR(45) NOT NULL, description VARCHAR(45));
CREATE TABLE employees_groups(employee_id REFERENCES employees(id) ON DELETE CASCADE, group_id REFERENCES groups(id) ON DELETE SET NULL, PRIMARY KEY(employee_id, group_id));
CREATE TABLE products(id INTEGER PRIMARY KEY, name VARCHAR(45) NOT NULL, description VARCHAR(500) NOT NULL, category INTEGER REFERENCES categories(id) ON DELETE SET NULL, barcode TEXT, price INTEGER, status REFERENCES status(id) ON DELETE SET NULL, quantity INTEGER DEFAULT 0, notes VARCHAR(500), brand INTEGER REFERENCES brands(id));
CREATE TABLE offers(id INTEGER PRIMARY KEY, start_date TEXT, end_date TEXT, percentage DECIMAL(3, 2), product INTEGER REFERENCES products(id), status INTEGER REFERENCES status(id));
CREATE UNIQUE INDEX unique_username ON employees(username);
CREATE TABLE users(id INTEGER PRIMARY KEY, first_name VARCHAR(45) NOT NULL, middle_name VARCHAR(45), last_name VARCHAR(45), phone_number TEXT, address TEXT, gender VARCHAR(1), email TEXT, notes TEXT, status INTEGER REFERENCES status(id) ON DELETE SET NULL, password TEXT);
CREATE TABLE brands(id INTEGER PRIMARY KEY, name VARCHAR(45) NOT NULL UNIQUE, description VARCHAR(100));
CREATE TABLE categories(id INTEGER PRIMARY KEY, name VARCHAR(45) NOT NULL UNIQUE, description VARCHAR(500) NOT NULL, status INTEGER REFERENCES status(id) ON DELETE SET NULL, notes VARCHAR(500), parent_category REFERENCES categories(id));