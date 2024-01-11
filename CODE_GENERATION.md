# Generating the Nuvolos Python Client API

The Nuvolos Python Client API is a generated library that provides a convenient way to call the public Nuvolos REST API from Python. The API is generated using [OpenAPI Generator](https://openapi-generator.tech/)


## Prerequisites

To generate the client code, please install `openapi-generator` following the instrutions on the project's website: https://openapi-generator.tech/docs/installation

## Generating the client

To generate the client, run the following command:

```bash
openapi-generator generate -i ./nuvolos-client-api.yml -g python -o . --skip-validate-spec -c ./python_gen.yml
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