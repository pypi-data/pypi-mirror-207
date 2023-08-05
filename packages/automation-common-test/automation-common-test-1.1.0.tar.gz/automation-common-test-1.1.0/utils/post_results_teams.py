#!/usr/bin/env python3
from cgi import test
from datetime import datetime
import json
import os
import pandas as pd
import requests
from performance_test_platform.utils.encryption import decrypt
import shutil
from performance_test_platform.helpers.yaml_files_parser import get_credentials_from_yaml_file, get_utils_config_from_yaml_file

"""
-------------------------------------------------------------------
Convert the CSV files and post into Teams channel
-------------------------------------------------------------------
"""


HOOK_URL = ""

# MCMP Apps Prefix
APPS_PREFIX = None
# Status to report in the post
STATUS = [
    {"key": "passed", "text": "Passed (Response times lower than 5 sec. and 0% of HTTP errors)", "description": "passed", "color": "#2DC440", "hide": True}, 
    {"key": "failed_response_times", "text": "Failed by Response Times (Response times greater than 5 sec.)", "description": "Failed by Response Times (Response times greater than 5 sec.)", "color": "#C0392B", "hide": False},
    {"key": "failed_with_errors", "text": "Failed by HTTP Error Percentage (Percentage of HTTP errors greater than 5%) ", "description": "Failed by HTTP Errors (Percentage of HTTP errors greater than 5%)",  "color": "#E74C3C","hide": False}
]
ENVS = None

def _set_config_variables():
    """Set config variables for the script to process the results
    """    
    global  ENVS, APPS_PREFIX
    config = get_utils_config_from_yaml_file("post_messaging_app")
    ENVS = config["envs"]
    APPS_PREFIX = config["apps_prefix"]

_set_config_variables()

# Main structure of the formatted data
RESULTS = {
    "release": "",
    "environment": "",
    **{ f"total_{status['key']}": 0 for status in STATUS},
    "tests_total": 0,
    "results": [],
}

# Supported environment with descriptions


_temp_folder = "__perf_results__"
_temp_path = ""


def get_transaction_status(trx):
    """Get the status of one transaction

    Args:
        trx (dict): transaction to get the status

    Returns:
        str: status of the transaction
    """    
    error_perc = trx["errorpct"]
    res_time = trx["meantime"]
    req_type = trx["type"]
    status = STATUS[0]["key"]
    if res_time > 5 and req_type !="CUSTOM":
         status = STATUS[1]["key"]
    elif error_perc > 5:
        status = STATUS[2]["key"]
    RESULTS[f"total_{status}"]+=1
    return status
   
    
def get_percentage_by_app():
    """Calculate the percentage of errors by application
    """    
    for result in RESULTS["results"]:
        for status in STATUS:
            result[f"{status['key']}_percentage"] = round(((len(result[f"{status['key']}_steps"]) / result["steps_count"]) * 100), 2)


def process_data(file_path, release, env):
    """Process the data to generate statistics and format it

    Args:
        file_path (str): path of the file to parse
        release (str): release date
        env (str): name of environment

    Raises:
        Exception: file does not match with apps prefixes
    """    
    RESULTS["release"] = datetime.strftime(release,'%m-%d-%Y')
    RESULTS["environment"] = env
    df = pd.read_csv(file_path)
    current_app = ""
    for prefix in APPS_PREFIX:
        if prefix.lower() in file_path.lower():
            current_app = prefix
            break
    if not current_app:
        raise Exception(f'This file does not match with apps prefixes. File: {file_path}')
    for _, row in df.iterrows():
        res_index = -1
        for i, item in enumerate(RESULTS["results"]):
            if item.get('app') == current_app:
                res_index = i
                break
        if res_index == -1:
            RESULTS["results"].append({
                "app": current_app,
                **{ f"{status['key']}_steps": [] for status in STATUS},
                "steps_count": 0
            })
            res_index = len(RESULTS["results"]) - 1       
        status = get_transaction_status(row)  
        RESULTS["results"][res_index][f"{status}_steps"].append(row["transaction"])
        RESULTS["results"][res_index]["steps_count"]+=1   
        RESULTS["tests_total"]+=1  
    get_percentage_by_app()
    
    
