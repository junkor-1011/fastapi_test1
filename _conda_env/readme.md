conda env
============

- to create env
    - [`create_env_fastapi_slim.yml`](./create_env_fastapi_slim.yml)

```sh
conda env create -f create_env_fastapi_slim.yml
```

- to freeze env
    - [`fastapi_slim_freeze.yml`](./fastapi_slim_freeze.yml)

```sh
conda env export -n fastapi_slim | tee fastapi_slim_freeze.yml
```



