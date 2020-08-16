# StockBoard

Visualize the StockRoom repos.

## Setup
First we have to create a stock repo. To do that, make a new directory and init stock

```
$ pip install stockroom
$ stock init
$ stock import torchvision.mnist
```

stock will download the dataset and setup the repo. Now you have the stockrepo running. Now lets get Stockboard up and running.

There are 2 ways.
### via Docker
This is the recomment way if you want to just try this out. (make sure you have docker setup properly)

1. Clone the repo and cd to directory
```
$ git clone 
$ cd stockboard
```

2. Build the docker Image
```
$  docker build -t stockboard .
```

3. Run the docker container
```
docker run -p 8000:8000 -v /path/to/stock/repo:/data stockboard
```

### directly

```
$ pip install -r requirements.txt
```

For now you will have to change the path in the code to the path of the stock repo that you created 
(sorry about that, will change it in the asap)
and run 
```
$ uvicorn api.main:stockboard --reload
```

the app should be up and running.
