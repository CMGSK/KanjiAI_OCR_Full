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

# DISCLAIMER:

We do provide all the necessary scripts. Some of them have hardcoded paths, debug functions, and several other things that may break or show unexpected behaviours if the use instructions are not followed precisely. 

We have trained this AI with less labels and epochs than we should have. The reason for this is saving time for deliver a proper demo in time. This means it may underperform with certain kanji and be less precise distinguishing between those with high similarities.


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
 - Run the main with the uvicorn command:
 ```
 uvicorn main:app --host 0.0.0.0 --port 39000
 ```


To deploy the IA dockerized end expose it to global network:

 - Install Docker
 - Follow the instructions provided in the section "Networking" of the documentation
 - Open the correct port (default on 39000)
 - Clone the project
 - Download the keras trained model from the section above and place it into python's trained_models folder.
 - Create a container with the Dockerfile provided in the repository and the documentation
 - Run the container


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


## Proper order of execution

This project is on a developing stage and we have not implemented a script to automate its use. We just have developed the tools to make it work properly. If you want to train the model, validate it, and make it work, a reminder of the correct order for the steps:

 - Install and get all the necessary libraries, and files as indicated in this instructions file.
 - Run `training_process.py` under `./python_ai/utils` (If you want to train)
 - Run `validation.py` under `./python_ai/utils` (to access the validation data)
 - If you trained the model from scratch, change the .keras file name under `./python_ai/trained_models/` to `fullmodel.keras`. You can skip this step if you didnt train it yourself, but make sure you have that file (a download for it is available).
 - Check documentation under `./latex_docu/final_pdf/*` and Docker official documentation to deploy a container with the application running. There is also information on how to expose it to the internet as a service. Alternatively, you can deploy it locally, as we already explained. 


## API Reference

#### Get a prediction

```https
  POST kanji.otterleek.com/
```

| Parameter | Type        | Description                |
| :-------- | :---------- | :------------------------- |
| `file`    | `multipart` | **Required**. Kanji image. |

