from io import BytesIO

import pandas as pd
from azure.storage.blob import BlobServiceClient


def read_df_from_blob(connection_string, container_name, blob_name):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name, snapshot=None)

    download_stream = blob_client.download_blob()
    csv_file = download_stream.content_as_text(encoding='utf-8-sig')
    file = BytesIO(csv_file.encode())
    df = pd.read_csv(file)


    return df


def save_df_to_blob(connection_string, container_name, blob_name, df):
    """
    We assume dfs is a list of dataframes
    """

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    blob_client.upload_blob(data=df, blob_type='BlockBlob')
    return True

