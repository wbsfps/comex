import os
import psycopg

try:
    conn = psycopg.connect(
        dbname=os.getenv("dbname"),
        user=os.getenv("user"),
        password=os.getenv("password"),
        host=os.getenv("host"),
        port=os.getenv("port"),
    )

    with conn.cursor() as cur:
        cur.execute("SELECT version();")
        
        version = cur.fetchone()[0]
        print("Versão do banco de dados PostgreSQL:", version)
        
        cur.execute("SELECT * FROM public.blocos_economicos;")
        rows = cur.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("Nenhum dado encontrado na tabela.")

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    if conn:
        conn.close()
        print("Conexão fechada.")