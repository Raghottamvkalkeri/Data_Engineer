
#Added Flask to make this csv to API 
from flask import Flask, jsonify
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app)
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
            # data_list.append({row})
            row_data = {"SL No": index}  # Add serial number
            row_data.update({header[i]: row[i] for i in range(len(header))})  # Map headers to values

            data_list.append(row_data)

    return jsonify(data_list)

if __name__ == '__main__':
    app.run(debug=True)