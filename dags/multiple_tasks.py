import pendulum

from airflow.decorators import dag, task

@dag(
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
)

def run_example_taskflow():
    @task()
    def getPersonDetails():
        return {
            "firstName": "Random",
            "surName": "Guy"
        }
        
    @task()
    def getLocationDetails():
        return {
            "country": "Brazil",
            "city": "Sao Paulo"
        }

    @task()
    def showProfile(firstName, surName, country, city):
        description = f"{firstName} {surName} lives in {city}, {country}"
        return description

    person = getPersonDetails()
    loc = getLocationDetails()
    showProfile(
       person["firstName"],
       person["surName"],
       loc["country"],
       loc["city"]
   )

 
run_example_taskflow()