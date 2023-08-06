"""Main module."""

import random
import ipyleaflet
import rasterio
import matplotlib
class Map(ipyleaflet.Map):

    def __init__(self, center=[20,0], **kwargs) -> None:
        if "scroll_wheel_zoom" not in kwargs:
            kwargs["scroll_wheel_zoom"] = True
        
        super().__init__(center = center, **kwargs)

        if "layers_control" not in kwargs:
            kwargs["layers_control"] = True

        if kwargs["layers_control"]:
            self.add_layers_control()
        
        if "fullscreen_control" not in kwargs:
            kwargs["fullscreen_control"] = True
        
        if kwargs ["fullscreen_control"]:
            self.add_fullscreen_control()

    def add_search_control(self, position="topright",**kwargs):
        """Adds search control to the map
        
        Args:
            Kwargs: Keyword arguments to pass to the search control.
        """
        if "url" not in kwargs:
            kwargs["url"] = "https://nominatim.openstreetmap.org/search?format=json&q={s}"

        search_control = ipyleaflet.SearchControl(position = position,**kwargs)
        self.add_control(search_control)
        


    def add_draw_control(self, **kwargs):
        """Adds draw control to the map.
        
        Args:
            Kwargs: Keyword Arguments to add to the draw control.
        """
        draw_control = ipyleaflet.DrawControl(**kwargs)
               
        draw_control.polyline =  {
            "shapeOptions": {
                "color": "#6bc2e5",
                "weight": 8,
                "opacity": 1.0
            }
        }
        draw_control.polygon = {
            "shapeOptions": {
                "fillColor": "#6be5c3",
                "color": "#6be5c3",
                "fillOpacity": 1.0
            },
            "drawError": {
                "color": "#dd253b",
                "message": "Oups!"
            },
            "allowIntersection": False
        }
        draw_control.circle = {
            "shapeOptions": {
                "fillColor": "#efed69",
                "color": "#efed69",
                "fillOpacity": 1.0
            }
        }
        draw_control.rectangle = {
            "shapeOptions": {
                "fillColor": "#fca45d",
                "color": "#fca45d",
                "fillOpacity": 1.0
            }
        }
        self.add_control(draw_control)


    def add_layers_control(self, position="topright", **kwargs):
        """Adds a layers control to the map.
        
        Args:
            kwargs: Keyword arguments to pass to the layers control
        """
        layers_control = ipyleaflet.LayersControl(position = position, **kwargs)
        self.add_control(layers_control)

    def add_fullscreen_control(self, position="topleft"):
        """Adds a fullscreen control to the map.
        
        Args:
            kwargs: Keyward arguments to pass to the layers control.
        """
        fullscreen_control = ipyleaflet.FullScreenControl(position=position)
        self.add_control(fullscreen_control)
    
    def add_tile_layer(self, url, name, attribution = "", **kwargs):
        """Adds a tile layer to the map.
        
        Args:
            url (str): The URL of the tile layer.
            name (str): The name of the tile layer
            attribution (str, optional): The attribution of the tile layer. Defaults to **
            """
        tile_layer = ipyleaflet.TileLayer(
            url = url,
            name = name,
            attribution = attribution,
            **kwargs
        )
        self.add_layer(tile_layer)
    
    def add_basemap(self, basemap, **kwargs):
        """ Adds a basemap to the map.

        Args:
            basemap : A basemap path 

        Raises:
            ValueError: Not a valid basemap
        """
        import xyzservices.providers as xyz

        if basemap.lower() == 'roadmap':
            url = 'http://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}'
            self.add_tile_layer(url, name=basemap, **kwargs ) 
        elif basemap.lower() == 'satellite':
            url = 'http://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}'
            self.add_tile_layer(url, name=basemap, **kwargs)
        else:
            try:
                basemap = eval(f"xyz.{basemap}")
                url = basemap.build_url()
                attribution = basemap.attribution 
                self.add_tile_layer(url, name =basemap.name, attribution=attribution, **kwargs)
            except:
                raise ValueError(f"Basemap '{basemap}' not found")
            

    def add_geojson(self, data, name="GeoJSON", **kwargs):
        """Adds a GeoJSON layer to the map.
        
        Args:
            data (dict): The GeoJSON data.
            """
        
        if isinstance(data, str):
            import json
            with open(data, "r") as f:
                data = json.load(f)

        geojson = ipyleaflet.GeoJSON(data=data, name=name,**kwargs)
        self.add_layer(geojson)
   
    def add_shp(self, data, name='Shapefile', **kwargs):
        """Adds a Shapefile layer to the map.
        
        Args:
            data (str): the path to the Shapefile.
        """
        import geopandas as gpd
        gdf = gpd.read_file(data)
        geojson = gdf.__geo_interface__
        self.add_geojson(geojson, name=name, **kwargs)

    def add_vector(self, data, name = 'Vector Data', **kwargs):
        """Adds Vector Data to the map.
        
        Args:
            data (str): the path to the Vector Data
            """
        import geopandas as gdp
        gdf = gdp.read_file(data)
        geojson = gdf.__geo_interface__
        self.add_geojson(geojson, name = name, **kwargs)

    def add_raster(self, url, name='Raster', fit_bounds=True, **kwargs):
        """Adds a raster layer to the map.
        Args:
            url (str): The URL of the raster layer.
            name (str, optional): The name of the raster layer. Defaults to 'Raster'.
            fit_bounds (bool, optional): Whether to fit the map bounds to the raster layer. Defaults to True.
        """
        import httpx

        titiler_endpoint = "https://titiler.xyz"

        r = httpx.get(
            f"{titiler_endpoint}/cog/info",
            params = {
                "url": url,
            }
        ).json()

        bounds = r["bounds"]

        r = httpx.get(
            f"{titiler_endpoint}/cog/tilejson.json",
            params = {
                "url": url,
            }
        ).json()

        tile = r["tiles"][0]

        self.add_tile_layer(url=tile, name=name, **kwargs)

        if fit_bounds:
            bbox = [[bounds[1], bounds[0]], [bounds[3], bounds[2]]]
            self.fit_bounds(bbox)

    def add_image(self, url, width, height, position, **kwargs):
        """Adds an image to the map.
        
        Args:
            URL (str): the url of the image
            width (int): the width of the image
            height (int): the height of the image
            position (list): the position of the image.
        """

        from ipyleaflet import WidgetControl
        import ipywidgets as widgets

        widget = widgets.HTML(value = f'<img src="{url}" width = "{width}" height = "{height}">')
        control = WidgetControl(widget = widget, position = position)
        self.add(control)

    def add_toolbar(self, position="topright"):
        """Adds a dropdown widget to select a basemap.
        Args:
            self: The map.
            position (str, optional): The position of the toolbar. Defaults to "topright".
        """
        import ipywidgets as widgets
        from ipyleaflet import WidgetControl

        widget_width = "250px"
        padding = "0px 0px 0px 5px"  # upper, right, bottom, left

        toolbar_button = widgets.ToggleButton(
            value=False,
            tooltip="Toolbar",
            icon="wrench",
            layout=widgets.Layout(width="28px", height="28px", padding=padding),
        )

        close_button = widgets.ToggleButton(
            value=False,
            tooltip="Close the tool",
            icon="times",
            button_style="primary",
            layout=widgets.Layout(height="28px", width="28px", padding=padding),
        )

        toolbar = widgets.HBox([toolbar_button, close_button])

        def toolbar_click(change):
            if change["new"]:
                toolbar.children = [toolbar_button, close_button]
            else:
                toolbar.children = [toolbar_button]
                
        toolbar_button.observe(toolbar_click, "value")

        def close_click(change):
            if change["new"]:
                toolbar_button.close()
                close_button.close()
                toolbar.close()
                
        close_button.observe(close_click, "value")

        rows = 2
        cols = 2
        grid = widgets.GridspecLayout(rows, cols, grid_gap="0px", layout=widgets.Layout(width="65px"))

        icons = ["folder-open", "map", "bluetooth", "area-chart"]

        for i in range(rows):
            for j in range(cols):
                grid[i, j] = widgets.Button(description="", button_style="primary", icon=icons[i*rows+j], 
                                            layout=widgets.Layout(width="28px", padding="0px"))
                
        toolbar = widgets.VBox([toolbar_button])
        
        basemap = widgets.Dropdown(
            options=[ 'ROADMAP', 'SATELLITE'],
            value=None,
            description='basemap:',
            style={'description_width': 'initial'},
            layout=widgets.Layout(width='250px')
        )
        
         
        close_button2 = widgets.ToggleButton(
            value=False,
            tooltip="Close the tool",
            icon="times",
            button_style="primary",
            layout=widgets.Layout(height="28px", width="28px", padding=padding),
        )


        def close_click2(change):
            if change["new"]:
                basemap_widget.children = []

                
        close_button2.observe(close_click2, "value")
        

        basemap_widget = widgets.HBox([basemap, close_button2])

        basemap_ctrl = ipyleaflet.WidgetControl(widget=basemap_widget, position='topright')

        def change_basemap(change):
            if change['new']:
                self.add_basemap(basemap.value)

        basemap.observe(change_basemap, names='value')

        output = widgets.Output()
        output_ctrl = WidgetControl(widget=output, position="bottomright")
        self.add_control(output_ctrl)

        def toolbar_click(b):
            with output:
                output.clear_output()
                print(f"You clicked the {b.icon} button.")

                if b.icon == 'map':
                    if basemap_ctrl not in self.controls:
                        self.add_control(basemap_ctrl)
                    else:
                        basemap_widget.children = [basemap, close_button2]

        for i in range(rows):
            for j in range(cols):
                tool = grid[i, j]
                tool.on_click(toolbar_click)

        def toolbar_click(change):
            if change["new"]:
                toolbar.children = [widgets.HBox([close_button, toolbar_button]), grid]
            else:
                toolbar.children = [toolbar_button]
                
        toolbar_button.observe(toolbar_click, "value")
        toolbar_ctrl = ipyleaflet.WidgetControl(widget=toolbar, position=position)

        self.add_control(toolbar_ctrl)  

