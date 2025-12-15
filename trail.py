
import requests
import csv
import json
import logging

logger = logging.getLogger(__name__)

class Trail():
    def __init__(self):
        self.trailURL = "https://api.trail.fi/api/v1/"
        self.trailItemURL = self.trailURL + "items/"
        self.trailDepartmentURL = self.trailURL + "departments/"

        self.headers = {
            "Content-Type":"application/json",
            "Authorization":"Basic ",
        }
        pass

    def loadKey(self, filename):
        global headers

        with open(filename) as file:
            for line in file:
                authTag = line.find("TRAIL_BASIC_AUTH_API_TOKEN = ")
                if (authTag == -1):
                    continue
                
                apiKey = line[29:]
                logger.debug("Key: " + apiKey)
                self.apiKey = apiKey
                self.headers["Authorization"] = "Basic " + apiKey
                return

        raise Exception("No key found in file")
    
    def updateItem(self, item, jsonPayload):
        global trailItemURL, headers

        response = requests.put(self.trailItemURL + item, headers=self.headers, json=jsonPayload)

        if (response.status_code != 200):
            logger.warn("Unable to update item " + item)
            logger.warn(response.content)
            return False
        
        logger.info("Successfully updated item " + item)
        return True
    
    def getModel(self, model):
        global trailModelURL, headers

        modelResponse = requests.get(self.trailModelURL + model, headers=self.headers)

        if (modelResponse.status_code != 200):
            raise Exception("Response code " + str(modelResponse.status_code) + " when loading model " + model)

        return json.loads(modelResponse.content)
    
    def getItem(self, item):
        global trailItemURL, headers

        itemResponse = requests.get(self.trailItemURL + item, headers=self.headers)

        if (itemResponse.status_code != 200):
            raise Exception("Response code " + str(itemResponse.status_code) + " when loading item " + item)

        return json.loads(itemResponse.content)
    
    def getDepartment(self, department):
        global trailItemURL, headers

        departmentResponse = requests.get(self.trailDepartmentURL, headers=self.headers)

        if (departmentResponse.status_code != 200):
            raise Exception("Response code " + str(departmentResponse.status_code) + " when loading department " + department)

        return json.loads(departmentResponse.content)

    def updateItemDepartment(self, item, department):
        global trailItemURL, headers

        responseJson = {
            "department": department,
        }

        return self.updateItem(item, responseJson)


    def updateItemIdentifier(self, oldIdentifier, newIdentifier):
        global trailItemURL, headers

        itemResponse = requests.get(self.trailItemURL + oldIdentifier, headers=self.headers)

        responseJson = {
            "identity": newIdentifier,
        }

        return self.updateItem(oldIdentifier, responseJson)


    def setItemLocationToItem(self, item, locationItem):
        global trailItemURL, headers

        locationData = self.getItem(locationItem)
        logger.debug(locationData)
        locationID = locationData['data']['id']
        logger.debug(locationID)

        responseJson = {
            "location_class": "item",
            "parent_item_id": locationID,
        }

        return self.updateItem(item, responseJson)


    def deleteItem(self, item, reason, description, force=False, permanent=False):
        global trailItemURL, headers
        
        itemResponse = requests.get(self.trailItemURL + item, headers=self.headers)
        if (itemResponse.status_code != 200):
            logger.warn("Unable to find item: " + item)
            return False
        
        jsonContent = json.loads(itemResponse.content)

        if (force==False):
            deleteAuthorisation = input("Are you sure you wish to delete " + item + " (" + jsonContent['data']['model']['name'] + ") Y/N:")
            deleteAuthorisation.capitalize().strip()
            if (deleteAuthorisation != "Y" and deleteAuthorisation != "YES"):
                return False
            
        params = {
            'delete_reason': reason,
            'delete_description': description,
            'permanently' : permanent
        }
        
        deleteResponse = requests.delete(self.trailItemURL + item, headers=self.headers, params=params)

        if (deleteResponse.status_code != 200):
            logger.warn("Unable to delete " + item)
            logger.warn(deleteResponse.content)
            return False

        logger.info("Successfully deleted " + item + " (" + jsonContent['data']['model']['name'] + ")")
        return True