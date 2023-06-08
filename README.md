# VecPot Python SDK

- [**Documentation**](https://docs.vecpot.com)
- [**PyPi Package**](https://pypi.org/project/vecpot/)

## Install

```bash
$ pip install vecpot
```

## Usage

```python
import vecpot
import os

VP_API_KEY = os.getenv("VP_API_KEY")
vp = vecpot.VecPot(api_key=VP_API_KEY)

embedding_response = vp.embed(text="data")
print(embedding_response["embeddings"])
```
