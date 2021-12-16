import json


def main():
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)

    data['members'][0]['age'] += 1

    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)


if __name__ == '__main__':
    main()
