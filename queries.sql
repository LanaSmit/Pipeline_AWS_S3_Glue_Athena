# Amazon Athena

SELECT track_name, album, popularity
FROM spotify_database.spotify
WHERE popularity > 80
ORDER BY popularity DESC;
