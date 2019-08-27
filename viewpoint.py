from psycopg2 import connect, sql


class Viewpoint:

    def __int__(self):
        connection = connect()

    def get_unprocessed_viewpoints(self):
        """ Creates a new project_document in database """
        return []

    def set_viewpoint_as_processed(self, id, image_file, peaks_file):
        """ Helper method that allows app to persist the current state of a project_document """
        pass
