import psycopg2
import pandas as pd

class GlobalVar():
    def __init__(self, host, dbname, user, password):
        self.conn = psycopg2.connect(
            host=host,
            dbname=dbname,
            user=user,
            password=password
        )
        self.cur = self.conn.cursor()
        
    # Other methods
    
    def add_or_update_column(self, chat_id, column_name, new_value):
        # check if the record with given chat_id is present or not
        self.cur.execute(f"SELECT * FROM global_var WHERE chat_id = '{chat_id}'")
        record = self.cur.fetchone()
        
        if record:
            # update the column
            self.cur.execute(f"UPDATE global_var SET {column_name} = '{new_value}' WHERE chat_id = '{chat_id}'")
            self.conn.commit()
            print(f"Record with chat_id {chat_id} updated successfully")
        else:
            # insert new record
            self.cur.execute(f"INSERT INTO global_var (chat_id, {column_name}) VALUES ('{chat_id}', '{new_value}')")
            self.conn.commit()
            print(f"Record with chat_id {chat_id} inserted successfully")

    def fetch_column(self,column_name):
        # check if the record with given chat_id is present or not
        self.cur.execute(f"SELECT {column_name} FROM applicants")
        record = self.cur.fetchall()
        
        if record:
            return list(record)
        else:
            return None
        

    def get_data(self,table_name):
        query = f"SELECT * FROM {table_name}"
        return pd.read_sql(query, self.conn)

    def insert_applicant(self,applicant_data,uid):

        # Build the INSERT statement
        sql = "INSERT INTO applicants (id,name, email, pan, location, exp, edu,role) VALUES (%s,%s, %s, %s, %s, %s, %s,%s)"
        values = (uid,applicant_data['name'], applicant_data['email'], applicant_data['pan'], applicant_data['location'], applicant_data['exp'], applicant_data['edu'], applicant_data['role'])

        # Execute the statement
        self.cur.execute(sql, values)

        # Commit the changes to the database
        self.conn.commit()

        # Close the cursor and connection
        # self.cur.close()
        # self.conn.close()

    def upload_data(self,data,id,role):
        try:

            
            # insert data into the faq table
            for question, answer in data.items():
                self.cur.execute("INSERT INTO faq(id,question, answer,role) VALUES(%s,%s,%s, %s)",
                                (id,question, answer,role))
            
            # save changes to the database
            self.conn.commit()
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
