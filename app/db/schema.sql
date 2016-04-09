drop table if exists members;
   create table memebers (
     id integer primary key autoincrement,
     firstName full not null,
     lastName text not null
);