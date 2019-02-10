import geopy
from folium import FeatureGroup, LayerControl, Marker, GeoJson, Icon, Map

# Creating api and map
location_glc = geopy.geocoders.Bing("AkMauqTzoufweVPfqhc7sH9vm94E7U5JZ4_pzcrm7pQ4smvCA8eMkYxuokQPRPCX")
html_map = Map(zoom_start=17)
# Creating FeatureGroups for movies and population
fg_m = FeatureGroup(name='Movies')
fg_pp = FeatureGroup(name="Population")


def population(path):
    """
    str -> None
    This function add  population child to the html map
    """

    fg_pp.add_child(GeoJson(data=open(path, 'r',
                                      encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor': 'green'
                            if x['properties']['POP2005'] < 10000000
                            else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                            else 'red'}))


def file_pars(path, year):
    """
    str, int-> dct{str: lst}
    Reads file and return all movies that were produced in that year
    """
    movie_dct = {}
    with open(path, mode="r", encoding="utf8") as file:
        for line in file:
            line = line.split(",")
            movie_yr = line[1]
            if str(year) == movie_yr:
                movie_nm = line[0]
                movie_lc = " ".join(line[3:]).strip()
                # print(movie_lc)
                if movie_lc in movie_dct:
                    movie_dct[movie_lc].append(movie_nm)
                else:
                    movie_dct[movie_lc] = [movie_nm]
        return movie_dct


def html_crtr(latitude, longitude, titles):
    """
    float, float, str -> None
    Function creates the httml file that has markers of movies by location
    """
    global html_map
    Marker(location=[latitude, longitude],
           popup=titles,
           icon=Icon()).add_to(fg_m)


def greeting():
    """
    None -> int

    Function greets user and ask to input year
    """
    print("Hello user\n"
          "this program will show you location were movies produced")
    year = int(input("Enter year: "))
    return year


def lct_to_crd(location):
    """
    str -> tuple(float, float)
    Function returns latitude and longitude by location adress

    >>> print(lct_to_crd("Lviv Ukraine"))
    (49.844409942627, 24.0254306793213)
    """
    lct = location_glc.geocode(location)
    return lct.latitude, lct.longitude


def main():
    """
    None -> None
    The main fuction that starts all module
    """
    year = greeting()

    # Change location for your preferences
    dct = file_pars('data/locations.csv', year)
    population('data/world.json')
    counter = 0
    global fg_list
    fg_list = []
    for location in dct:
        title_str = ""
        for title in dct[location]:
            title_str += title
        try:
            latitude, longitude = lct_to_crd(location)
            html_crtr(latitude, longitude, title_str)
            counter += 1

            print("one more")

        except Exception:
            print("Error 429")

    print("Finish", counter)
    # Adding to the html map movie layer
    fg_m.add_to(html_map)
    # Adding to the html map population layer
    fg_pp.add_to(html_map)
    # Saving map
    LayerControl().add_to(html_map)
    html_map.save('Map_movie.html')


if __name__ == '__main__':
    main()
