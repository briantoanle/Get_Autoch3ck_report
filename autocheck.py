import requests
import config

sample = ["https://www.autotrader.com/cars-for-sale/experian?SID=ATCpqbwsrhtSksggQO&VIN=4T3ZA3BB4BU039547&brand=atc&ps=true&make=Toyota",
          "https://www.autotrader.com/cars-for-sale/experian?SID=ATCpqbwsrhtSksggQO&VIN=JTEZU14R668055827&brand=atc&ps=true&make=Toyota",
          "https://www.autotrader.com/cars-for-sale/experian?SID=ATCpqbwsrhtSksggQO&VIN=4JGDA7DB3CA057743&brand=atc&ps=true&make=Mercedes-Benz",
          "https://www.autotrader.com/cars-for-sale/experian?SID=ATCpqbwsrhtSksggQO&VIN=5YJYGDEE4MF066732&brand=atc&ps=true&make=Tesla"]

testLink = 'https://www.autotrader.com/cars-for-sale/experian?SID=ATCpqbwsrhtSksggQO&VIN=5YJYGDEE4MF066732&brand=atc&ps=true&make=Tesla'

vin = ''

def get_car_information(VIN):
    # this method takes in a VIN number and returns the car's make
    api_url = 'https://api.api-ninjas.com/v1/vinlookup?vin={}'.format(VIN)
    response = requests.get(api_url, headers={'X-Api-Key': f'{config.api_ninja_key}'})
    if response.status_code == requests.codes.ok:
        # convert api response to dictionary for easier parsing
        return response.json()
    else:
        print("Error:", response.status_code, response.text)

def parse_car_information(VIN):
    car = get_car_information(VIN)

    return car['manufacturer']

def replace_VIN_and_make(autotrader_link, VIN, Make):
    # this method gets the autotrader link, vin, make and return a new string with required information
    vin_location = autotrader_link.find('VIN=')
    make_location = autotrader_link.find('make=')
    #print(autotrader_link[make_location+5:len(autotrader_link)])
    #print(autotrader_link[vin_location+4:vin_location+4+17])

    # strings are immutable
    #autotrader_link[autotrader_link[vin_location+4:vin_location+4+17]] = VIN
    newLink = autotrader_link[:vin_location+4] + VIN + autotrader_link[vin_location+21:make_location+5] + Make

    return newLink

replace_VIN_and_make(testLink,'JN1AZ4EH3DM383000','Nissan')

def main():

    while vin.lower() != 'exit':
        vin = str(input('Please enter the vin: '))
        make = str(input(('Please enter the make of the vehicle')))

        print()