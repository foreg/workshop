--
-- PostgreSQL database dump
--

-- Dumped from database version 11.1
-- Dumped by pg_dump version 11.1

-- Started on 2019-03-09 21:07:24

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 2848 (class 1262 OID 16531)
-- Name: workshop; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE workshop WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Russian_Russia.1251' LC_CTYPE = 'Russian_Russia.1251';


ALTER DATABASE workshop OWNER TO postgres;

\connect workshop

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 196 (class 1259 OID 16532)
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- TOC entry 198 (class 1259 OID 16539)
-- Name: client; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.client (
    id integer NOT NULL,
    "FIO" character varying(100),
    email character varying(120)
);


ALTER TABLE public.client OWNER TO postgres;

--
-- TOC entry 197 (class 1259 OID 16537)
-- Name: client_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.client_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.client_id_seq OWNER TO postgres;

--
-- TOC entry 2849 (class 0 OID 0)
-- Dependencies: 197
-- Name: client_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.client_id_seq OWNED BY public.client.id;


--
-- TOC entry 202 (class 1259 OID 16556)
-- Name: request; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.request (
    id integer NOT NULL,
    client_id integer NOT NULL,
    service_id integer NOT NULL,
    date timestamp without time zone
);


ALTER TABLE public.request OWNER TO postgres;

--
-- TOC entry 201 (class 1259 OID 16554)
-- Name: request_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.request_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.request_id_seq OWNER TO postgres;

--
-- TOC entry 2850 (class 0 OID 0)
-- Dependencies: 201
-- Name: request_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.request_id_seq OWNED BY public.request.id;


--
-- TOC entry 200 (class 1259 OID 16548)
-- Name: service; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.service (
    id integer NOT NULL,
    name character varying(100),
    price double precision
);


ALTER TABLE public.service OWNER TO postgres;

--
-- TOC entry 199 (class 1259 OID 16546)
-- Name: service_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.service_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.service_id_seq OWNER TO postgres;

--
-- TOC entry 2851 (class 0 OID 0)
-- Dependencies: 199
-- Name: service_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.service_id_seq OWNED BY public.service.id;


--
-- TOC entry 2701 (class 2604 OID 16542)
-- Name: client id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.client ALTER COLUMN id SET DEFAULT nextval('public.client_id_seq'::regclass);


--
-- TOC entry 2703 (class 2604 OID 16559)
-- Name: request id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.request ALTER COLUMN id SET DEFAULT nextval('public.request_id_seq'::regclass);


--
-- TOC entry 2702 (class 2604 OID 16551)
-- Name: service id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service ALTER COLUMN id SET DEFAULT nextval('public.service_id_seq'::regclass);


--
-- TOC entry 2836 (class 0 OID 16532)
-- Dependencies: 196
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.alembic_version (version_num) VALUES ('070ea1a058d0');


--
-- TOC entry 2838 (class 0 OID 16539)
-- Dependencies: 198
-- Data for Name: client; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.client (id, "FIO", email) VALUES (4, 'Petrov Petr Petrovich', 'petrov@mail.ru');
INSERT INTO public.client (id, "FIO", email) VALUES (16, 'Sidorov Sidor Sidorovich', 'sidorov@mail.ru');
INSERT INTO public.client (id, "FIO", email) VALUES (5, 'Ivanov Ivan Ivanovich', 'ivanov@mail.ru');


--
-- TOC entry 2842 (class 0 OID 16556)
-- Dependencies: 202
-- Data for Name: request; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.request (id, client_id, service_id, date) VALUES (2, 5, 1, '2019-03-09 15:12:52.765715');
INSERT INTO public.request (id, client_id, service_id, date) VALUES (4, 16, 1, '2019-03-09 15:27:17.694753');
INSERT INTO public.request (id, client_id, service_id, date) VALUES (7, 16, 1, '2019-03-09 15:34:58.442786');
INSERT INTO public.request (id, client_id, service_id, date) VALUES (1, 5, 2, '2019-03-09 15:11:48');


--
-- TOC entry 2840 (class 0 OID 16548)
-- Dependencies: 200
-- Data for Name: service; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.service (id, name, price) VALUES (2, 'service 2', 200);
INSERT INTO public.service (id, name, price) VALUES (3, 'service 3', 300);
INSERT INTO public.service (id, name, price) VALUES (1, 'service 1 edited', 100);


--
-- TOC entry 2852 (class 0 OID 0)
-- Dependencies: 197
-- Name: client_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.client_id_seq', 17, true);


--
-- TOC entry 2853 (class 0 OID 0)
-- Dependencies: 201
-- Name: request_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.request_id_seq', 7, true);


--
-- TOC entry 2854 (class 0 OID 0)
-- Dependencies: 199
-- Name: service_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.service_id_seq', 4, true);


--
-- TOC entry 2705 (class 2606 OID 16536)
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- TOC entry 2707 (class 2606 OID 16544)
-- Name: client client_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.client
    ADD CONSTRAINT client_pkey PRIMARY KEY (id);


--
-- TOC entry 2712 (class 2606 OID 16561)
-- Name: request request_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.request
    ADD CONSTRAINT request_pkey PRIMARY KEY (id);


--
-- TOC entry 2710 (class 2606 OID 16553)
-- Name: service service_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service
    ADD CONSTRAINT service_pkey PRIMARY KEY (id);


--
-- TOC entry 2708 (class 1259 OID 16545)
-- Name: ix_client_email; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_client_email ON public.client USING btree (email);


--
-- TOC entry 2714 (class 2606 OID 16577)
-- Name: request request_client_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.request
    ADD CONSTRAINT request_client_id_fkey FOREIGN KEY (client_id) REFERENCES public.client(id) ON DELETE RESTRICT;


--
-- TOC entry 2713 (class 2606 OID 16572)
-- Name: request request_service_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.request
    ADD CONSTRAINT request_service_id_fkey FOREIGN KEY (service_id) REFERENCES public.service(id) ON DELETE RESTRICT;


-- Completed on 2019-03-09 21:07:25

--
-- PostgreSQL database dump complete
--

