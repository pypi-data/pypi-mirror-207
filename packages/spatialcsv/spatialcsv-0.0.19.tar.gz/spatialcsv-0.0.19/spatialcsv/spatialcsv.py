import pandas as pd
import csv
from dms2dec.dms_convert import dms2dec
from pyproj import Transformer



class Points:
    
    def __init__(self, csv, coords, **kwargs):
        '''
        Main class for spatialcsv
        Args:
        csv: filepath or url to csv file
        coords: list with header titles indicating latitude and longitude
            example: coords=['lat', 'long']
        tags (optional): If displaying on leafmap,
            these will show up as info when the point is selected
            list with header titles indicating tags
            example: tags=['city', 'pop']
        epsg (optional): Will automatically process lat/long degree or decimal,
            if coordinates are in x/y, will assume epsg:3857
            If this is not your crs, indicate here
            example: epsg='2274'
        '''
        self.csv = csv
        self.coords = coords
        self.df = pd.read_csv(csv, header=0, index_col=False)
        if "tags" not in kwargs:
            self.tags = self.get_header()
        else:
            self.tags = kwargs["tags"]
        if "epsg" not in kwargs:
            kwargs["epsg"] = 3857
            self.epsg = 3857
        else:
            self.epsg = kwargs["epsg"]

        self.df = self.lat_long()


    def remove_null(self):
        '''
        Removes lines that have empty coordinates. 
        Empty coordinates cause problems with streamlit
        '''
        """
        for index, row in self.df.iterrows():
            if pd.isna(row[self.coords[0]]) or pd.isna(row[self.coords[1]]):
                self.df.drop([index, 0], inplace=True)
        """
        self.df.dropna(axis=0, how='any', subset=[self.coords[0], self.coords[1]], inplace=True)
        return(self.df)


    def to_streamlit(self):
        '''
        renames columns so that it can be added to streamlit app
        '''
        self.remove_null()
        self.df.rename(columns={self.coords[0]:'lat', self.coords[1]:'lon'}, inplace=True) 
        return(self.df)


    def to_leafmap(self):
        '''
        Selects what information you want displayed on the leafmap marker
        '''
        drops = []
        for item in list(self.df.columns):
            if item not in self.coords and item not in self.tags:
                self.df.drop(columns=[item], inplace=True)
        return(self.df)


    def get_header(self):
        '''
        returns header row
        '''
        return(list(self.df.columns))


    def lat_long(self):
        #checks everything in lat/long decimal format:
        test_df = self.df.get(self.coords)
        for item in self.df[self.coords[0]].to_list():
            if 'S' in str(item) or 'N' in str(item):
                self.df = self.degree_to_decimal()
                return(self.df)
            elif int(item) > 180:
                self.df = self.change_proj()
                return(self.df)
            else:
                return(self.df)


    def updated_csv(self, file_name):
        '''
        Outputs the processed csv into a new csv
        '''
        self.df.to_csv(file_name, index=False)




    def degree_to_decimal(self):
        '''
        Changes the coordinates in the csv from degree format to decimal
        '''
        temp_df = self.df.get(self.coords)
        listlat = []
        listlong = []
        for item in self.df[self.coords[0]].to_list():
            listlat.append(dms2dec(item))
        for item in self.df[self.coords[1]].to_list():
            listlong.append(dms2dec(item)) 
        temp_df[self.coords[0]] = self.df[self.coords[0]].replace(
                self.df[self.coords[0]].to_list(), listlat)
        self.df[self.coords[0]] = temp_df[self.coords[0]]
        temp_df[self.coords[1]] = self.df[self.coords[1]].replace(
                self.df[self.coords[1]].to_list(), listlong)
        self.df[self.coords[1]] = temp_df[self.coords[1]]
        return(self.df)
	
	
    def change_proj(self):
        '''
        Changes the projection from what is given to lat/long epsg:4326
        '''
        transformer = Transformer.from_crs(self.epsg, 4326)
        listlat = []
        listlong = []
        listlat, listlong = transformer.transform(
                self.df[self.coords[0]].values, 
                self.df[self.coords[1]].values)
        self.df[self.coords[0]] = listlat
        self.df[self.coords[1]] = listlong
        return(self.df)
	
    

def get_cols(data):
    '''
    for getting the column header while still in csv format
    '''
    df = pd.read_csv(data, header=0, index_col=False)
    return(list(df.columns))
    
