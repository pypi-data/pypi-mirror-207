import inquirer
import boto3
import os
from ..services.data import Data

def download_data():
    try:
        dynamo = boto3.resource('dynamodb')
        tables = [table.name for table in dynamo.tables.all()]

        questions = [
            inquirer.List('table',
                        message="Select a table",
                        choices=tables,
                        autocomplete=True,
                        carousel=True,
                        ),
            inquirer.List('output_format',
                        message="Select output format",
                        choices=["csv", "json", "xlsx"],
                        ),
            
        ]
        answers = inquirer.prompt(questions)
        d = Data()
        data = d.get_data(answers['table'])
        d.save_data(data, answers['output_format'], answers['table'])
        print("Data saved successfully")
    except Exception as e:
        print("Error: ", e)