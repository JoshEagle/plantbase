import os
import json
import pandas as pd
import datetime


def scrape_to_file(html, today):

    os_command = f'curl {html} > plantbase/data/weather_data/{today}.html'
    os.system(os_command)


def get_weather(today):

    weather = json.load(open(f'plantbase/data/weather_data/{today}.html'))

    weather_summary = []
    titles, paras = [], []

    weather_info = {'applicable_date',
                    'weather_state_name',
                    'min_temp',
                    'max_temp',
                    'wind_speed'}

    for i in range(5):
        for key, value in weather['consolidated_weather'][i].items():
            if key in weather_info:
                titles.append(key)
                paras.append(value)
        weather_summary.append(dict(zip(titles,paras)))

    for row in weather_summary:
            date_object = datetime.datetime.strptime(row['applicable_date'], '%Y-%m-%d')
            row['applicable_date'] = date_object.strftime('%a %-d %b %Y')
            row['min_temp'] = str(round(row['min_temp'])) + ' C'
            row['max_temp'] = str(round(row['max_temp'])) + ' C'
            row['wind_speed'] = str(round(row['wind_speed'])) + ' mph'

    return weather_summary


def df_engineering(df):

    weather_info_df = pd.DataFrame(df)
    weather_info_df = weather_info_df.set_index('applicable_date')

    return weather_info_df


def main():

    today = datetime.date.today().strftime('%y%m%d')
    html = 'https://www.metaweather.com/api/location/44418/'

    scrape_to_file(html, today)
    weather_info_df = df_engineering(get_weather(today))
    weather_info_df.to_csv(f'plantbase/data/weather_data/{today}.csv')


if __name__ == '__main__':
    main()
