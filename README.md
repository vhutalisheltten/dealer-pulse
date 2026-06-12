# Dealer Pulse

A self-contained dealer performance evaluation app, ready for IBM Code Engine.

## Run locally

```bash
python -m pip install -r requirements.txt
python app.py
```

Open `http://localhost:8080`.

## Test

```bash
pytest
```

## Deploy to IBM Code Engine from GitHub

After pushing this repository to GitHub, create a Code Engine application from
source and select this repository. The app listens on port `8080` and includes
a `Dockerfile`; no additional build configuration is required.

## Product Details Microservice

The `product_details` directory contains a separate Product Details
Microservice for deployment from its own source context.
