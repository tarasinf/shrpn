from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build
from datetime import datetime
from django.conf import settings


class GoogleFusionTableManager:
    def __init__(self, table_id):
        self.table_id = table_id
        scopes = ['https://www.googleapis.com/auth/fusiontables']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(settings.SERVICE_ACCOUNT_CREDENTIAL_FILE_PATH,
                                                                       scopes)
        self.fusiontables = build('fusiontables', 'v2', credentials=credentials)

    def _execute_row_sql(self, sql):
        return self.fusiontables.query().sql(sql=sql).execute()

    def create(self, address):
        return self._execute_row_sql(sql="INSERT INTO {} ('Address', 'Location', 'Date') VALUES ('{}', '{}', '{}');"
                                     .format(self.table_id, address.encode('utf-8'), address.encode('utf-8'),
                                             unicode(datetime.now())))

    def get_all(self):
        # TODO handle error
        response = self._execute_row_sql(sql="SELECT * FROM {};".format(self.table_id))
        return response.get('rows', [])

    def exist_by_address(self, address):
        return 'rows' in self._execute_row_sql(sql="SELECT * from {} WHERE 'Addredd'='{}';"
                                               .format(self.table_id, address))

    def delete_all(self):
        return self._execute_row_sql(sql="DELETE FROM {};".format(self.table_id))
