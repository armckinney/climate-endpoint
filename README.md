<!-- header -->
<div align="center">
    <p>
    <!-- Header -->
        <img width="100px" src="./static/images/climate_logo.png"  alt="climate-endpoint" />
        <h2>Climate Endpoint</h2>
        <p><i>Enabling the search for a better future</i></p>
    </p>
    <p>
    <!-- Shields -->
        <a href="https://github.com/armckinney/climate-endpoint/LICENSE">
            <img alt="License" src="https://img.shields.io/github/license/armckinney/climate-endpoint.svg" />
        </a>
        <a href="https://codecov.io/gh/armckinney/climate-endpoint">
            <img alt="Code Coverage" src="https://codecov.io/gh/armckinney/climate-endpoint/branch/master/graph/badge.svg" />
        </a>
        <a href="https://github.com/armckinney/climate-endpoint/issues">
            <img alt="Issues" src="https://img.shields.io/github/issues/armckinney/climate-endpoint" />
        </a>
        <a href="https://github.com/armckinney/climate-endpoint/pulls">
            <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/armckinney/climate-endpoint" />
        </a>
        <a href="https://stackshare.io/armck/climate-endpoint">
            <img alt="StackShare.io" src="http://img.shields.io/badge/tech-stack-0690fa.svg?label=StackShare.io">
        </a>
    </p>
    <p>
    <!-- Links -->
        <a href="#demo">View Demo</a>
        ·
        <a href="https://github.com/armckinney/climate-endpoint/issues/new/choose">Report Bug</a>
        ·
        <a href="https://github.com/armckinney/climate-endpoint/issues/new/choose">Request Feature</a>
    </p>
</div>
<br>
<br>

# API Routes
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

/api/v1.0/ and /api/v1.0//

* Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
* When given the start only, calculates TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
* When given the start and the end date, calculates the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

