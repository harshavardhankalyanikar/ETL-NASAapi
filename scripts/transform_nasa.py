
import pandas as pd
import json 
import glob
import os 
def transform_weather_data():
    os.makedirs("../data/staged",exist_ok=True)
    latest_file=sorted(glob.glob("../data/raw/apod_*.json"))[-1]


    with  open(latest_file,"r") as f:
        data=json.load(f)
    df=pd.DataFrame( {
            "date": [data["date"]],
            "title": [data["title"]],
            "explanation": [data["explanation"]],
            "media_type": [data["media_type"]],
            "img_url": [data["url"]],
        }
)
    df["inserted_at"] = pd.Timestamp.now()
    output_path="../data/staged/apod_cleaned.csv"
    df.to_csv(output_path,index=False)
    print(f"Transformed {len(df)} apod records to : {output_path}")
    return df
if __name__=="__main__":
    transform_weather_data()