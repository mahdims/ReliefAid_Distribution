# Branch-and-Price Algorithm for Fast and Equitable Last-Mile Relief Aid Distribution

## Overview
This repository contains the datasets used in the paper titled **"Branch-and-Price Algorithm for Fast and Equitable Last-Mile Relief Aid Distribution."** The datasets is made publicly available to support equitable last-mile aid distribution research. The provided datasets are:

1. **Kartal Dataset**
2. **Van Dataset**

## Description of the Datasets

### Kartal Dataset
- This dataset contains information about relief aid distribution for the Kartal region in Istanbul, Turkey. It includes 12 selected shelter locations, thier estimated reileif aid demand and attitie and lattetiuds.
- The dataset considered real-world constraints, including vehicle capacity, maximum travel time and total supply at the depot.
- The distances between nodes are calculated arrording to actual transportation routes and potential road closures after a possible earthquick.

### Van Dataset
- This dataset contains information about the Van region following the 2011 Van earthquake, including 94 demand points and one local distribution center (LDC). 
- The dataset includes three level of node aggegartion 15, 30 and 60 demand nodes.

## Data Class for JSON Handling
This repository also includes a Python class (`Data`) that can be used to load data from a JSON file and populate relevant attributes for optimization tasks.

### How to Use the Data Class
Use the `Data` class directly to load and access the data.

Example usage:
```python
from data import Data

if __name__ == "__main__":
    dataSet = "Van"
    fileName = "Van15_A1.json"
    data = Data(f"./{dataSet}/{fileName}")
    print(data)
```

## How to Use the Datasets
- Clone the repository:
  ```bash
  git clone https://github.com/mahdims/ReliefAid_Distribution.git
  ```
- The datasets are provided in JSON format for ease of integration with the `Data` class.



