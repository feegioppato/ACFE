 # -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 11:18:34 2022

@author: Fernando Gioppato
"""
import re
import os
import tika
from tika import parser
import pandas as pd


class Extractor:
    
    def __init__(self, filepath, s, e, anos):
        
        """ 
        Initializes Extractor class.
        
        Parameters
        ----------
        filepath : string
            The path to the file used to extract data.
        
        s: string
            First page of the document containing tha data to be extract.
            Must follow the pattern: 'PÁGINA: x DE y'.
            ex : 'PÁGINA: 2 DE 137'
            
        e: string
            Last page of the document containing data to be extracted.
            Must follow the pattern: 'PÁGINA: x DE y'.
            ex: 'PÁGINA: 9 DE 137'
            
        anos: array_like
            Array-like object containing the years analized.
        """
        
        self.filepath = filepath
        self.startpoint = s
        self.endpoint = e
        self.listofyears = anos
        
    
    def _read_file(self):
        
        """
        Parses `.pdf` file into string objects containing tha data and metadata.
        
        Returns
        -------
            Array-like object containg both string data parsed from the `.pdf` file and its metadata.
        """
        
        self.parsed = parser.from_file(self.filepath)
        return self.parsed
    
    
    def _raw_content(self):
        
        """
        Stores the data attribute of the parsed object in a variable.
        
        Returns
        -------
            Raw string object. Contains the whole `.pdf` file parsed.
        """
        
        self.content = (self._read_file())['content']
        return self.content
    

    def _unstructured_data(self):
        
        """
        Trims the document so that only the pages containing actual data is kept.
        
        Returns
        -------
            Raw string object. Contains only the pages with data used on the analysis.
        """
        
        trim_pattern = re.compile(f"(?<={self.startpoint}).*(?={self.endpoint})", re.DOTALL|re.IGNORECASE)
        search_object = (trim_pattern).search(self._raw_content())
        return search_object.group(0)
    
    
    
    def _string_data(self):
        
        """
        Extracts the data from the raw string and stores it in an dictionary.
        
        Returns
        -------
            Dictionary containing tha data extracted from the `.pdf` file.
        """
        
        pattern = r'''
        (?P<cd>\d(?:\.\d{1,2})*)\s
        (?P<nc>(?:[a-zA-Z\u00C0-\u00ff/()\-]+\s)+)
        (?P<terceiro_ano>-?\d{1,3},?(?:,?\.?\d{1,3})*)*\s
        (?P<segundo_ano>-?\d{1,3},?(?:,?\.?\d{1,3})*)*\s
        (?P<primeiro_ano>-?\d{1,3}(?:,?\.?\d{1,3})*)'''
        
        p = re.compile(pattern, re.X)
        
        results_dict = []
        for match in re.finditer(p, self._unstructured_data()):
            (results_dict).append(match.groupdict())
            
        return results_dict
      
        
    def _data(self):
        
        """
        Consolidates the data into an pd.DataFrame.
        
        Returns
        -------
        DataFrame containing tha data.
        """
        
        self.structured_data = pd.DataFrame(self._string_data())
        self.structured_data.iloc[:, -3:] = self._data_convertion(self.structured_data.iloc[:, -3:])
        self.structured_data = self._column_names(self.structured_data)
        self.structured_data = self.structured_data.set_index('cd')
        
        return self.structured_data
        
    
    def _column_names(self, x):
        
        """
        Rename column names with the `anos` keyword argument.
        
        Returns
        -------
        DataFrame with renamed columns.
        """
        
        return x.rename({'terceiro_ano' : self.listofyears[0],
                        'segundo_ano' : self.listofyears[1],
                        'primeiro_ano' : self.listofyears[2]},
                        axis = 1)    
            
        
    def _data_convertion(self, x):
        
        """
        Converts tha data from string to float.
        
        Returns
        -------
        DataFrame with converted data.
        """
        
        return x.replace(['\.', ','], ['', '.'], regex = True).astype(float)










