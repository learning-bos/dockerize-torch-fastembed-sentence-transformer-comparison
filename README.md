# dockerize-torch-fastembed-sentence-transformer-comparison
This is a comparison between torch fastembed and sentence-transformer. The goal is to see what is the best in order to save space for creating a docker image.

Of course we expect that torch will be the heaviest one and also sentence transformer so we are going to use three different environments in conda to not get in conflict with each other.

PYTHON VERSION: 3.12.4
CONDAENVS:
1. fastembed
2. torch
3. sentence

```
conda create -n fastembed -y
conda create -n torch -y
conda create -n sentence -y
```
```
conda activate fastembed
conda activate torch
conda activate sentence
```

We expect also that each of this will create a List of float of each sentence that is 384 of length.

## Fastembed

### Libraries
--user cause i had trouble reading a file
```
pip3 install --no-cache-dir fastembed --user
```

There is a problem with ONNX so we needed to downgrade to v.1.19 see [requirements](./fastembed/requirements.txt)

### Build time
![](./fastembed/img/build.png)

### Image size
![](./fastembed/img/image-size.png)


## Finale

| name | build time (s) | image size (GB) |
|-----|------|-----|
| fastembed | 27 | 0.6 |
