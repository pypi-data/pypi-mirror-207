#from neurospeed.auth.auth_as_user_handler import Auth_AS_User_Handler
#from neurospeed.utils.helper_service import UtilService
#from neurospeed.hia_user_data.neurobrave_sensor_interface import HIA_Client

from neurospeed.auth.auth_as_customer_handler import Auth_AS_Customer_handler
from neurospeed.api_http_handlers.recorder_http_handler import UserRoom_Recorder_Handler
from neurospeed.api_http_handlers.exporter_http_handler import UserRoom_Recorder_Exporter_Handler
import time 
import logging
import requests
from datetime import datetime

global recorder_handler
global exporter_handler


def run_recorder_flow(customer_auth, hia_config, recorder_name = "default"):
    '''
    create data recorder instance on cloud.
    recorder created with status "resource_pending".
    once available recording resources found and assgined
    recorder status will change to "pending",
    then once recorder picked by assigned recorder resources and start to record status will change to "recording"
    '''
    global recorder_handler
     
    username = hia_config["username"]
    # set up data recorder instance:
    # list_recorders = recorder_handler.list_recorders(0,50)
    
    list_recorders = recorder_handler.list_recorders(1, 50, {"username": username})
    logging.debug("list of existing recorders:")
    logging.debug(list_recorders)
    if list_recorders is not None:
        for index, item in enumerate(list_recorders["pager"]["items"]):
            if not list_recorders["pager"]["items"][index]["status"] == "stopped":
                logging.debug("discovered Recorder with status not stopped, stopping recorder")                
                rec_id = list_recorders["pager"]["items"][index]["id"]
                recorder_handler.update_recorder(rec_id, "stopped")                 
                while True:                    
                    if recorder_handler.get_recorder(rec_id)["status"] == "stopped":
                        logging.debug("stopped recorder successfully")
                        time.sleep(5)
                        break


    recorder = recorder_handler.create_recorder(username = username, recorder_name = recorder_name)
    if recorder == None:
        logging.debug("failed to create recorder")
        return None
        
    recorder_id = str(recorder["id"])
    logging.debug('created recorder with id' + recorder_id)
    # get recorder ID for further administration:
    recorder = recorder_handler.get_recorder(recorder_id)     
    logging.debug("recorder status: " + recorder["status"])
    
    # wait until cloud resources allocated to recorder:
    recorder_recording = False
    max_query_attemps = 5
    query_attemps = 1
    while (recorder_recording != True & (query_attemps < max_query_attemps) ):
        recorder = recorder_handler.get_recorder(recorder_id)   
        logging.debug("recorder status: " + recorder["status"])
        if (recorder["status"] == "recording"):
            logging.debug('recorder started recording')
            recorder_recording = True
        else:
            logging.debug('recorder not recording yet')
            query_attemps = query_attemps + 1
            time.sleep(10)
             
    if (recorder_recording != True):
        logging.debug('recorder not yet recording after ' + str(query_attemps)  + ' query attempts')
        recorder_handler.delete_recorder(recorder_id)
        return None
     

    # #once recorder starts recording, you can change it's status to paused or stopped. you can resume paused recorder but not stopped recorder
    # # pause recorder:
    # res = recorder_handler.update_recorder(recorder_id, "paused")
    # recorder = recorder_handler.get_recorder(recorder_id)     
    # print("recorder status: " + recorder["status"])
    # time.sleep(15)
    
    # # reactivate paused recorder
    # recorder_handler.update_recorder(recorder_id, "pending") 
    # recorder = recorder_handler.get_recorder(recorder_id)     
    # print("recorder status: " + recorder["status"])
 
    #recorder_handler.delete_recorder(recorder_id) # uncomment this to delete recorder
    # recorders = recorder_handler.list_recorders(username)
    # print(recorders)
    
     
    
    
    return recorder_id


def start_recording(customer_auth, hia_config, recorder_name):
    global recorder_handler
    recorder_handler = UserRoom_Recorder_Handler(customer_auth)   
    recorder_id = run_recorder_flow(customer_auth, hia_config, recorder_name)
    
    while recorder_id is None:
        print("FAILED starting the cloud recording serivce! Retrying.\n")
        recorder_id = run_recorder_flow(hia_config)  
    return recorder_id



def stop_recording(recorder_id):
    recorder_handler.update_recorder(recorder_id, "stopped") 
    print("recorder status: " + recorder_handler.get_recorder(recorder_id)["status"])


def run_exporter_flow(recorder_id, exporter_config, hia_config, save_folder):
    '''
    inputs:
        recorder id - string with recorder id in neurospeed that's used in this section
        exporter_config - dictionry with exported configuration. exporter name, time limits, fields to export.
        hia_config - dictionary with hia_config. used for the credentials.
        save_folder - absolute folder path to save the .csv file
    
    outputs:
        full absolute path to downloaded .csv file with data
        
        
    this function operates the exported on neurospeed via the neurospeed API.
    it runs exporter on cloud, waits for it to complete, and downloads the file using received temporary URL. 
    the URL deprecated quickly so don't expect it to work after even few minutes of completing the export. 
    
    the downloaded file is .csv, same format like downlaoding from exporter via neurospeed dashboard
    
    '''
    
    global exporter_handler
    # create exporter, if recorder has no data, request will fail.
    exporter = exporter_handler.create_exporter(int(recorder_id), exporter_config)
    exporter_id = str(exporter["id"])

    exporter = exporter_handler.get_exporter(exporter_id)  
    logging.debug("EXPORTER: ")
    logging.debug(exporter)

    # once exporter created, query it's status until it "exported".
    max_query_attemps = 100
    for query_attempt in range(max_query_attemps):
        exporter = exporter_handler.get_exporter(exporter_id)  
        logging.debug("exporter status: " + exporter["status"])
        if (exporter["status"] == "exported"):
            logging.debug('exporter finished exporting')
            break
        time.sleep(2)
             
        
    if exporter["status"] != "exported":
        logging.debug('exporter not yet exported the file after  ' + str(max_query_attemps)  + ' query attempts')
        exporter_handler.delete_exporter(exporter_id)
        return None
   
    # once exporter exported the file, you can ask for an URL to download the exported file. 
    #the url available for only short time before it deprecates
    #get_exported_url(exporter_id) returns dictionary of structure {"url": "https://neurospeed...... ...."}
    url_response = exporter_handler.get_exported_url(exporter_id)["url"]  
    #delete_exporter(exporter_id) # uncomment this to delete exporter
    # list all exporters under username
    # exporters = exporter_handler.list_exporters(hia_config["username"])
    # print(exporters)    
    logging.debug("data download link: " + url_response)
    exported_data = requests.get(url_response)
    exported_filename = save_folder + "/_" + exporter_config["custom_name"] + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + '.csv'
    logging.debug("saving data to local file at " + exported_filename)
    with open(exported_filename, "wb")as f:
        f.write(exported_data.content)

    return exported_filename
    
def download_data(customer_auth, recorder_id, exporter_config, hia_config, save_folder):
    global exporter_handler
    exporter_handler = UserRoom_Recorder_Exporter_Handler(customer_auth)
    run_exporter_flow(recorder_id, exporter_config, hia_config, save_folder)
