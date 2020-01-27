'''
Author: Drew McKinney
Creation Date: 1/26/2020
VU_DABC
SQL Alchemy - Challenge
Flask API
'''



# import dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import numpy as np
import datetime as dt


# database setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite?check_same_thread=False")
Base = automap_base()
Base.prepare(engine, reflect=True)
session = Session(engine)

Measurement = Base.classes.measurement
Station = Base.classes.station


# flask setup
app = Flask(__name__)



# flask routes

@app.route('/')
def index():
    return('''
    <h1>Hawaii Weather Data API Documentation</h1>
    <br>
    <h2>Route List:</h2>
    <br>
    <strong>Click item headers for examples.</strong>
    <ol>
        <li><a href=/>Index</a> : /</li>
            <ul>
                <li>Main Domumentation Page Detailing end points</li>
            </ul>
        <li><a href=/api/v1.0/precipitation>/api/v1.0/precipitation</a></li>
            <ul>
                <li>Return a JSON list of precipitation data by date.</li>
                <li>Returned as JSON Format</li>
            </ul>
        <li><a href=/api/v1.0/stations>/api/v1.0/stations</a></li>
            <ul>
                <li>Return a JSON list of stations from the dataset.</li>
                <li>Returned as JSON Format</li>
            </ul>
        <li><a href=/api/v1.0/tobs>/api/v1.0/tobs</a></li>
            <ul>
                <li>Return a JSON list of Temperature Observations (tobs) for the previous year.</li>
                <li>Returned as JSON Format</li>
            </ul>
        <li><a href=/api/v1.0/2016-06-06>/api/v1.0/<code>&lt;start_date&gt;</code></a></li>
            <ul>
                <li>Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start date to end of dataset.</li>
                <li>Returned as JSON Format</li>
                <li>Date Query Format: yyyy-mm-dd</li>
            </ul>
        <li><a href=/api/v1.0/2016-05-06/2016-06-06>/api/v1.0/<code>&lt;start_date&gt;/&lt;end_date&gt;</code></a></li>
            <ul>
                <li>Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.</li>
                <li>Returned as JSON Format</li>
                <li>Date Query Format: yyyy-mm-dd</li>
            </ul>
    </ol>

    Last Documentation Update: 1/26/2019

    
    ''')


@app.route('/api/v1.0/precipitation')
def prcp():
    '''
    Returns precipitation data per date in Json format.
    '''
    try:
        query = session.query(Measurement.date, Measurement.prcp).all()

        results = []
        for item in query:
            date = np.ravel(item)[0]
            value = np.ravel(item)[1]
            diction = {date : value}
            results.append(diction)
        
        return jsonify(results)

    except:
        return 'Unknown Server Error'



@app.route('/api/v1.0/stations')
def stns():
    '''
    Returns weather station data in Json format.
    '''
    try:
        query = session.query(Station.id, Station.station, Station.name).all()
        
        results = []
        for item in query:
            station_id = np.ravel(item)[0]
            station = np.ravel(item)[1]
            name = np.ravel(item)[2]
            diction = {station_id : [{'name': name}, {'station':station}]}
            results.append(diction)

        return jsonify(results)
    except:
        return 'Unknown Server Error'



@app.route('/api/v1.0/tobs')
def temps():
    '''
    Returns temperature observations (tobs) for the previous year (from end of data set).
    '''
    try:
        last_date = np.ravel(session.query(func.max(Measurement.date)).all())[0]
        last_year_date = dt.datetime.strptime(last_date, '%Y-%m-%d') - dt.timedelta(days=365)

        query = session.query(Measurement.date, Measurement.tobs).\
                    filter(Measurement.date > last_year_date).\
                    order_by(Measurement.date).all()

        results = []
        for item in query:
            date = np.ravel(item)[0]
            tobs = np.ravel(item)[1]
            diction = { date : tobs }
            results.append(diction)

        return jsonify(results)

    except:
        return 'Unknown Server Error'



@app.route('/api/v1.0/<start_date>')
def strt(start_date):
    '''
    Returns JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
    '''
    try:
        start_date = dt.datetime.strptime(start_date, '%Y-%m-%d')

        query = session.query(Measurement.tobs).\
                    filter(Measurement.date > start_date).\
                    order_by(Measurement.date).all()

        temps = []
        for item in query:
            temps.append(np.ravel(item)[0])
        tmax = round(max(temps), 2)
        tmin = round(min(temps), 2)
        tavg = round(sum(temps)/len(temps), 2)
        results = { 'tavg' : tavg, 'tmin' : tmin, 'tmax' : tmax}

        return jsonify(results)
    except:
        return 'Unknown Server Error'



@app.route('/api/v1.0/<start_date>/<end_date>')
def strtend(start_date, end_date):
    '''
    Returns JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
    '''
    try:
        start_date = dt.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = dt.datetime.strptime(end_date, '%Y-%m-%d')

        query = session.query(Measurement.tobs).\
                    filter(Measurement.date > start_date).\
                    filter(Measurement.date < end_date).\
                    order_by(Measurement.date).all()

        temps = []
        for item in query:
            temps.append(np.ravel(item)[0])
        tmax = round(max(temps), 2)
        tmin = round(min(temps), 2)
        tavg = round(sum(temps)/len(temps), 2)
        results = { 'tavg' : tavg, 'tmin' : tmin, 'tmax' : tmax}

        return jsonify(results)
    except:
        return 'Unknown Server Error'





if __name__ == '__main__':
    app.run(debug=True)
