import os
import json
import pandas as pd
from datetime import date


def scrape_to_file(html, path):

    os_command = f'curl {html} > {path}-today.html'
    os.system(os_command)


def get_weather(path):

    weather = json.load(open(f'{path}-today.html'))

    weather_summary = []
    titles, paras = [], []

    weather_info = {'applicable_date',
                    'weather_state_name',
                    'min_temp',
                    'max_temp',
                    'wind_speed',
                    'humidity'}

    for i in range(5):
        for key, value in weather['consolidated_weather'][i].items():
            if key in weather_info:
                titles.append(key)
                paras.append(value)
        weather_summary.append(dict(zip(titles,paras)))

    return weather_summary


def main():

    today = date.today().strftime('%Y/%-m/%-d')

    html = 'https://www.metaweather.com/api/location/44418/'

    path = html.replace('https://www.metaweather.com/api/location/','').replace('/','')

    scrape_to_file(html, path)

    weather_info = get_weather(path)
    weather_info_df = pd.DataFrame(weather_info)
    weather_info_df.to_csv(f'{path}-today.csv')


if __name__ == '__main__':
    main()
