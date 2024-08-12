"""
SQLite CRUD Class
"""

from sqlite3 import Connection


class SQLiteCRUD:
    """
    Class to handle all basic SQLite CRUD operations
    """

    def __init__(self, db_connection: Connection):
        self.conn = db_connection

    def create_many(
        self,
        table: str,
        columns: tuple[str],
        insert_values: list[tuple[str]],
        where: tuple[str, str] = ("", ""),
    ):
        """
        Function for creating and inserting many values into a database
        """
        if isinstance(insert_values, list):
            columns_str = ", ".join(columns)
            placeholders = ", ".join(["?"] * len(insert_values[0]))
            sql_cmd = f"""
                INSERT INTO {table} ({columns_str})
                VALUES ({placeholders})
                """

            if where[0]:
                sql_cmd += f"\nWHERE {where[0]} = ?"
                self.conn.executemany(
                    sql_cmd,
                    [(*insert_value, where[1]) for insert_value in insert_values],
                )

            else:
                self.conn.executemany(sql_cmd, insert_values)

        else:
            raise TypeError("insert_values must be a list of tuples of strings")

    def create_one(
        self,
        table: str,
        columns: tuple[str],
        insert_values: tuple[str],
        where: tuple[str, str] = ("", ""),
    ):
        """
        Function for creating and inserting values into a database
        """
        if isinstance(insert_values, tuple):
            columns_str = ", ".join(columns)
            placeholders = ", ".join(["?"] * len(insert_values))
            sql_cmd = f"""
                INSERT INTO {table} ({columns_str})
                VALUES ({placeholders})
                """

            if where[0]:
                sql_cmd += f"\nWHERE {where[0]} = ?"
                self.conn.execute(
                    sql_cmd,
                    (*insert_values, where[1]),
                )

            else:
                self.conn.execute(sql_cmd, insert_values)

        else:
            raise TypeError("insert_values must be a tuple of strings")

    def read(self):
        """
        Function for retriewing and selecting items from a database
        """

    def update(self):
        """
        Function for updating items already within a database
        """

    def delete(self):
        """
        Function for deleting items from a database
        """
