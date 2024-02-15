-- lists all cities (cities.id, cities.name, states.names)
SELECT cities.id, cities.name, cities.name 
FROM cities LEFT JOIN states ON states.id = cities.state_id
ORDER BY cities.id;
