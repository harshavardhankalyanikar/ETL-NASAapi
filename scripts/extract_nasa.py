import json 
from pathlib import Path
from datetime import datetime
import requests 

DATA_DIR=Path(__file__).resolve().parents[1]/"data"/"raw"
DATA_DIR.mkdir(parents=True,exist_ok=True)

def extract_apod_data(lat=17.3850,lon=78.4067,days=1):
    url="https://api.nasa.gov/planetary/apod?api_key=komBhoRlINNZs68haKLl5208yc9i1jXwTKb0zQQd"
    params={
        "api_key": "komBhoRlINNZs68haKLl5208yc9i1jXwTKb0zQQd",
        "thumbs": True
    }
    resp=requests.get(url,params=params)
    resp.raise_for_status()
    data=resp.json()
    filename=DATA_DIR/f"apod_{datetime.now().strftime('%Y%m%d %H%M%S')}.json"
    filename.write_text(json.dumps(data,indent=2))
    print(f"Extracted APOD data saved to {filename}")
    return data 
if __name__=="__main__":
    extract_apod_data()
