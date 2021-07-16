-- Lists all shows, and all genres linked to that show,
-- from the database hbtn_0d_tvshows.
SELECT m.title
FROM tv_shows m
JOIN tv_show_genres AS tv_sg
	ON tv_sg.show_id = m.id
JOIN tv_genres AS g
	ON tv_sg.genre_id = g.id
WHERE g.name = "Comedy"
ORDER BY m.title;
