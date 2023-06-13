import json

from pyapacheatlas.auth import BasicAuthentication
from pyapacheatlas.core import AtlasClient

auth = BasicAuthentication(
    username="admin",
    password="admin"
)

client = AtlasClient(
    endpoint_url="http://172.17.204.37:21000/api/atlas/v2",
    authentication=auth
)

from pyapacheatlas.readers import ExcelConfiguration, ExcelReader

ec = ExcelConfiguration()
reader = ExcelReader(ec)

entities = reader.parse_bulk_entities("./demo.xlsx")

results = client.upload_entities(entities)




