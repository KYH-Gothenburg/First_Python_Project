import requests
import json


def main():
    name = input('What is your name? ')
    data = requests.get('https://api.agify.io?name=' + name)
    response_data = json.loads(data.text)
    print(f'My guess is that you are {response_data["age"]} years old')


if __name__ == '__main__':
    main()
