import requests
import pprint
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta

SERVICE_KEY = ""
BASE_URL = "https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1"

class GetApplyHomeData() :
    def getData():
        date = datetime.now()
        today = date.date()
        beforeday = date.date() - relativedelta(days=5) 
        
        requst_url = f"{BASE_URL}/getAPTLttotPblancDetail?page=0&perPage=10&returnType=json&cond%5BRCRIT_PBLANC_DE%3A%3ALTE%5D={today}&cond%5BRCRIT_PBLANC_DE%3A%3AGTE%5D={beforeday}&serviceKey={SERVICE_KEY}"

        response = requests.get(requst_url)
        contents = response.text

        json_ob = json.loads(contents)
        return_data = []

        for data in json_ob['data']:    
            insert_data = {'HOUSE_NM' : data['HOUSE_NM'] , 'PBLANC_URL' : data['PBLANC_URL'], 'HMPG_ADRES' : data['HMPG_ADRES']}
            return_data.append(insert_data)
            
        return return_data