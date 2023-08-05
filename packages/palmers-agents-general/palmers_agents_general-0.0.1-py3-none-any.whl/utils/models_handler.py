import base64
import json
import os
import pickle
import sys
import requests

INFERENCE_URL = os.getenv('INFERENCE_END_POINT') # 20.85.61.212
INFERENCE_PREFIX = os.getenv('INFERENCE_PREFIX') # prod
INFERENCE_PROTOCOL = os.getenv('INFERENCE_PROTOCOL') # http
MESSAGE_MAX_SIZE = float(os.getenv('MESSAGE_MAX_SIZE') or (25 * 1024 * 1024)) # http value_if_true if condition else value_if_false




def send_to_models(data_dict):
    # is there a room to release memory here?
    # release memory

    # preprocessed data
    # collect metrics

    inference_results = {}
    for store in data_dict.keys():
        store_data = data_dict[store]
        df = store_data['data']
        model_url = store_data['model_url'] #serve/model_100_endpoint

        data_size = sys.getsizeof(df)
        print(f'store: {store}, data size: {data_size}')
        if data_size > MESSAGE_MAX_SIZE:
            raise Exception(f'error: store {store} data size > {MESSAGE_MAX_SIZE / (1024 * 1024)} MB')

        # send to model
        pickled = pickle.dumps(df)
        pickled_b64 = base64.b64encode(pickled)
        data_str = pickled_b64.decode('utf-8')
        url = f'{INFERENCE_PROTOCOL}://{INFERENCE_URL}/{INFERENCE_PREFIX}/{model_url}'  # Replace with your API endpoint

        if INFERENCE_PROTOCOL == 'http':
            data = {"body": {"features": data_str}}  # Data to be sent with the POST request

            response = requests.post(url, json=data)


        else:
            raise Exception('only http is supported')

        if response.status_code == 200:
            print(f'Model inference for store {store} successful!')
            response_dict = json.loads(response.text)
            predictions = pickle.loads(base64.b64decode(response_dict['body']['predictions'].encode()))
            inference_results[store] = predictions

        else :
            raise Exception(f'Model inference for store {store} failed!, status code: {response.status_code}')

    return inference_results
