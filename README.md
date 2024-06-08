## Documentation

[Tensorflow](https://www.tensorflow.org/api_docs)

[Docker](https://docs.docker.com/)

[Traefik](https://doc.traefik.io/traefik/)

[FastAPI](https://fastapi.tiangolo.com/)

[Python](https://docs.python.org/3/)

[Debian](https://www.debian.org/doc/)

[Flutter](https://docs.flutter.dev/)

[LaTeX](https://www.latex-project.org/help/documentation/)


## Downloads

[Kanji_Dataset.zip](https://nextcloud.otterleek.com/s/zxdKKBXD5TKq8zQ)

[Fullmodel.keras](https://nextcloud.otterleek.com/s/Ggb9npniamTKk5Q)


## Requirements

### For running:
 - Docker or Python 3.8 installed on your machine
 - Download the keras trained model from the section above and place it into python's trained_models folder.

### For training:
 - Python 3.8
 - 32Gb RAM as it is, adaptable to run on 16Gb
 - 2Gb of storage available
 - Recommended Ryzen 5 5600 or higher 
 - Download the base dataset from the section above and unzip it into python's dataset folder.
 * Note: Having a physical GPU available will decrease significantly the training times. It is recommended to have CUDA, although we include a package in requirements.txt that allows a translation from AMD Technology to CUDA (only for Windows OS)

## Run locally

To train the IA locally: 

 - Clone the project
 - Install dependencies provided in `requirements.txt`
 - Download the base dataset from the section above and unzip it into python's dataset folder.
 - Run the training_process.py script and wait for it to end


To run the IA locally without a container:

 - Clone the project
 - Download the keras trained model from the section above and place it into python's trained_models folder.
 - Install dependencies provided in `requirements.txt`
 - Run the main with uvicorn.


To deploy the IA locally end expose it to global network:

 - Install Docker
 - Follow the instructions provided in the section "Networking" of the documentation
 - Open the correct port
 - Clone the project
 - Download the keras trained model from the section above and place it into python's trained_models folder.
 - Create a container with the Dockerfile provided in the repository and the documentation
 - Run the container

 ## API Reference

#### Get a prediction

```https
  POST kanji.otterleek.com/
```

| Parameter | Type        | Description                |
| :-------- | :---------- | :------------------------- |
| `file`    | `multipart` | **Required**. Kanji image. |

