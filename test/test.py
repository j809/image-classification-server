import requests as r
server_response = r.post("http://localhost:5000/predict", files={"file": open('test_images/dog.jpg','rb')})
print(server_response.json())

# curl -F "file=@dog.jpg" http://localhost:5000/predict
