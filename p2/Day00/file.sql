CREATE TABLE data_2022_oct (
    event_time TIMESTAMP,         -- Première colonne DATETIME
    event_type VARCHAR(50),       -- Type d'événement (par exemple, 'achat', 'vue')
    product_id BIGINT,            -- ID du produit
    price DECIMAL(10, 2),         -- Prix du produit
    user_id BIGINT,               -- ID de l'utilisateur
    user_session UUID             -- Session utilisateur (UUID pour l'unicité)
);

CREATE TABLE data_2023_jan (
    event_time TIMESTAMP,         -- Timestamp pour les événements
    event_type VARCHAR(255),      -- Type d'événement (comme 'achat', 'vue', etc.)
    product_id BIGINT,            -- ID du produit, supposé être un entier long
    price DECIMAL(10, 2),         -- Prix, avec deux décimales pour les centimes
    user_id BIGINT,               -- ID de l'utilisateur, supposé être un entier long
    user_session UUID             -- UUID pour la session utilisateur
);

CREATE TABLE data_2022_nov (
    event_time TIMESTAMP,         -- Timestamp pour les événements
    event_type VARCHAR(255),      -- Type d'événement (comme 'achat', 'vue', etc.)
    product_id BIGINT,            -- ID du produit, supposé être un entier long
    price DECIMAL(10, 2),         -- Prix, avec deux décimales pour les centimes
    user_id BIGINT,               -- ID de l'utilisateur, supposé être un entier long
    user_session UUID             -- UUID pour la session utilisateur
);


-- Pour créer une table items avec les colonnes product_id, category_id, category_code, et brand, 
-- vous pouvez utiliser le script SQL suivant. Je vais définir des types de données génériques pour 
-- ces colonnes, mais vous devrez peut-être les ajuster en fonction de la structure exacte de vos données :

CREATE TABLE items (
    product_id BIGINT,                 -- ID du produit, supposé être un entier long
    category_id BIGINT,                -- ID de la catégorie, supposé être un entier long
    category_code VARCHAR(255),        -- Code de la catégorie
    brand VARCHAR(255)                 -- Marque du produit
);


-- Ce script SQL crée une table avec les colonnes et les types de données suivants :

-- product_id : BIGINT, approprié pour les identifiants numériques de grande taille.
-- category_id : BIGINT, également pour un identifiant numérique de grande taille.
-- category_code : VARCHAR(255), pour des chaînes de caractères textuelles qui pourraient représenter des codes de catégorie.
-- brand : VARCHAR(255), pour les noms de marque.
-- Veillez à ajuster les types de données (VARCHAR, BIGINT) selon les spécificités et les besoins de votre dataset. Si par exemple 
-- category_code ou brand peuvent contenir des valeurs très longues, vous pourriez vouloir augmenter la taille du VARCHAR, ou si les 
-- valeurs sont courtes, la réduire pour optimiser l'utilisation de l'espace de stockage.


CREATE TABLE customers AS
SELECT
    e.event_time,
    e.event_type,
    p.product_id,
    p.price,
    u.user_id,
    u.user_session,
    c.category_id,
    c.category_code,
    p.brand
FROM
    events e
JOIN products p ON e.product_id = p.product_id
JOIN categories c ON p.category_id = c.category_id
JOIN users u ON e.user_id = u.user_id;


-- If you need to join multiple tables that have a similar structure into a single table called customers, you can do this
--  by using a UNION or UNION ALL statement in SQL. The UNION operator is used to combine the result sets of two or more SELECT statements.
--  It removes duplicate rows between the various SELECT statements. If you want to keep all duplicates, you would use UNION ALL.

-- Here's a general SQL template for how you might combine data_2020_*, data_2021_*, data_2022_*, etc., into a single table called customers. 
-- This assumes that all the data_202*_*** tables have the exact same column structure:

CREATE TABLE customers AS
SELECT * FROM data_2022_oct
UNION
SELECT * FROM data_2022_nov
UNION
SELECT * FROM data_2023_jan
-- Continue for all relevant tables
;


-- To combine the customers and items tables into a single customers table, you will need to perform a JOIN operation. This operation will merge 
-- rows from both tables based on a common column that exists in both tables. This common column is usually a primary key in one table and a foreign 
-- key in another, such as product_id or user_id.

-- Below is a SQL template to join the customers table with the items table. This example assumes that product_id is the common column between the 
-- two tables. Adjust the column names and join conditions according to the actual structure of your tables:

CREATE TABLE combined_customers AS
SELECT
    c.*,
    i.category_id,
    i.category_code,
    i.brand
FROM
    customers c
JOIN
    items i ON c.product_id = i.product_id;


-- In this SQL statement:

-- c.* selects all columns from the customers table.
-- i.category_id, i.category_code, and i.brand select the respective columns from the items table.
-- The JOIN clause merges rows from customers with matching rows from items based on the product_id column.
-- If you only want to include rows from customers that have a matching row in items, you would use an INNER JOIN. 
-- If you want to include all rows from customers and only combine data from items where it matches (leaving NULLs where there is no match), you would use a LEFT JOIN.

-- Please ensure you perform this operation during a period of low activity if you're working with large tables, and always back up your tables before 
-- running such significant operations to prevent data loss.