CREATE TABLE Item (
    item_id INT PRIMARY KEY, 
    item_name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE Stock (
    item_id INT PRIMARY KEY,
    item_quantity FLOAT NOT NULL DEFAULT 0,
    CONSTRAINT fk_stock_item
        FOREIGN KEY (item_id)
        REFERENCES Item(item_id)
);

CREATE TABLE Dishes (
    dish_id INT PRIMARY KEY, -- For PostgreSQL, you could use SERIAL PRIMARY KEY for auto-incrementing IDs
    dish_name VARCHAR(255) NOT NULL UNIQUE
);

-- This is a junction table to create a many-to-many relationship
-- between Dishes and Items.
CREATE TABLE Dish_Items (
    dish_id INT,
    item_id INT,
    PRIMARY KEY (dish_id, item_id),
    FOREIGN KEY (dish_id) REFERENCES Dishes(dish_id),
    FOREIGN KEY (item_id) REFERENCES Item(item_id)
);

INSERT INTO Item (item_id,item_name) 

VALUES
    (1,'Tomato'),
    (2,'Cabbage'),
    (3,'Carrot'),
    (4,'Cauliflower'),
    (5,'Spinach'),
    (6,'Brinjal'),
    (7,'Cucumber'),
    (8,'Beetroot'),
    (9,'Radish'),
    (10,'Chilli'),
    (11,'Garlic'),
    (12,'Ginger'),
    (13,'Potato'),
    (14,'Onions'),
    (15,'Lady-Fingers'),
    (16,'Bottle Gourd'),
    (17,'French-Beans');

INSERT INTO Item (item_id,item_name) 

VALUES
    (18,'Paneer'),
    (19,'Curd'),
    (20,'Wheat-Flour'),
    (21,'Rice');


SELECT * FROM Item;

INSERT INTO stock (item_id,item_quantity) 
VALUES
    (1,2.5),
    (2,1.5),
    (3,2),
    (4,2),
    (5,3),
    (6,3),
    (7,4),
    (8,4),
    (9,4),
    (10,5),
    (11,6),
    (12,6),
    (13,7),
    (14,7),
    (15,8),
    (16,8),
    (17,9);

-- Insert the dishes themselves
INSERT INTO Dishes (dish_id, dish_name)
VALUES
    (1, 'Tomato Soup'),
    (2, 'Cabbage Soup'),
    (3, 'Aalo-Bhindi Sabzi'),
    (4, 'Mixed Vegetable Curry'),
    (5, 'Aalo-Ghobi Sabzi'),
    (6, 'Palak Paneer'),
    (7, 'Baingan Bharta'),
    (8, 'Kachumber Salad'),
    (9, 'Beetroot Raita'),
    (10, 'Gajar-Halwa'),
    (11, 'Mooli Paratha'),
    (12, 'Chilli-Garlic Potato'),
    (13, 'Aloo Tikki'),
    (14, 'French Beans Stir Fry'),
    (15, 'Lauki Kofta Curry');

INSERT INTO Dish_Items (dish_id, item_id)
VALUES
    -- Tomato Soup (dish 1) uses Tomato (item 1)
    (1, 1),
    -- Cabbage Soup (dish 2) uses Cabbage (item 2)
    (2, 2),
    -- Potato-Lady-Finger Sabzi (dish 3) uses Potato (item 13) and Lady-Fingers (item 15)
    (3, 13),
    (3, 15),
    -- Mixed Vegetable Curry (dish 4) uses Carrot (item 3), Cauliflower (item 4), Peas (not in list)
    (4, 3),
    (4, 4),
    -- Spinach Curry (dish 5) uses Spinach (item 5)
    (5, 5),
    -- Baingan Bharta (dish 6) uses Brinjal (item 6)
    (6, 6),
    -- Palak Paneer (dish 7) uses Spinach (item 5)
    (7, 5),
    (7, 18),
    -- Kachumber Salad (dish 8) uses Cucumber (item 7), Tomato (item 1), Onion (item 14)
    (8, 7),
    (8, 1),
    (8, 14),
    -- Beetroot Raita (dish 9) uses Beetroot (item 8)
    (9, 8),
    (9, 19),
    -- Gajar-Halwa (dish 10) uses Wheat Flour (item 20), Rice (item 21)
    (10, 3),
    (10, 20),
    (10, 21),
    -- Mooli Paratha (dish 11) uses Wheat Flour (item 20)
    (11, 20),
    (11, 9),
    -- Chilli-Garlic Potato (dish 12) uses Potato (item 13)
    (12, 13),
    (12, 10),
    (12, 11),
    -- Aloo Tikki (dish 13) uses Potato (item 13)
    (13, 13),
    (13, 12),
    -- French Beans Stir Fry (dish 14) uses French Beans (item 17)
    (14, 17),
    (14, 10),
    (14, 11),
    -- Lauki Kofta Curry (dish 15) uses Spinach (item 5)
    (15, 16),
    (15, 5);