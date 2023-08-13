import requests
import datetime as dt

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "ioasndfoiawnefwioaa"
USERNAME = "squareen"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Create POST Request
# response = requests.post(url=pixela_endpoint, json=user_params)
# response.raise_for_status()
# print(response.text)

# https://pixe.la/v1/users/squareen/graphs/graph1.html
graph_config = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "Minute",
    "type": "int",
    "color": "kuro"
}
request_header = {
    "X-USER-TOKEN": TOKEN
}
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=request_header)
# print(graph_response.json())
# graph_response.raise_for_status()

# Post Pixel
post_url = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
curr_date = dt.date.today()
param_cur_date = curr_date.strftime("%Y%m%d")
print(param_cur_date)

post_pixel_param = {
    "date": param_cur_date,
    "quantity": "30"
}

# post_pixel_response = requests.post(url=post_url, json=post_pixel_param, headers=request_header)
# print(post_pixel_response.json())
# post_pixel_response.raise_for_status()

# PUT Pixel
put_pixel_url = f"{post_url}/{param_cur_date}"
put_pixel_param = {
    "quantity": "60"
}
put_pixel_response = requests.put(url=put_pixel_url, json=put_pixel_param, headers=request_header)
print(put_pixel_response.json())
put_pixel_response.raise_for_status()