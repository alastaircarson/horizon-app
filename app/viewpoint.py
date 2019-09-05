from psycopg2 import connect


class Viewpoint:

    def __init__(self):
        self.conn = connect("dbname='lcdev' user='postgres' host='192.168.16.16' password='XXX'")
        self.cursor = self.conn.cursor()

    def get_unprocessed_viewpoints(self):
        sql_get_unprocessed = """
            select id, st_x(geometry) as x, st_y(geometry) as y
            from viewpoint where not processed
            """
        self.cursor.execute(sql_get_unprocessed)
        rows = self.cursor.fetchall()
        return [{"id": row[0], "x":row[1], "y":row[2]} for row in rows]

    def set_viewpoint_as_processed(self, id, image_file, peaks_file):
        sql_set_processed = """
            update viewpoint
            set processed = true, image_file = %(image_file)s, peaks_file = %(peaks_file)s
            where id = %(id)s;
            """
        # params = {"vid": vid, "image_file": image_file, "peaks_file": peaks_file}
        try:
            print(f"update record: {id}")
            self.cursor.execute(sql_set_processed, {"id": id, "image_file": image_file, "peaks_file": peaks_file})
            self.conn.commit()
            print(f"updated record: {id}")
        except Exception as e:
            print(f"error {str(e)}")
