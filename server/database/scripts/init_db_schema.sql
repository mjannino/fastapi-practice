CREATE TABLE IF NOT EXISTS users(
  id SERIAL NOT NULL PRIMARY KEY
 ,email TEXT
 ,is_active BOOLEAN
);

CREATE TABLE IF NOT EXISTS items(
  id SERIAL NOT NULL PRIMARY KEY
 ,title TEXT
 ,description BOOLEAN
 ,owner_id INTEGER
);

ALTER TABLE items
    ADD CONSTRAINT 'items_users_fk' FOREIGN KEY (owner_id) REFERENCES users (id);