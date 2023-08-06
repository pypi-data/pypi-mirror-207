import spotON_sdk




print (spotON_sdk.Markets().markets_List)
print (spotON_sdk.Markets().get_Market_by_area_code("AT").country.emoji)
print (spotON_sdk.Austria.__name__)

for country in spotON_sdk.Markets().markets_List:
    print (country.name)
