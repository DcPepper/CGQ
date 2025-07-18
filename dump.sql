--
-- PostgreSQL database dump
--

-- Dumped from database version 17.5 (Debian 17.5-1.pgdg120+1)
-- Dumped by pg_dump version 17.5 (Debian 17.5-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: quiz_japanese; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.quiz_japanese (
    id bigint NOT NULL,
    fr text NOT NULL,
    furigana text NOT NULL,
    kanji text NOT NULL,
    romaji text NOT NULL,
    difficulty integer NOT NULL,
    category character varying(50) NOT NULL
);


ALTER TABLE public.quiz_japanese OWNER TO "user";

--
-- Name: quiz_japanese_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

ALTER TABLE public.quiz_japanese ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.quiz_japanese_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Data for Name: quiz_japanese; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.quiz_japanese (id, fr, furigana, kanji, romaji, difficulty, category) FROM stdin;
1	excusez-moi	ÒüÖÒü┐Òü¥ÒüøÒéô		sumimasen	1	expression
2	o├╣	Òü®Òüô		doko	1	base
3	nous	Òü╝ÒüÅÒüƒÒüí		bokutachi	1	base
4	maison	ÒüåÒüí		uchi	1	vocabulaire
5	tout pr├¿s	ÒüÖÒüÉÒüíÒüïÒüÅ		suguchikaku	1	expression
6	 ensemble	ÒüäÒüúÒüùÒéç Òü½		issho ni	1	expression
7	aller	ÒüäÒüÅ		iku	1	verbe
8	par ici	ÒüôÒüúÒüí		kocchi	1	expression
9	oui	Òü»Òüä		hai	1	base
10	gare	ÒüêÒüì		eki	1	vocabulaire
11	superette	ÒüôÒéôÒü│Òü½		konbini	1	vocabulaire
12	pluie	ÒüéÒéü		ame	1	vocabulaire
13	on est de retour	ÒüƒÒüáÒüäÒü¥		tadaima	1	expression
14	nouveau	ÒüéÒüƒÒéëÒüù		atarashi	1	adjectif
15	r├®sident	ÒüÿÒéàÒüåÒü½Òéô		juunin	1	vocabulaire
16	arriver	ÒüñÒüÅ		tsuku	1	verbe
17	propri├®atire	ÒüèÒüåÒéä		ooya	1	vocabulaire
18	├®tudiant	ÒüîÒüÅÒüøÒüä		gakusee	1	vocabulaire
19	employ├®	ÒüïÒüäÒüùÒéâÒüäÒéô		kaishain	1	vocabulaire
20	enseignante	ÒüìÒéçÒüåÒüù		kyooshi	1	vocabulaire
21	beaucoup	ÒüƒÒüÅÒüòÒéô		takusan	1	vocabulaire
22	manger	ÒüƒÒü╣Òéï		taberu	1	verbe
23	venir	ÒüÅÒéï		kuru	1	verbe
24	photographe	ÒüùÒéâÒüùÒéôÒüï		shashinka	1	vocabulaire
25	je	Òü╝ÒüÅ		boku	1	base
26	savoir	ÒüùÒüúÒüª ÒüäÒéï		shitte iru	1	verbe
27	je viens de	ÒüïÒéë ÒüìÒü¥ÒüùÒüƒ		kara kimashita	1	expression
28	je suis de	ÒüïÒéë ÒüºÒüÖ		kara desu	1	expression
29	thailande	ÒüƒÒüä		tai	1	vocabulaire
30	bresil	ÒüÂÒéëÒüÿÒéï		burajiru	1	vocabulaire
31	ah bon	ÒüØÒüå ÒüºÒüÖ Òüï		soo desu ka	1	expression
32	je (poli)	ÒéÅÒüƒÒüÅÒüù		watakushi	1	base
\.


--
-- Name: quiz_japanese_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.quiz_japanese_id_seq', 33, true);


--
-- Name: quiz_japanese quiz_japanese_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.quiz_japanese
    ADD CONSTRAINT quiz_japanese_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

