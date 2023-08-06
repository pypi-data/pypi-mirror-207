import pandas as pd
import boto3
import os
from datetime import datetime

class Data:

    dynamo = None

    def __init__(self):
        self.dynamo = boto3.resource('dynamodb')


    def get_data(self, table_name):
        table = self.dynamo.Table(table_name)
        response = table.scan()
        return response['Items']
    
    def save_data(self, data, output_format, table_name):
        df = pd.DataFrame(data)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        cur_dir = os.getcwd()
        filename = f"{cur_dir}/{table_name}-{timestamp}.{output_format}"

        if output_format == "csv":
            df.to_csv(filename, index=False)
        if output_format == "json":
            df.to_json(filename)
        if output_format == "xlsx":
            df.to_excel(filename, index=False)
