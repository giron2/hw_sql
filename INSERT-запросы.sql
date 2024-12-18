INSERT INTO album VALUES (1, 'album_1', 2000);
INSERT INTO album VALUES (2, 'album_2', 2010);
INSERT INTO album VALUES (3, 'album_3', 2019);
INSERT INTO album VALUES (4, 'album_4', 2020);

INSERT INTO track VALUES (1, 'track_1', 180, 1);
INSERT INTO track VALUES (2, 'track_2', 360, 1);
INSERT INTO track VALUES (3, 'my_track_3', 222, 2);
INSERT INTO track VALUES (4, 'track_4', 323, 3);
INSERT INTO track VALUES (5, 'track_5', 155, 3);
INSERT INTO track VALUES (6, 'track_6 my', 340, 4);
INSERT INTO track VALUES (7, 'my track_6', 310, 4);
INSERT INTO track VALUES (8, 'track my 6', 340, 4);
INSERT INTO track VALUES (9, 'my', 240, 4);
INSERT INTO track VALUES (10, 'track_7', 215, 4);
INSERT INTO track VALUES (11, 'track_6 мой', 340, 4);
INSERT INTO track VALUES (12, 'мой track_6', 310, 4);
INSERT INTO track VALUES (13, 'track мой 6', 340, 4);
INSERT INTO track VALUES (14, 'МОЙ', 240, 4);

INSERT INTO genre VALUES (1, 'genre_1');
INSERT INTO genre VALUES (2, 'genre_2');
INSERT INTO genre VALUES (3, 'genre_3');
INSERT INTO genre VALUES (4, 'genre_4');

INSERT INTO artist VALUES (1, 'artist_1');
INSERT INTO artist VALUES (2, 'artist_2');
INSERT INTO artist VALUES (3, 'best artist_3');
INSERT INTO artist VALUES (4, 'artist_4');
INSERT INTO artist VALUES (5, 'artist_5');

INSERT INTO collection VALUES (1, 'collection_1', 2000);
INSERT INTO collection VALUES (2, 'collection_2', 2010);
INSERT INTO collection VALUES (3, 'collection_3', 2019);
INSERT INTO collection VALUES (4, 'collection_4', 2020);
INSERT INTO collection VALUES (5, 'collection_5', 2020);

INSERT INTO genre_artist VALUES (1, 1);
INSERT INTO genre_artist VALUES (1, 2);
INSERT INTO genre_artist VALUES (3, 1);
INSERT INTO genre_artist VALUES (1, 3);
INSERT INTO genre_artist VALUES (2, 5);
INSERT INTO genre_artist VALUES (4, 4);

INSERT INTO album_artist VALUES (1, 5);
INSERT INTO album_artist VALUES (1, 2);
INSERT INTO album_artist VALUES (3, 3);
INSERT INTO album_artist VALUES (4, 1);
INSERT INTO album_artist VALUES (1, 1);
INSERT INTO album_artist VALUES (3, 1);

INSERT INTO track_collection VALUES (1, 5);
INSERT INTO track_collection VALUES (1, 2);
INSERT INTO track_collection VALUES (2, 3);
INSERT INTO track_collection VALUES (3, 1);
INSERT INTO track_collection VALUES (3, 3);
INSERT INTO track_collection VALUES (6, 4);
INSERT INTO track_collection VALUES (4, 4);
INSERT INTO track_collection VALUES (7, 5);
INSERT INTO track_collection VALUES (3, 2);