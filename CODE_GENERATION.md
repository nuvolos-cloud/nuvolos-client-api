# Generating the Nuvolos Python Client API

The Nuvolos Python Client API is a generated library that provides a convenient way to call the public Nuvolos REST API from Python. The API is generated using [OpenAPI Generator](https://openapi-generator.tech/).


## Prerequisites

Install `openapi-generator` by following the [official installation instructions](https://openapi-generator.tech/docs/installation). Use the version recorded in `.openapi-generator/VERSION` to keep generated diffs reproducible.

## Generating the client

Download the deployed public API specification from `https://api.eu1-staging.nuvolos.cloud/openapi.yaml` for staging verification or `https://api.eu1.nuvolos.cloud/openapi.yaml` for a production release, save it as `nuvolos-client-api.yml`, then run:

```bash
openapi-generator generate -i ./nuvolos-client-api.yml -g python -o . --skip-validate-spec -c ./python_gen.yml -t ./templates
```

## Running an example

To run an example, please install the client library:

```bash
pip install -e .
```

Then, run the example:

```bash
export NUVOLOS_API_KEY="<your-api-key>"
python nuvolos_client_api_example.py
```