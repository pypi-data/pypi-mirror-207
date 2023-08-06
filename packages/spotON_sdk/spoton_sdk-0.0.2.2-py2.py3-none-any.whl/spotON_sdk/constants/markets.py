from dataclasses import dataclass
from entsoe import Area
import pandas as pd

import pandas as pd
from dataclasses import dataclass, field
from typing import Optional, Dict,Any
import pytz

from typing import List
from .countries import *
from .bidding_zones import bidding_zones

@dataclass
class Market():
    area:Area
    country :Country
    country_code : str = field(init=False)
    region_code : str = field(init=False)
    cities : str = field(init=False)


    def __post_init__(self):
        self.area_code = self.area.name
        country_region = self.area_code.split("_")
        self.country_code = country_region[0]
        if len(country_region) >=2:
            self.region_code = country_region[1]
        else:
            self.region_code = ""
        print (self.area_code)
        try:
            city_List = bidding_zones[self.area_code]["cities"]
            my_string = ', '.join(city_List)
            self.cities = my_string
        except:
            self.cities = "no city"


        self.name = f"{self.country.emoji} {self.country.__class__.__name__} {self.area_code} {self.cities}"
        #self.get_Market_by_area_code(self.area.name)

dataclass
class Markets():
    austria = Market(Area.AT,Austria)
    germany = Market(Area.DE_LU,Germany)
    luxembourg = Market(Area.DE_LU,Luxembourg)
    sweden1 = Market(Area.SE_1,Sweden)
    sweden2 = Market(Area.SE_2,Sweden)
    sweden3 = Market(Area.SE_3,Sweden)
    sweden4 = Market(Area.SE_4,Sweden)
    markets_List = [value for key, value in vars().items() if isinstance(value, Market)]

    @staticmethod
    def get_Market_by_area_code(area_code: str) -> Optional[Market]:
        for country in Markets.markets_List:
            if country.country_code == area_code:
                return country

        return None


def return_All_Areas(filterstring:str ="MBA"):
        
    result = []
    for area in Area:
        #print (area.name, area.meaning)
        if filterstring in area.meaning:
            result.append(area)
            print (area.name)

    return result


