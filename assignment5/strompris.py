#!/usr/bin/env python3
"""
Fetch data from https://www.hvakosterstrommen.no/strompris-api
and visualize it.

Assignment 5
"""

import datetime

import altair as alt
import pandas as pd
import requests
import requests_cache

# install an HTTP request cache
# to avoid unnecessary repeat requests for the same data
# this will create the file http_cache.sqlite
requests_cache.install_cache()


# task 5.1:


def fetch_day_prices(date: datetime.date = None, location: str = "NO1") -> pd.DataFrame:
    """Fetch one day of data for one location from hvakosterstrommen.no API

    Args:
        date (datetime.date, optional): The date to evaluate prices. Defaults to None.
        location (str, optional): The location code to evaluate prices. Defaults to "NO1".

    Returns:
        pd.DataFrame: Dataframe containing prices in NOK for every hour of date.
    """
    if date is None:
        date = datetime.date.today()

    # Ensure date is after 2nd Oct 2022
    assert date >= datetime.date(2022, 10, 2)
    url = f"https://www.hvakosterstrommen.no/api/v1/prices/{date.strftime('%Y/%m-%d')}_{location}.json"
    data = requests.get(url).json()
    df = pd.DataFrame.from_records(data, columns=["NOK_per_kWh", "time_start"])
    df.time_start = pd.to_datetime(df.time_start, utc=True).dt.tz_convert("Europe/Oslo")
    return df


# LOCATION_CODES maps codes ("NO1") to names ("Oslo")
LOCATION_CODES = {
    "NO1": "Oslo",
    "NO2": "Kristiansand",
    "NO3": "Trondheim",
    "NO4": "Tromsø",
    "NO5": "Bergen",
}

# task 1:


def fetch_prices(
    end_date: datetime.date = None,
    days: int = 7,
    locations=tuple(LOCATION_CODES.keys()),
) -> pd.DataFrame:
    """Fetch prices for multiple days and locations into a single DataFrame

    Make sure to document arguments and return value...
    ...
    """
    if end_date is None:
        end_date = datetime.date.today()

    res = pd.DataFrame()
    for i in reversed(range(days)):
        date = end_date - datetime.timedelta(days=i)
        for loc in locations:
            df = fetch_day_prices(date, loc)
            df["location_code"] = loc
            df["location"] = LOCATION_CODES[loc]
            res = pd.concat([res, df])

    return res


# task 5.1:


def plot_prices(df: pd.DataFrame) -> alt.Chart:
    """Plot energy prices over time

    x-axis should be time_start
    y-axis should be price in NOK
    each location should get its own line

    Make sure to document arguments and return value...
    """
    ...


# Task 5.4


def plot_daily_prices(df: pd.DataFrame) -> alt.Chart:
    """Plot the daily average price

    x-axis should be time_start (day resolution)
    y-axis should be price in NOK

    You may use any mark.

    Make sure to document arguments and return value...
    """
    ...


# Task 5.6

ACTIVITIES = {
    # activity name: energy cost in kW
    ...
}


def plot_activity_prices(df: pd.DataFrame, activity: str = "shower", minutes: float = 10) -> alt.Chart:
    """
    Plot price for one activity by name,
    given a data frame of prices, and its duration in minutes.

    Make sure to document arguments and return value...
    """

    ...


def main():
    """Allow running this module as a script for testing."""
    df = fetch_prices()
    chart = plot_prices(df)
    # showing the chart without requiring jupyter notebook or vs code for example
    # requires altair viewer: `pip install altair_viewer`
    chart.show()


if __name__ == "__main__":
    main()
