import pandas as pd
import requests as rqt
import json
import boto3


def lambda_handler(event, context):
    s3 = boto3.client(
        service_name='s3',
        aws_access_key_id='AKIA3L72EA2KADFNMXF7',
        aws_secret_access_key='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',
        region_name='us-east-1')

    bucket_name = 'data-lake-suellen'

    api_key = 'k_ohddqxdy'
    ids = ['tt6467266', 'tt14156154', 'tt15416668', 'tt11306376', 'tt13249198', 'tt12801262', 'tt2948372', 'tt5562070', 'tt7146812', 'tt15419420']

    filme_data = []

    for film_id in ids:
        url = f'https://imdb-api.com/en/API/Title/{api_key}/{film_id}'
        response = rqt.get(url)
        data = response.json()

        if 'awards' in data:
           filme = {
                'id': data['id'],
                'titulo': data['title'],
                'premiacao': data['awards'],
                'diretores':data['directors'],
                'imagem': data['image'],
                'enredo': data['plot'],
                'investimento': data['boxOffice']['budget'],
                'lucro_mundial': data['boxOffice']['cumulativeWorldwideGross'],
                'produtora':data['companies'],
            }
        filme_data.append(filme)

    json_data = json.dumps(filme_data)
    s3_client = boto3.client('s3')
    bucket_name = 'data-lake-suellen'
    file_name = 's3://data-lake-suellen/Raw/Local/IMDB/2023/06/20/hankingimdb.json'
    s3_client.put_object(Body=json_data, Bucket=bucket_name, Key=file_name)


    return {"statusCode": 200, "body": "Sucesso"}