def build_teams_payload(suite_name):
    """Build the Teams message structure to be sent

    Returns:
        dict: payload
    """   
    payload = {
        "summary": "MCMP Performance Testing",
    }
    body = []
    body.append( {   
                    "type": "TextBlock",
                    "text": f"""
                        **Test Suite**: {suite_name} \n
                        **Environment**: {RESULTS['environment']} \n
                        **Release**: {RESULTS['release']} \n
                        **Apps**: {','.join(result['app'] for result in RESULTS['results'])} \n
                        **Num vUser**: {ENVS[RESULTS['environment']]['users_summary']} \n
                        **Think time**: {ENVS[RESULTS['environment']]['think_time']} \n
                        **Total # of HTTP Transactions**: {RESULTS['tests_total']}  \n
                    """
                })
    for status in STATUS:
        body.append({
            "type" : "TextBlock",
            "text" : f"**{status['text']}** : {RESULTS['total_'+status['key']]}"
        })
    body.append(
                {   
                    "type": "TextBlock",
                    "text": "_________________________________________________________________\n"
                }
            )    

    for result in RESULTS["results"]:
        for status in STATUS:
            if status['hide']: continue
            if result[f'{status["key"]}_percentage'] == 0: continue
            test_string = "\r"
            for step in result[f"{status['key']}_steps"]:
                test_string+= f"- {step} \r"
            body.append(
                {   
                    "type": "TextBlock",
                    "text": f"""**{result['app'].replace("_", " ")} tests: {status['description']}**  {test_string}"""
                }
            )
            body.append(
                {   
                    "type": "TextBlock",
                    "text": "\n"
                }
            )
    payload["type"] = "message"
    attachments = {}
    attachments["contentType"] = "application/vnd.microsoft.card.adaptive"
    attachments["contentUrl"] = None
    attachments["content"] = {
            "$schema":"http://adaptivecards.io/schemas/adaptive-card.json",
            "type":"AdaptiveCard",
            "version":"1.2",
            "msTeams" : { "width": "full" },
            "body" : body
    }

    attachments_arr = [ attachments ]
    payload["attachments"] = attachments_arr
    return payload

        
def post_to_teams(payload, secret):
    """Post the message to Teams

    Args:
        payload (str): Teams formatted data 

    Raises:
        Exception: error during post
    """    
    response = requests.post(url=decrypt(HOOK_URL, secret), data=json.dumps(payload),
                             headers={
                                 'Content-Type': "application/json",
                             })
    if response.status_code != 200:
        raise Exception(f'Something went wrong posting the results to Teams')
    else:
        print("Results posted successfully")


def unzip_file(path):
    """Unzip the file in case of a .zip

    Args:
        path (str): path to the zip file

    Returns:
        str: new path with files unzipped
    """    
    global _temp_path
    unzipped_folder = path.split('/')[-1].split('.')[0]
    shutil.unpack_archive(path, os.path.join(_temp_folder, unzipped_folder))
    print(unzipped_folder)
    new_path = f"{_temp_folder}/{unzipped_folder}"
    print(new_path)
    _temp_path = new_path

    return new_path

def remove_directory():
    """Remove the temporary folder
    """  
    if os.path.exists(_temp_folder):
        shutil.rmtree(_temp_folder)
   
def set_credentials():
    """Set the credentials retriving them from the credentials.tml file
    """    
    credentials = get_credentials_from_yaml_file("teams")
    global HOOK_URL
    HOOK_URL = credentials['hook_url']
        
def main(args):
    """Main function of the script

    Args:
        args (Namespace): parameters parsed by the args parser
    """    
    set_credentials()
    if args.path.endswith('.zip'):
        files = os.listdir(unzip_file(args.path))
        args.path = _temp_path
    else:
        files = os.listdir(args.path)
    for f in files:
        if f.endswith('.csv') and 'csv_stats.csv' in f:
            process_data(os.path.join(args.path, f), args.release, args.env)
    payload = build_teams_payload(args.suite)
    post_to_teams(payload, args.secret)
    remove_directory()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default='csv_results', type=str, help='CSV Files folder')
    parser.add_argument('--release', required=True, type=lambda x: datetime.strptime(x,'%m%d%Y'), help='Release date (mmddyyyy)')
    parser.add_argument('--env', required=True, choices=[key for key in ENVS.keys()], help='Environment')
    parser.add_argument('--secret', default=os.getenv('PERFORMANCE_TEST_PLATFORM_SECRET'), help='Symmetric key used to decrypt the pre seed file')
    parser.add_argument('--suite',required=True, type=str, help='Name of the test suite')

    exit(main(parser.parse_args()))