import rasterio
import matplotlib.pyplot as plt

def view_satellite_bands(filename):
    """Display images of the satellite bands

    Args:
        filename (str): the path to the image
    """
    with rasterio.open(filename) as dataset:
        # loop through each band and plot separately
        for i in range(1, dataset.count+1):
            band = dataset.read(i)
            plt.imshow(band)
            plt.title("Band {}".format(i))
            plt.show()  




import rasterio
import geopandas as gpd
import matplotlib.pyplot as plt

def plot_pixel_spectral_profile(geotiff_path, pixel_x, pixel_y):
    """_summary_

    Args:
        geotiff_path (str): path to the image
        pixel_x (int): X location of pixel 
        pixel_y (int): y location of pixel
    """
    # Open the geotiff file in read mode
    src = rasterio.open(geotiff_path)

    # Read the pixel values and geometry using the pixel's location
    pixel_values = src.read()[:, pixel_y, pixel_x]
    pixel_geometry = src.transform * (pixel_x, pixel_y)

    # Plot the spectral profile
    fig, ax = plt.subplots()
    ax.plot(src.indexes, pixel_values)
    ax.set_xlabel('Band Index')
    ax.set_ylabel('Pixel Reflectance')
    ax.set_title('Pixel Spectral Profile')
    plt.show()





















def read_band(src, band):
    """Reads the data from a band in a rasterio dataset

    Args:
        src (rasterio DatasetReader): the rasterio dataset
        band (int): the band number

    Returns:
        data (numpy array): the data from the selected band
        band (int): the band number
    """
    data = src.read(band)
    return data, band


import rasterio

def print_geotiff_metadata(filename):
    """Displays available metadata for the image 

    Args:
        filename (str): path to the image
    """
    with rasterio.open(filename) as dataset:
        print(f"Metadata for GeoTIFF file: {filename}")
        print(f"Width: {dataset.width}")
        print(f"Height: {dataset.height}")
        print(f"Number of bands: {dataset.count}")
        print(f"Data type: {dataset.dtypes[0]}")
        print(f"Coordinate reference system: {dataset.crs}")
        print(f"Transform: \n{dataset.transform}")
        print(f"Bounds: {dataset.bounds}")
        print(f"Metadata: {dataset.meta}")


    




# Generate random latitude and longitude coordinates
def Generate_random_location():
    "Generates a Random Latitude and Longitude "
    lat = random.uniform(-90, 90)
    lon = random.uniform(-180, 180)

    # Print the coordinates
    print("Latitude: ", lat)
    print("Longitude: ", lon)
