CREATE TABLE visita (
     id integer primary key autoincrement,
     email text not null,
     fecha text not null,
     atendido integer null default 0     
);

CREATE UNIQUE INDEX idxVisita ON visita(email, fecha);


