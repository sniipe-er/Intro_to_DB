import mysql.connector


def create_database():
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Sayf@20056"
        )

        if connection.is_connected:
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")


if __name__ == "__main__":
    create_database()