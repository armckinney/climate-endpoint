
<!-- 
README Template Author: otheneildrew
Template Source: https://github.com/othneildrew/Best-README-Template
Version Author: Drew McKinney
 -->





<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
![GitHub last commit](https://img.shields.io/github/last-commit/ARMcK-hub/climate-endpoint)
[![MIT License][license-shield]][license-url]
![GitHub top language](https://img.shields.io/github/languages/top/ARMcK-hub/climate-endpoint)
![GitHub repo size](https://img.shields.io/github/repo-size/ARMcK-hub/climate-endpoint)
![Website](https://img.shields.io/website?down_color=lightgrey&down_message=offline&up_color=blue&up_message=online&url=https%3A%2F%2Fwestendfinancial.herokuapp.com%2F)

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://climate-endpoint.herokuapp.com/">
    <img src="https://static.goanywhere.com/images/tutorials/read-json/ExampleJSON2.png" alt="Logo" width="100" height="100">
  </a>

  <h3 align="center">Climate-Endpoint</h3>

  <p align="center">
    Climate Data API
    <br />
    <a href="https://climate-endpoint.herokuapp.com/" target="_blank"><strong> >> Visit Demo >> </strong></a>
    <br />
    <a href="https://github.com/ARMcK-hub/climate-endpoint/issues">Report Bug</a>
    -
    <a href="https://github.com/ARMcK-hub/climate-endpoint/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://climate-endpoint.herokuapp.com/)

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

Here's why Climate-Endpoint is important:
* Allows other systems to integrate and touch climate data easily and for free!


### Built With
* [Heroku](https://www.heroku.com/home)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [PostgreSQL](https://www.postgresql.org/)


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

<img src="https://avatars3.githubusercontent.com/u/57081049?s=460&u=1260bc893922a063a29f437d8565e4b970fe45ca&v=4" width=200>
<h3>Drew McKinney</h3>

[![GitHub][github-shield]][github-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Email][email-shield]][email-url]



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Vanderbilt University - powered by Trilogy](https://bootcamps.vanderbilt.edu/data/)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

<!-- Stock -->
[license-url]: https://github.com/ARMcK-hub/West-End-Financial/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/drew-mckinney/
[email-shield]: https://img.shields.io/badge/-Email-black.svg?style=flat&colorB=555
[email-url]: mailto:andrewryanmckinney@gmail.com
[github-shield]: https://img.shields.io/badge/-GitHub-black.svg?style=flat&colorB=555
[github-url]: https://github.com/ARMcK-hub
[languages-shield]: https://img.shields.io/badge/-GitHub-black.svg?style=flat&colorB=555


<!-- Project Dynamic -->
[license-shield]: https://img.shields.io/github/license/ARMcK-hub/climate-endpoint.svg?style=flat
[contributors-shield]: https://img.shields.io/github/contributors/ARMcK-hub/climate-endpoint.svg?style=flat
[contributors-url]: https://github.com/ARMcK-hub/climate-endpoint/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ARMcK-hub/climate-endpoint.svg?style=flat
[forks-url]: https://github.com/ARMcK-hub/climate-endpoint/network/members
[stars-shield]: https://img.shields.io/github/stars/ARMcK-hub/climate-endpoint.svg?style=flat
[stars-url]: https://github.com/ARMcK-hub/climate-endpoint/stargazers
[issues-shield]: https://img.shields.io/github/issues/ARMcK-hub/climate-endpoint.svg?style=flat
[issues-url]: https://github.com/ARMcK-hub/climate-endpoint/issues
[product-screenshot]: https://climatedataguide.ucar.edu/sites/default/files/styles/node_lightbox_display/public/key_figures/climate_data_set/PRISM_ppt_30yr_normal_4kmM2_annual.png?itok=UWLBBnGa

