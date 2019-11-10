# Movies map

> This python module creates html file that include movie map and population map on a separated layers.

Movie layer contains markers on world map that shows theyre origin studio.
Population layer divides into 3 colors (red(> 2M), orange(< 2M), green(< 1M)
![index](https://user-images.githubusercontent.com/44615981/52539170-be688f80-2d83-11e9-89e4-4f857802e7b8.jpg)




## Getting Started

This would be easy, just relax...

### Prerequisites

You need to install folium and geopy

```
pip install folium
pip install geopy
```


### Installing

Downloading my repo

```
git clone https://github.com/wat4era/html_map
```

Unziping "data.zip" (Linux & OS X)

```
unzip data.zip
```

* Changing path in the html_map.py (lines 90, 91) 
* Changing Bing-API (default = my API) in the html_map.py (line 5)


## Running the tests
* Run html_map.py (input year)
* Open new file "Movie_map.html"




## HTML code
* <*!DOCTYPE*> -  determinates document type
* <*head*> - Specifies the technical information about the document
* <*meta*> - determinates meta tegs
* <*script*> - script description
* <*link*> - establishes a connection to an external document
* <*style*> - defines the style of the elements of the web page
* <*body*> - document's body
## Modules description:
* population() - Add population child to the html map
* file_pars() - Reads file and return all movies that were produced in that year
* html_crtr() - Creates the httml file that has markers of movies by location
* greeting() - Greets user and ask to input year
* lct_to_crd() - Returns latitude and longitude by location adress
* main() - The main fuction that starts all module
## Conclusion

This module is useful for some statistics about people population
But most powerful think is the movies map that is useful not only from statistic side but also from economy side, or if you need find some studio in some country you can check is it studion in demand.

## Version
02 10 2019 - demo version

## Authors

* **Danylo Sluzhynskyi** 

