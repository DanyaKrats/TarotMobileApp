import requests
import json
import memory
from datetime import datetime

def request_mock(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            list_of_values = list(memory.read_json_from_file("cotd.txt").values())
            return list_of_values[0]
    return wrapper

class Connection:
    def __init__(self) -> None:
        self.base_url = "http://13.60.56.40"
        self.data = ''
    
    @request_mock
    def get_cotd_random(self, filename="cotd.txt"):
        today_str = datetime.today().strftime('%Y-%m-%d')
        try:
            last_result:dict = memory.read_json_from_file(filename)

            if today_str in last_result.keys():
                return last_result[today_str]

        except Exception as e:
            pass
        
        responce = requests.request("GET", self.base_url + "/card_of_the_day")
        result = json.loads(responce.content.decode()) 
        data = {today_str:result}
        memory.create_and_write_json_to_file(data, filename)
        return result

    
# a = Connection()
# responce = a.get_cotd_random()
# print(responce)