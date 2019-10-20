drop schema main cascade; 

create schema main;

create table main.users (
	ID INT NOT NULL,
	FIRSTNAME TEXT NOT NULL,
	LASTNAME TEXT NOT NULL,
	EMAIL TEXT NOT NULL,
	USERNAME TEXT NOT NULL,
	PASSWORD TEXT NOT NULL,			 
	PRIMARY KEY (ID)
);
