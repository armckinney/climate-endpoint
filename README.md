# Climate-Endpoint
---
This repository houses an API endpoint flask-application that returns various data on climates reported per Hawaiian stations.

Endpoint documentation can be viewed at the end of this README.



### Technologies:
1. Python
2. SQLAlchemy (sqlite)
3. Flask
4. Numpy
5. Datetime
6. Jupyter Notebook



### Endpoint Routes
---

/

* Home page.
* Lists all routes that are available.


/api/v1.0/precipitation


* Converts the query results to a Dictionary using date as the key and prcp as the value.
* Returns the JSON representation of your dictionary.




/api/v1.0/stations

* Returns a JSON list of stations from the dataset.


/api/v1.0/tobs

* Queries for the dates and temperature observations from a year from the last data point.
* Returns a JSON list of Temperature Observations (tobs) for the previous year.


/api/v1.0/<start> and /api/v1.0/<start>/<end>

* Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
* When given the start only, calculates TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
* When given the start and the end date, calculates the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.