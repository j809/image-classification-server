# Dockerized PyTorch Inference


## Build and Run
Take the following steps to setup and run the project locally:

1. Clone the repository from [source](https://github.com/ds-umass/project-3-group-7.git)

2. To build the docker container, navigate to the `app` directory and run the following command from this directory:
```
docker build . -t inference_docker
```
3. Use the following command to run the image in a container:
```
docker run -p 5000:5000 inference_docker
```
The server should be up and running now.

## Test
The server accepts a **POST** request and handles the image only in **JPG** format. After running the docker image, the server can be tested using either of the following two approaches:

1. From the `test` directory, run the following (it makes an API request with images present in the `test_images` directory):
```
python test.py
```

2. Run the following `curl` command, 
```
curl -F "file=@IMAGE_NAME.jpg" http://localhost:5000/predict
```
where IMAGE_NAME is the name of the image that you want to run the test against.
