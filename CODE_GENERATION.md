# Generating the Nuvolos Python Client API

The Nuvolos Python Client API is a generated library that provides a convenient way to call the public Nuvolos REST API from Python. The API is generated using [OpenAPI Generator](https://openapi-generator.tech/).


## Prerequisites

Install `openapi-generator` by following the [official installation instructions](https://openapi-generator.tech/docs/installation). Use the version recorded in `.openapi-generator/VERSION` (currently 7.25.0) to keep generated diffs reproducible.

```bash
# example: pin the CLI used by this repo
pip install 'openapi-generator-cli==7.25.0'
```

## Preparing the OpenAPI input

1. Download the deployed public API specification:
   - staging verification: `https://api.eu1-staging.nuvolos.cloud/openapi.yaml`
   - production release: `https://api.eu1.nuvolos.cloud/openapi.yaml`
2. Save it as `nuvolos-client-api.yml`.
3. Normalize schema names before generating. The live backend emits marshmallow class names with a trailing `Schema` suffix (and a few apispec collision names). The Python client historically strips those so imports stay stable for downstream packages such as `nuvolos-cli`:

| Live schema id | Client schema id |
| --- | --- |
| `FooSchema` | `Foo` |
| `HTTPError` | `ClientApiError` (keep the existing `ClientApiError` body) |
| `StartAppSchema1` | `StartApp` |
| `TableUpdateSchemaUpdate` | `TableUpdate` |
| `TaskSchema1` | `Task1` |

Also rewrite every `#/components/schemas/...` `$ref`, set:

```yaml
openapi: 3.0.0
info:
  title: Nuvolos
  version: prod
servers:
  - url: https://api.eu1.nuvolos.cloud
```

Skipping the rename step produces classes like `GroupInstanceCreateRequestSchema` and breaks existing consumers.

4. Bump `packageVersion` in `python_gen.yml` when cutting a release.

## Generating the client

```bash
openapi-generator-cli generate -i ./nuvolos-client-api.yml -g python -o . \
  --skip-validate-spec -c ./python_gen.yml -t ./templates
```

After generation, confirm packaging metadata still matches repo conventions (`pyproject.toml` is produced from `templates/pyproject.mustache`).

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
