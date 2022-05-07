CREATE TABLE public.users(
    id SERIAL PRIMARY KEY,
    email text NOT NULL,
    password text NOT NULL
);

CREATE TABLE public.books (
	id SERIAL primary key,
	description text not null,
	title text not null,
	author text not null
);

ALTER TABLE IF EXISTS public.users
    OWNER to postgres;

ALTER TABLE IF EXISTS public.books
	OWNER to postgres;

INSERT INTO public.users(
	id, email, password)
	VALUES (1, 'epitech@gmail.com', '7ece99e593ff5dd200e2b9233d9ba654');