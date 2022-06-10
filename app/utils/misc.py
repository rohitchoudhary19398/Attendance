import datetime
import os
import shutil

import pandas as pd
import pysftp
import requests
from dateutil.parser import parse

from irecordpackages.parser import CONFIG

# from irecordpackages.pipelines import process_documents
from irecordpackages.utils import constants
from irecordpackages.utils import platform_exception as exp
from irecordpackages.utils.platform_logging import logger


#
# def process_batch(uploads_csv):
#     batch_of_n = []
#     n = 0
#     batch_size = 4
#     batch_list = []
#     for index in uploads_csv.index:
#         file = os.path.join(uploads_csv.at[index, "folder_location"], uploads_csv.at[index, "filename"])
#         if n % batch_size != 0:
#             batch_list.append(file)
#         else:
#             if len(batch_list) > 0:
#                 batch_of_n.append(batch_list)
#             batch_list = []
#             batch_list.append(file)
#         n += 1
#     if n % batch_size != 0:
#         batch_of_n.append(batch_list)
#     processes = []
#     for batch in batch_of_n:
#         start_time = time.time()
#         for file in batch:
#             processes.append(multiprocessing.Process(target=process_documents.start_processing_, args=(file,)))
#         for i in processes:
#             i.start()
#         for i in processes:
#             i.join()
#         print("Time to run full batch ", time.time() - start_time)


def get_csv_from_pdf(save_path, url=r"http://127.0.0.1:8000/extract-data"):
    try:
        filename = os.path.basename(save_path)
        file_data = {"file": (filename, open(save_path, "rb"))}
        session = requests.Session()
        response = session.post(url, files=file_data, timeout=120)
        if response.status_code == 200:
            json = response.json()
            dataframe = pd.read_json(json)
            return dataframe
        else:
            raise exp.PlatformException(
                f"Post Request to InvoiceExtractor Failed: {response.content}",
                f"Post Request to InvoiceExtractor Failed: {response.content}",
            )
    except exp.PlatformException as e:
        logger.exception(e.custom_message)
        raise e
    except Exception as e:
        logger.exception(str(e))
        raise exp.PlatformException(str(e), str(e))


def save_file(file, save_path, type="csv"):
    if type == "csv":
        input_df = pd.read_csv(file)
        input_df.to_csv(save_path, index=False)

    if type == "PDF" or type == "pdf":
        file.save(save_path)


def get_list_of_files(upload_folder, status):
    temp_list = []
    if status == constants.constant.all:
        filter_df = upload_folder
    else:
        filter_df = upload_folder[upload_folder[constants.constant.status] == status]
    # filter_df.sort_values(by=[constants.constant.upload_time], ascending=False)
    # filter_df.reset_index(inplace=True, drop=True)
    for index in filter_df.index:
        dict_to_save = {}
        dict_to_save[constants.constant.filename] = filter_df.at[
            index, constants.constant.filename
        ]
        dict_to_save[constants.constant.type] = filter_df.at[
            index, constants.constant.type
        ]
        dict_to_save[constants.constant.uuid] = filter_df.at[
            index, constants.constant.uuid
        ]
        dict_to_save[constants.constant.status] = filter_df.at[
            index, constants.constant.status
        ]
        upload_val = filter_df.at[index, constants.constant.upload_time]
        if not isinstance(upload_val, datetime.date):
            upload_val = parse(upload_val)
        dict_to_save[constants.constant.upload_time] = upload_val.strftime(
            constants.TimeFormat.week_day_month_year_time
        )
        dict_to_save[constants.constant.processed_time] = " "
        val = filter_df.at[index, constants.constant.processed_time]
        if val != " ":
            if not isinstance(val, datetime.date):
                val = parse(val)
            dict_to_save[constants.constant.processed_time] = val.strftime(
                constants.TimeFormat.week_day_month_year_time
            )
        temp_list.append(dict_to_save)
    return temp_list


def delete_file_by_uuid(uuid):
    try:
        file_path = os.path.join(CONFIG.uploadFolder, uuid)
        shutil.rmtree(file_path)
    except exp.PlatformException as e:
        logger.exception(e.custom_message)
        raise e
    except Exception as e:
        logger.exception(str(e))
        msg = f"Failed to DELETE FILE : UUID : {uuid}"
        raise exp.PlatformException(msg, str(e))


def delete_invoice_by_invoice_id(invoice_id):
    try:
        invoice_path = os.path.join(CONFIG.templateFolderPath, f"{invoice_id}.csv")
        os.remove(invoice_path)
    except exp.PlatformException as e:
        logger.exception(e.custom_message)
        raise e
    except Exception as e:
        logger.exception(str(e))
        msg = f"Failed to Delete invoice Invoice ID : {invoice_id}"
        raise exp.PlatformException(msg, str(e))


def get_invoice_by_invoice_id(invoice_id, covert_dtype=False):
    try:
        invoice_path = os.path.join(CONFIG.templateFolderPath, f"{invoice_id}.csv")
        convert_dtype = {i: str for i in CONFIG.account_segment_columns}
        dataframe = pd.read_csv(invoice_path, dtype=convert_dtype)
        dataframe = dataframe.where(pd.notnull(dataframe), None)
        return dataframe

    except exp.PlatformException as e:
        logger.exception(e.custom_message)
        raise e
    except Exception as e:
        logger.exception(str(e))
        msg = f"Failed to FETCH invoice Invoice ID : {invoice_id}"
        raise exp.PlatformException(msg, str(e))


def update_invoice_by_invoice_id(invoice_id, dataframe):
    # todo exception handling
    try:
        invoice_path = os.path.join(CONFIG.templateFolderPath, f"{invoice_id}.csv")
        return dataframe.to_csv(invoice_path, index=False)
    except exp.PlatformException as e:
        logger.exception(e.custom_message)
        raise e
    except Exception as e:
        logger.exception(str(e))
        msg = f"Failed to UPDATE invoice Invoice ID : {invoice_id}"
        raise exp.PlatformException(msg, str(e))


def upload_file_to_sftp(host, username, password, file_path, target_path):
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    try:
        with pysftp.Connection(
            host, username=username, password=password, cnopts=cnopts
        ) as sftp:
            sftp.put(file_path, target_path)
    except Exception as e:
        raise exp.PlatformException(str(e), str(e))
