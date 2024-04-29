import psycopg2 as pgsql

connection = pgsql.connect(host="localhost", dbname="postgres", user="postgres", 
                         password="mumbik112233", port=5433)
cur = connection.cursor()

cur.execute("""CREATE OR REPLACE FUNCTION search_from_pb_byname(a character varying)
  RETURNS SETOF PhoneBook
AS
$$
SELECT * 
FROM PhoneBook 
WHERE first_name=a;
$$
language sql;
""")





cur.execute("""CREATE OR REPLACE PROCEDURE insert_to_pb(a character varying, b character varying, c integer)
LANGUAGE plpgsql
AS $$
DECLARE v_exists INTEGER;
BEGIN
    SELECT into v_exists (SELECT count(*) FROM public.PhoneBook WHERE first_name = b AND last_name=a);
    IF v_exists=0 THEN
        INSERT INTO public.PhoneBook (last_name, first_name, phone_number) values(a, b, c);
    END IF;
	IF v_exists IS NOT NULL THEN
        UPDATE public.PhoneBook
		SET phone_number = c
		WHERE last_name = a AND first_name=b;
    END IF;
END;
$$;
""")




cur.execute("""CREATE OR REPLACE PROCEDURE insert_loop()
LANGUAGE plpgsql
AS $$
DECLARE
   m   text[];
   num int;
   arr text[] := '{{Muhammed, Ali, 123456789},{Bruce, Lee, 12312346465}}'; 
BEGIN
   FOREACH m SLICE 1 IN ARRAY arr
   LOOP
      SELECT INTO num CAST(m[3] AS INTEGER);
      INSERT INTO PhoneBook (last_name, first_name, phone_number) values(m[1],m[2],num);
   END LOOP;
END
$$;""")




cur.execute("""CREATE OR REPLACE FUNCTION paginating(a integer, b integer)
RETURNS SETOF PhoneBook
AS $$
    SELECT * FROM PhoneBook 
	ORDER BY last_name
	LIMIT a OFFSET b;
$$
language sql;""")






cur.execute("""CREATE OR REPLACE PROCEDURE delete_from_pb(a character varying, b character varying)
LANGUAGE plpgsql
AS $$
DECLARE v_exists INTEGER;
BEGIN
    SELECT into v_exists (SELECT count(*) FROM public.PhoneBook WHERE first_name = b AND last_name=a);
	IF v_exists IS NOT NULL THEN
        DELETE FROM PhoneBook
		WHERE last_name=a AND first_name=b;
    END IF;
END;
$$;""")







cur.execute("""CALL insert_to_pb('Mike','Tyson',465465654);
""")
cur.execute("""SELECT *
FROM search_from_pb_byname('lol');""")
print(cur.fetchall())
cur.execute("""CALL insert_to_pb('pip', 'pup', 66);""")
cur.execute("""SELECT *
FROM paginating(5, 2);""")
print(cur.fetchall())
cur.execute("""CALL delete_from_pb('Mike', 'Tyson');""")
cur.execute("""CALL insert_loop();""")


connection.commit()
cur.close()
connection.close()
