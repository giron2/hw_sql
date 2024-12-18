
--Название и продолжительность самого длительного трека.
SELECT name, duration FROM track
WHERE duration = (SELECT  MAX(duration) FROM track);

--Название треков, продолжительность которых не менее 3,5 минут.
SELECT name FROM track
WHERE duration >= 210;

--Названия сборников, вышедших в период с 2018 по 2020 год включительно.
SELECT name FROM collection
WHERE year >= 2018 AND year <= 2020;

--Исполнители, чьё имя состоит из одного слова.
SELECT name FROM artist
WHERE name NOT LIKE '% %';


--Название треков, которые содержат слово «мой» или «my»
SELECT name FROM track
WHERE LOWER(name) LIKE '% my %' 
OR LOWER(name) LIKE 'my %'
OR LOWER(name) LIKE '% my'
OR LOWER(name) LIKE 'my'
OR LOWER(name) LIKE 'мой %'
OR LOWER(name) LIKE '% мой'
OR LOWER(name) LIKE 'мой'
OR LOWER(name) LIKE '% мой %';


--Количество исполнителей в каждом жанре.
SELECT genre_id, COUNT(*) FROM genre_artist
GROUP BY genre_id
ORDER BY COUNT(*) DESC;


--Количество треков, вошедших в альбомы 2019–2020 годов.
SELECT COUNT (*)
FROM track 
JOIN album 
ON track.album=album.id
WHERE album.year >= 2019 AND album.year <= 2020;


--Средняя продолжительность треков по каждому альбому.
SELECT album.name, AVG(track.duration)
FROM track 
JOIN album 
ON track.album=album.id
GROUP BY album.name;

--Все исполнители, которые не выпустили альбомы в 2020 году.
SELECT DISTINCT artist.name
FROM artist
WHERE artist.name NOT IN ( SELECT artist.name
FROM artist
JOIN album_artist  ON artist.id=album_artist.artist_id
JOIN album ON album.id=album_artist.album_id
WHERE album.year = 2020);


--Названия сборников, в которых присутствует конкретный исполнитель (выберите его сами).
SELECT DISTINCT collection.name
FROM collection  
JOIN track_collection  ON collection.id=track_collection.collection_id
JOIN track  ON track.id=track_collection.track_id
JOIN album  ON album.id=track.album
JOIN album_artist  ON album.id=album_artist.album_id
JOIN artist  ON artist.id=album_artist.artist_id
WHERE artist.name = 'artist_2';

--Названия альбомов, в которых присутствуют исполнители более чем одного жанра.
SELECT album.name, genre_artist.artist_id, count(genre_artist.genre_id)
FROM genre_artist
JOIN artist  ON artist.id=genre_artist.artist_id
JOIN album_artist  ON artist.id=album_artist.artist_id
JOIN album ON album.id=album_artist.album_id
GROUP BY genre_artist.artist_id, album.name
HAVING COUNT(genre_artist.genre_id) > 1;
