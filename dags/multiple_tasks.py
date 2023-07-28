import pendulum
import json

from airflow.decorators import dag, task

@dag(
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
)

def run_example_taskflow(multiple_outputs=True):
    @task()
    def getPersonDetails():
        sample_data = {
            "firstName": "Random",
            "surName": "Guy"
        }
        return json.dumps(sample_data)
        
    @task(multiple_outputs=True)
    def getLocationDetails():
        sample_data =  {
            "country": "Brazil",
            "city": "Sao Paulo"
        }
        return json.dumps(sample_data)

    @task()
    def showProfile(firstName):
        print(firstName)

    person = getPersonDetails()
    # loc = getLocationDetails()
    showProfile(
       firstName=person,
    )

 
run_example_taskflow()
