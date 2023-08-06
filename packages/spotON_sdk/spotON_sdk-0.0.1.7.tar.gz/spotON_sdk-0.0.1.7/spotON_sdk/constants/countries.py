from dataclasses import dataclass, field

from typing import Any,Optional
from entsoe.entsoe import Area


import pandas as pd
import pytz

def _country_code_to_emoji(country_code):
    OFFSET = 127397
    return ''.join(chr(ord(c) + OFFSET) for c in country_code.upper())

@dataclass
class Country:
    capital: str
    country_code: str
    UTC_time_difference: int = field(init=False)

    def calculate_utc_time_difference(self) -> Optional[pd.Timedelta]:
        try:
            local_tz = pytz.timezone(self.capital)
            utc_dt = pd.Timestamp.utcnow().to_pydatetime()
            local_dt = utc_dt.astimezone(local_tz)
            UTC_time_difference = (local_dt.utcoffset().total_seconds()) // 3600
            delta = pd.Timedelta(hours=UTC_time_difference)
            return delta,UTC_time_difference
        
        except:
            print(f"{self.capital} not found in European capitals.")
            return None

    def __post_init__(self: Any) -> None:
        self.delta,self.UTC_time_difference = self.calculate_utc_time_difference()
        self.emoji = _country_code_to_emoji(self.country_code)


@dataclass
class Austria(Country):
    capital: str = "Europe/Vienna"
    country_code: str = "AT"


@dataclass
class Belgium(Country):
    capital: str = "Europe/Brussels"
    country_code: str = "BE"


@dataclass
class Bulgaria(Country):
    capital: str = "Europe/Sofia"
    country_code: str = "BG"


@dataclass
class Croatia(Country):
    capital: str = "Europe/Zagreb"
    country_code: str = "HR"


@dataclass
class Cyprus(Country):
    capital: str = "Asia/Nicosia"
    country_code: str = "CY"


@dataclass
class CzechRepublic(Country):
    capital: str = "Europe/Prague"
    country_code: str = "CZ"


@dataclass
class Denmark(Country):
    capital: str = "Europe/Copenhagen"
    country_code: str = "DK"


@dataclass
class Estonia(Country):
    capital: str = "Europe/Tallinn"
    country_code: str = "EE"


@dataclass
class Finland(Country):
    capital: str = "Europe/Helsinki"
    country_code: str = "FI"


@dataclass
class France(Country):
    capital: str = "Europe/Paris"
    country_code: str = "FR"


@dataclass
class Germany(Country):
    capital: str = "Europe/Berlin"
    country_code: str = "DE"


@dataclass
class Greece(Country):
    capital: str = "Europe/Athens"
    country_code: str = "GR"


@dataclass
class Hungary(Country):
    capital: str = "Europe/Budapest"
    country_code: str = "HU"


@dataclass
class Ireland(Country):
    capital: str = "Europe/Dublin"
    country_code: str = "IE"


@dataclass
class Italy(Country):
    capital: str = "Europe/Rome"
    country_code: str = "IT"


@dataclass
class Latvia(Country):
    capital: str = "Europe/Riga"
    country_code: str = "LV"


@dataclass
class Lithuania(Country):
    capital: str = "Europe/Vilnius"
    country_code: str = "LT"


@dataclass
class Luxembourg(Country):
    capital: str = "Europe/Luxembourg"
    country_code: str = "LU"


@dataclass
class Malta(Country):
    capital: str = "Europe/Malta"
    country_code: str = "MT"


@dataclass
class Netherlands(Country):
    capital: str = "Europe/Amsterdam"
    country_code: str = "NL"


@dataclass
class Poland(Country):
    capital: str = "Europe/Warsaw"
    country_code: str = "PL"


@dataclass
class Portugal(Country):
    capital: str = "Europe/Lisbon"
    country_code :str = "PT"

@dataclass
class Romania(Country):
    capital: str = "Europe/Bucharest"
    country_code: str = "RO"


@dataclass
class Slovakia(Country):
    capital: str = "Europe/Bratislava"
    country_code: str = "SK"


@dataclass
class Slovenia(Country):
    capital: str = "Europe/Ljubljana"
    country_code: str = "SI"


@dataclass
class Spain(Country):
    capital: str = "Europe/Madrid"
    country_code: str = "ES"


@dataclass
class Sweden(Country):
    capital: str = "Europe/Stockholm"
    country_code: str = "SE"


'''@dataclass
class Market():
    area:Area
    country :Country



    def __post_init__(self):
        self.area_code = self.area.name
        country_region = self.area_code.split("_")
        self.country_code = country_region[0]
        if len(country_region) >=2:
            self.region_code = country_region[1]
        else:
            self.region_code = ""
        #self.get_Market_by_area_code(self.area.name)

@dataclass
class Markets():
    austria = Market(Area.AT,Austria)
    germany = Market(Area.DE,Germany)
    sweden = Market(Area.SE,Sweden)
    markets_List = [value for key, value in vars().items() if isinstance(value, Market)]

'''

def return_All_Areas(filterstring:str ="MBA"):
        
    result = []
    for area in Area:
        #print (area.name, area.meaning)
        if filterstring in area.meaning:
            result.append(area)
            print (area.name)

    return result

