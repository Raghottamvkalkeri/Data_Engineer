
#Added Flask to make this csv to API 
from flask import Flask, jsonify
import csv

app = Flask(__name__)

@app.route('/APIS', methods=['GET'])
def get_data():
    data_list = []

    with open('Zomato-data-.csv', mode='r', encoding='utf-8') as file:
        datavalue = csv.reader(file)

        header = next(datavalue)
        name = header.index('name')
        orderdata = header.index('online_order')

        for index,  row in enumerate(datavalue , start = 1):
            # print("Sl No ", index , "Name " , row[name] , "Ordred Online " ,row[orderdata])
            data_list.append({})

    return jsonify(data_list)

if __name__ == '__main__':
    app.run(debug=True)