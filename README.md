# Cloud Functions Wrapper

This is a very simple template to assist the development of python based cloud functions (Google Cloud Platform's approach on serverless computing). It may also work with other public clouds, like Azure or AWS, but I haven't tested, so cannot guarantee.

The main idea is that, in order to simplify the publication of Python functions, GCP offers a sort of enclosure which will then call the provided function. This enclosure is not more than a very simple Flask app that redirects any requests to the functions deployed. This repository aims on replicating this enclosure.

## Requirements

Google offers Python 3.7 as a stable version and 3.8 in beta. I used 3.8.1 for my development, but little to nothing should change among those versions.

- Flask
- Gunicorn
- virtualenv (recommended, but not mandatory). I actually use pyenv, but feel free to pick whatever isolates your development environment and won't make a mess of your OS.

## Setting up

To get started, clone the repository, create a virtualenv and install the requirements:

```bash
$ git clone https://github.com/mauodias/cloud-functions-wrapper.git; cd cloud-functions-wrapper
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements
```

This is enough to get started. Having that done, just start the server to get a nice Hello World! in port 8000:

```bash
$ gunicorn app:app --reload
[2020-07-25 22:55:25 +0200] [3563] [INFO] Starting gunicorn 20.0.4
[2020-07-25 22:55:25 +0200] [3563] [INFO] Listening at: http://127.0.0.1:8000 (3563)
[2020-07-25 22:55:25 +0200] [3563] [INFO] Using worker: sync
[2020-07-25 22:55:25 +0200] [3565] [INFO] Booting worker with pid: 3565
```

Navigate to http://127.0.0.1:8000 and check with your own eyes :D

## Moving on from Hello World

To actually develop your function, navigate to the folder `application` and edit the `main.py` file. Just keep the `main` function signature as is and develop around it. The `request` parameter that it receives is a Flask [`request`](https://flask.palletsprojects.com/en/1.1.x/api/#flask.request) object.
