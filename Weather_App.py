import requests
import bs4


def main():
    # print the header
    print_header()
    # get zipcode from user
    zipcode = get_zipcode()
    # get html from the web
    html = get_html_from_web(zipcode)

    # parse the html
    report = get_weather_from_html(html)

    # display for the forecast
    print('The temperature in {} right now is {}{} and weather condition is {}'.format(
        report[0],
        report[2],
        report[3],
        report[1]

    ))
    # print(report)
    # print(len(report))
    # display for the forecast
    print('Have a nice Day! -  main')


def print_header():
    print('----------------')
    print('    Weather App')
    print('----------------')


def get_zipcode():
    code = input('What zipcode do you want the weather for (97201)? ')
    return code


def get_html_from_web(zipcode):
    url = ('https://www.wunderground.com/weather/sg/{}'.format(zipcode))
    print(url)
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text[0:500])

    return response.text


def get_weather_from_html(html):
    cityCss = 'div.columns.small-12.city-header.ng-star-inserted h1'
    weatherConditionCss = 'div.condition-icon.small-6.medium-12.columns p'
    weatherTempScaleCss = 'div.current-temp span.ng-star-inserted'

    soup = bs4.BeautifulSoup(html, 'html.parser')
    location = soup.find(class_='columns small-12 city-header ng-star-inserted').find('h1').find('span').get_text()
    condition = soup.find(class_='condition-icon small-6 medium-12 columns').find('p').get_text()
    Temperature = soup.find(class_='current-temp').find(class_='wu-value').get_text()
    Scale = soup.find(class_='current-temp').find(class_='wu-label').get_text()

    loc = cleanup_text(location)
    Loc = find_city_and_area_from_loc(loc)
    cond = cleanup_text(condition)
    Temp = cleanup_text(Temperature)
    scale = cleanup_text(Scale)

    # print(Loc, cond, Temp, scale)
    return (Loc, cond, Temp, scale)


def find_city_and_area_from_loc(loc: str):
    parts = loc.split(',')
    part = ','.join(parts[0:2])
    # print(part)
    return part


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == '__main__':
    main()
