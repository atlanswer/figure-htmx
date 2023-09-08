# Figure

Create publication-quality figure.

## Development

Install dependencies

```shell
# node dependencies
pnpm i
# conda environment
conda-lock install --mamba -p ./venv --dev
conda activate ./venv
```

Dev server

```shell
uvicorn dev:app --reload --app-dir=api
```
