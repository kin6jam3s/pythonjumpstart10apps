import requests
import bs4
import collections

WeatherReports = collections.namedtuple('data_on_WeatherReports',
                                        'Locations, cond, Temp, scale')


def main():
    # print the header
    print_header()
    # get zipcode from user
    zipcode = get_zipcode()
    # get html from the web / zipcode pass to function get_html_from_web()
    html = get_html_from_web(zipcode)

    # Variable html containing the response.text will be sent to this function for parsing
    report = get_weather_from_html(html)

    # display for the forecast using tuple index
    print('The temperature in {} right now is {}{} and weather condition is {}'.format(
        report[0],
        report[2],
        report[3],
        report[1]

    ))
    # using namedtuple
    print('------------------------------------')
    print('----------Using Collection----------')
    print('------------------------------------')
    print('NamedTuple : The temperature in {} right now is {}{} and weather condition is {}'.format(
        report.Locations,
        report.Temp,
        report.scale,
        report.cond

    ))

    # print(report)
    # print(len(report))
    # display for the forecast
    print('Have a nice Day! -  main')


# Function for displaying header
def print_header():
    print('----------------')
    print('    Weather App')
    print('----------------')


# Function for getting zipcode from user
def get_zipcode():
    code = input('What zipcode do you want the weather for (97201)? ')
    return code  # return the variable code


# Function for getting html from web
def get_html_from_web(zipcode):
    # appending the the zipcode to the url
    url = ('https://www.wunderground.com/weather/sg/{}'.format(zipcode))
    print(url)
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text[0:500])
    # print(response.text)
    return response.text


# Function for parsing the html text bu using inspect on chrome
def get_weather_from_html(html):
    # $('div.columns.small-12.city-header.ng-star-inserted h1').textContent
    cityCss = 'div.columns.small-12.city-header.ng-star-inserted h1'
    # $('div.condition-icon.small-6.medium-12.columns p').textContent
    weatherConditionCss = 'div.condition-icon.small-6.medium-12.columns p'
    weatherTempScaleCss = 'div.current-temp span.ng-star-inserted'

    soup = bs4.BeautifulSoup(html, 'html.parser')
    # used to find location
    location = soup.find(class_='columns small-12 city-header ng-star-inserted').find('h1').find('span').get_text()
    # used to find the condition
    condition = soup.find(class_='condition-icon small-6 medium-12 columns').find('p').get_text()
    # find the temp
    Temperature = soup.find(class_='current-temp').find(class_='wu-value').get_text()
    # find the scale
    Scale = soup.find(class_='current-temp').find(class_='wu-label').get_text()

    # location variable sent to cleanup text function
    loc = cleanup_text(location)
    # send strip loc to find_city_and_area_from_loc function
    Loc = find_city_and_area_from_loc(loc)
    # condition variable sent to cleanup text function
    cond = cleanup_text(condition)
    # Temperature variable sent to cleanup text function
    Temp = cleanup_text(Temperature)
    # location Scale sent to cleanup text function
    scale = cleanup_text(Scale)

    # print(Loc, cond, Temp, scale)
    # return (Loc, cond, Temp, scale)
    # Assigning the value to collection.namedtuple to assign variable to Location = loc, etc
    rep = WeatherReports(Locations=Loc, cond=cond, Temp=Temp, scale=Scale)
    # print(type(rep))
    return rep  # rep will be sent back and will be assign to variable named report


# loc without white space sent and defined as string
def find_city_and_area_from_loc(loc: str):
    # split the location
    # print(loc)
    parts = loc.split(',')
    # print(parts, type(parts))
    part = ','.join(parts[0:2])
    # print(part, type(part))
    return part


# location text sent and defined as str
def cleanup_text(text: str):
    # if not string return text
    if not text:
        return text
    # If text is string then strip space
    text = text.strip()  # remove whitespace
    return text  # return without space


if __name__ == '__main__':
    main()
