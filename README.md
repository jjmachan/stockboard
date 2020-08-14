# StockBoard

Visualize the StockRoom repos.

## Setup

First we have to create a stock repo. To do that, make a new directory and init stock

```
$ pip install stockroom
$ stock init
$ stock import torchvision.mnist
```

stock will download the dataset and setup the repo.

Now lets clone this repo, cd into that dir and install all the requirements

```
$ pip install -r requirements.txt
```

For now you will have to change the path in the code to the path of the stock repo that you created (sorry about that, will change it in the asap)
and run 
```
$ uvicorn api.main:stockboard --reload
```

the app should be up and running.
