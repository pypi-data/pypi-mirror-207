# Standard imports
from pprint import pprint

# Third-party imports
import requests
import pandas as pd

# Project imports
from . import utils

### Dataset functions ###


def upload_dataset(dataset_filepath: str, server="cloud", verbose=False) -> None:
    """
    Upload a dataset to the cloud so that it can be queried and used for training
    params:
        dataset_filepath: str; location of csv dataset on local machine
        server: str; either "cloud" or "local"
        verbose: bool
    """
    # TODO: Allow for uploading pandas dataframes
    headers = utils.STANDARD_HEADERS.copy()  #  TODO: Is .copy() necessary here?
    headers["X-Dataset"] = dataset_filepath
    lambda_url = utils.get_server_url(server) + "/generate_upload_url"
    r = requests.get(lambda_url, headers=headers)
    utils.check_response(r)
    if verbose:
        utils.print_response_message(r)
    upload_url = r.json()["url"]
    if verbose:
        print(f"Uploading {dataset_filepath}")
    utils.upload_file_to_presigned_url(
        dataset_filepath, upload_url, verbose=verbose)
    process_url = utils.get_server_url(server) + "/process_uploaded_dataset"
    r = requests.post(process_url, headers=headers)
    if verbose:
        utils.print_response_message(r)


def query_dataset(dataset_name: str, server="cloud", verbose=False) -> pd.DataFrame:
    """
    Query a dataset that exists on the cloud by printing summary statistics
    params:
        dataset_name: str; name of dataset on S3 (same as the uploaded file name)
        server: str; either "cloud" or "local"
        verbose: bool
    """
    url = utils.get_server_url(server) + "/query_dataset"
    headers = utils.STANDARD_HEADERS.copy()
    headers["X-Dataset"] = dataset_name
    r = requests.get(url, headers=headers)
    utils.check_response(r)
    df = utils.extract_csv_from_response(r, "summary")
    if verbose:
        utils.print_response_message(r)
        print("Summary:\n", df, "\n")
    return df


def list_datasets(server="cloud", verbose=False) -> list:
    """
    List datasets that have been uploaded to the cloud
    params:
        server: str; either "cloud" or "local"
        verbose: bool
    """
    url = utils.get_server_url(server) + "/list_datasets"
    headers = utils.STANDARD_HEADERS.copy()
    r = requests.get(url, headers=headers)
    utils.check_response(r)
    if verbose:
        utils.print_response_message(r)
    response = r.json()
    return response["datasets"]


def delete_dataset(dataset_name: str, server="cloud", verbose=False) -> None:
    """
    Delete a dataset from the cloud
    params:
        dataset_name: str; name of dataset on S3 (same as the uploaded file name)
        server: str; either "cloud" or "local"
        verbose: bool
    """
    url = utils.get_server_url(server) + "/delete_dataset"
    headers = utils.STANDARD_HEADERS.copy()
    headers["X-Dataset"] = dataset_name
    r = requests.post(url, headers=headers)
    utils.check_response(r)
    if verbose:
        utils.print_response_message(r)

###  ###

### Campaign functions ###


def train_campaign(params: dict, campaign: str, server="cloud", verbose=False) -> None:
    """
    Train a campaign remotely using twinLab
    params:
        params: dict; parameters for training
        campaign: str; name of this campaign and final trained model (user choice)
        server: str; either "cloud" or "local"
        verbose: bool
    """
    if server == "cloud":
        url = utils.TRAIN_CAMPAIGN_CLOUD_URL
    else:
        url = utils.get_server_url(server) + "/train_campaign"
    headers = utils.STANDARD_HEADERS.copy()
    headers["X-Campaign"] = campaign
    r = requests.post(url, json=params, headers=headers)
    utils.check_response(r)
    if verbose:
        utils.print_response_message(r)


def query_campaign(campaign_name: str, server="cloud", verbose=False) -> dict:
    """
    Print summary statistics for a pre-trained campaign
    params:
        campaign_name: str; name of trained model to query
        server: str; either "cloud" or "local"
        verbose: bool
    """
    url = utils.get_server_url(server) + "/query_campaign"
    headers = utils.STANDARD_HEADERS.copy()
    headers["X-Campaign"] = campaign_name
    r = requests.get(url, headers=headers)
    utils.check_response(r)
    metadata = utils.extract_item_from_response(r, "metadata")
    if verbose:
        utils.print_response_message(r)
        print("Metadata:")
        pprint(metadata, compact=True, sort_dicts=False)
    return metadata


def list_campaigns(server="cloud", verbose=False) -> list:
    """
    List all trained campaigns stored in cloud
    params:
        server: str; either "cloud" or "local"
        verbose: bool
    """
    url = utils.get_server_url(server) + "/list_campaigns"
    headers = utils.STANDARD_HEADERS.copy()
    r = requests.get(url, headers=headers)
    utils.check_response(r)
    if verbose:
        utils.print_response_message(r)
    response = r.json()
    return response["campaigns"]


def sample_campaign(
    filepath: str, campaign: str, server="cloud", verbose=False
) -> tuple:
    """
    Sample a pre-trained campaign that exists on the cloud
    params:
        filepath: str; location of csv dataset on local machine for evaluation
        campaign: str; name of pre-trained model to do the evaluating
        server: str; either "cloud" or "local"
        verbose: bool
    """
    # TODO: Rename to evaluate_campaign?
    # TODO: Allow for uploading pandas dataframes
    url = utils.get_server_url(server) + "/sample_campaign"
    files = {"file": (filepath, open(filepath, "rb"), "text/csv")}
    headers = utils.STANDARD_HEADERS.copy()
    headers["X-Campaign"] = campaign
    r = requests.post(url, files=files, headers=headers)
    utils.check_response(r)
    df_mean = utils.extract_csv_from_response(r, "y_mean")
    df_std = utils.extract_csv_from_response(r, "y_std")
    if verbose:
        utils.print_response_message(r)
        print("Mean: \n", df_mean, "\n")
        print("Std: \n", df_std, "\n")
    return df_mean, df_std


def delete_campaign(campaign_name: str, server="cloud", verbose=False) -> None:
    """
    Delete campaign directory from S3
    params:
        campaign_name: str; name of trained model to delete
        server: str; either "cloud" or "local"
        verbose: bool
    """
    url = utils.get_server_url(server) + "/delete_campaign"
    headers = utils.STANDARD_HEADERS.copy()
    headers["X-Campaign"] = campaign_name
    r = requests.post(url, headers=headers)
    utils.check_response(r)
    if verbose:
        utils.print_response_message(r)
