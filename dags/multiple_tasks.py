import pendulum
import json

from airflow.decorators import dag, task

@dag(
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
)

def run_example_taskflow():
    @task(multiple_outputs=True)
    def getPersonDetails():
        sample_data = {
            "firstName": "Random",
            "surName": "Guy"
        }
        return sample_data
        
    @task(multiple_outputs=True)
    def getLocationDetails():
        sample_data =  {
            "country": "Brazil",
            "city": "Sao Paulo"
        }
        return sample_data

    @task()
    def showProfile(firstName, surName, country, city):
        print(f"{firstName} {surName} lives in {city}, {country}")

    person = getPersonDetails()
    loc = getLocationDetails()
    showProfile(
       firstName=person['firstName'],
       surName=person['surName'],
       country=loc['country'],
       city=loc['city']
    )

 
run_example_taskflow()
