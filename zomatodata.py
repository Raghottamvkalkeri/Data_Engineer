# import pandas as pd
# import requests
# import csv

# url = "https://jsonplaceholder.typicode.com/posts"

# # Make a GET request to fetch data
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     data = response.json()  # Convert response to JSON
#     df = pd.DataFrame(data)  # Convert JSON to DataFrame
#     print(df.head())  # Display first 5 rows
# else:
#     print(f"Failed to fetch data. Status code: {response.status_code}")

# with open('Zomato-data-.csv', mode='r', encoding='utf-8') as file:
#         datavalue = csv.reader(file)

#         header = next(datavalue)
#         name = header.index('name')
#         orderdata = header.index('online_order')

#         for index,  row in enumerate(datavalue , start = 1):
#             print("Sl No ", index , "Name " , row[name] , "Ordred Online " ,row[orderdata])
#             # data_list.append({row})
#             # row_data = {"SL No": index}  # Add serial number
#             # row_data.update({header[i]: row[i] for i in range(len(header))})  # Map headers to values


# import json
# from http.server import SimpleHTTPRequestHandler, HTTPServer

# df = pd.read_csv("Zomato-data-.csv")

# class MyHandler(SimpleHTTPRequestHandler):
#     def do_GET(self):
#         if self.path == "/restaurants":
#             self.send_response(200)
#             self.send_header("Content-type", "application/json")
#             self.end_headers()
#             self.wfile.write(json.dumps(df.to_dict(orient="records")).encode())
#         else:
#             self.send_response(404)
#             self.end_headers()
#             self.wfile.write(b"Not Found")

# server = HTTPServer(("0.0.0.0", 8000), MyHandler)
# print("Server running on http://127.0.0.1:8000")
# server.serve_forever()


import pandas as pd

# Read the CSV file
df = pd.read_csv('zomato.csv')

#define name and online_order columns
# name = df['name']
# online_order = df['online_order']

# Select only the name and online_order columns
selected_columns = df[['name', 'online_order']]

# Convert to JSON
json_data = selected_columns.to_json(orient='records')
csv_data = selected_columns.to_csv('zomatodata.csv', index=True , index_label="SL No")

# Convert DataFrame to JSON
# json_data = df.to_json(orient='records')

# Optionally, write the JSON data to a file
with open('zomato.json', 'w') as f:
    f.write(json_data)

# print(json_data)