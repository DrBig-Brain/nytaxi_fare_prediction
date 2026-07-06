from datetime import datetime
import subprocess
def ingest():
    today = datetime.now()
    year = today.year
    if(today.month > 2):
        month = today.month - 2
    else:
        month = today.month + 10
        year -= 1

    month = f"{month:02d}"
    year = str(year)

    url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month}.parquet"
    destination = f"./dataset/raw/{year}-{month}-raw.parquet"
    print(f"downloading {url}")
    try:
        subprocess.run(['wget','-O',destination,url])
        print(f"dataset saved to {destination}")
    except Exception as e:
        print("error downloading dataset",e)
if __name__ == "__main__":
    print(ingest())