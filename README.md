## Documentation

[Tensorflow](https://www.tensorflow.org/api_docs)
[Docker](https://docs.docker.com/)
[Traefik](https://doc.traefik.io/traefik/)
[FastAPI](https://fastapi.tiangolo.com/)
[Python](https://docs.python.org/3/)
[Debian](https://www.debian.org/doc/)
[Flutter](https://docs.flutter.dev/)
[LaTeX](https://www.latex-project.org/help/documentation/)

## Requirements

### For running:
 - Docker or Python 3.8 installed on your machine

### For training:
 - Python 3.8
 - 32Gb RAM as it is, adaptable to run on 16Gb
 - 2Gb of storage available
 - Recommended Ryzen 5 5600 or higher 
 * Note: Having a phisical GPU available will decrease significantly the training times. It is recommended to have CUDA, although we include a package in requirements.txt that allows a translation from AMD Technology to CUDA (only for Windows OS)

## Run locally

To train the IA locally: 

 - Clone the proyect
 - Install dependencies provided in `requirements.txt`
 - Download the dataset and the necessary fonts provided in the "necessary files" section
 - Unzip them in the root of the folder with the same name
 - Run the training_process.py script and wait for it to end


To run the IA locally without a container:

 - Clone the proyect
 - Install dependencies provided in `requirements.txt`
 - Run the main with uvicorn.


To deploy the IA locally end expose it to global network:

 - Follow the instructions provided in the section "Networking" of the documentation
 - Open the correct port
 - Clone the project
 - Create a container with the Dockerfile provided in the repository and the documentation
 - Run the container

 ## API Reference

#### Get a prediction

```https
  POST kanji.otterleek.ddns/
```

| Parameter | Type        | Description                |
| :-------- | :---------- | :------------------------- |
| `file`    | `multipart` | **Required**. Kanji image. |

