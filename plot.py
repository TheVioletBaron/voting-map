"""
Casey Edmonds-Estes
Project 4
11/13/18
"""
from PIL import Image, ImageDraw
from PIL.ImageColor import getrgb


class Plot:
    """
    Provides the ability to map, draw and color regions in a long/lat
    bounding box onto a proportionally scaled image.
    """
    @staticmethod
    def interpolate(x_1, x_2, x_3, newlength):
        """
        linearly interpolates x_2 <= x_1 <= x_3 into newlength
        x_2 and x_3 define a line segment, and x1 falls somewhere between them
        scale the width of the line segment to newlength, and return where
        x_1 falls on the scaled line.
        """
        return newlength*(x_1 - x_2)/(x_3 - x_2)

    @staticmethod
    def proportional_height(new_width, width, height):
        """
        return a height for new_width that is
        proportional to height with respect to width
        Yields:
            int: a new height
        """
        return height/width * new_width
    
    @staticmethod
    def fill(region, style):
        """return the fill color for region according to the given 'style'"""
        if style == "GRAD":
            return Plot.gradient(region)
        else:
            return Plot.solid(region)

    @staticmethod
    def solid(region):
        """
        a solid color based on a region's plurality of votes
        Args:
            region (Region): a region object
        Yields:
            (int, int, int): a triple (RGB values between 0 and 255)
        """
        from PIL import getrbg
        return PIL.getrbg(region)

    @staticmethod
    def gradient(region):
        """
        a gradient color based on percentages of votes in a region
        Args:
            region (Region): a region object
        Yields:
            (int, int, int): a triple (RGB values between 0 and 255)
        """
        color_list = [0,0,0]
        color_list[0] = int(255*region.republican_percentage())
        color_list[1] = int(255*region.other_percentage())
        color_list[2] = int(255*region.democrat_percentage())
        return tuple(color_list)

    def __init__(self, width, min_long, min_lat, max_long, max_lat):
        """
        Create a width x height image where height is proportional to width
        with respect to the long/lat coordinates.
        """
        self.width = width
        self.min_long = min_long
        self.min_lat = min_lat
        self.max_long = max_long
        self.max_lat = max_lat
        new_height = int(self.proportional_height(width, (max_lat-min_lat), (max_long-min_long)))
        self.new_height = new_height
        self.image =  Image.new("RGB", (width, new_height), (255, 255, 255))

     

    def save(self, filename):
        """save the current image to 'filename'"""
        self.image.save(filename, "PNG")
        
    def draw(self, region, style):
        """
        Draws 'region' in the given 'style' at the correct position on the
        current image
        Args:
            region (Region): a Region object with a set of coordinates
            style (str): 'GRAD' or 'SOLID' to determine the polygon's fill
        """
        new_coords = []
        for i in region.coords:
            new_coords.append((self.interpolate(i[0], self.min_lat, self.max_lat, self.width), self.new_height - self.interpolate(i[1], self.min_long, self.max_long, self.new_height)))
            
        style_translator = None
        if style == "GRAD":
            style_translator = Plot.gradient(region)
        elif style == "SOLID":
            style_translator = Plot.solid(region)
        else:
            print("Error: style should be 'GRAD' or 'SOLID'")
        ImageDraw.Draw(self.image).polygon(new_coords, fill=style_translator, outline=None)

