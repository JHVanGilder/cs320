import zipfile
import sqlite3
import pandas as pd
from IPython.core.display import HTML

def open(name):
    """
    opens the desired path as a Connection object
    
    Parameters
    __________
    name: str
        name of the file wanted for output as a Connection object
        
    Returns
    _______
    Connection type object
    """
    c = Connection(name)
    return c

class Connection:
    def __init__(self, name):
        self.name = name
        self.db = sqlite3.connect(name + ".db")
        self.zf = zipfile.ZipFile(name + ".zip")
        
    def list_images(self):
        """
        creates a list of the images inside of the desired zip location
        
        Parameters
        __________
        None
        
        Returns
        _______
        sorted list of images within a desired zip
        """
        df = pd.read_sql("SELECT * FROM images", self.db)
        return sorted(list(df["image"]))
    
    def image_year(self, npy_file):
        """
        outputs only images that are from a specific year
        
        Parameters
        __________
        npy_file:
            ???
        
        Returns
        _______
        integer representing the year of an image creation
        """
        df = pd.read_sql("SELECT * FROM images", self.db)
        return int(df[df["image"] == npy_file]["year"])
    
    def image_name(self, npy_file):
        """
        outputs the name of an image in a file
        
        Parameters
        __________
        npy_file:
            ???
            
        Returns
        _______
        DataFrame of names of images
        """
        
        s = """
        SELECT name
        FROM places
        INNER JOIN images
        ON places.place_id = images.place_id
        WHERE image = "{}"
        """
        df = pd.read_sql(s.format(npy_file), self.db)
        return df["name"].iloc[0]
    
    def __enter__(self):
        return open(self.name)
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.close()
        
    def close(self):
        """
        closes databases and zipfiles open
        
        Paramters
        _________
        None
        
        Returns
        _______
        None
        """
        
        self.db.close()
        self.zf.close()
    
    def animate(self, city_name):
        """
        outputs an mp4 video of the land usage of a desired city from 2001 to 2016
        
        Parameters
        __________
        city_name: str
            desired city for output of land usage map
            
        Returns
        _______
        none, but does give new .mp4 file in directory with animated land usage map described in doc_string
        """
        
        
        
        
        
        
        