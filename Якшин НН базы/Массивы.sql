create table posts(
 id serial primary key,
 title varchar(30),
 body text,
 tags varchar(10)[]
);

insert into posts(title, body, tags)
values ('Post Title', 'Post Text',
'{"sql", "postgres", "database", "plsql"}');

select * from posts;