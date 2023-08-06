import spotON_sdk




print (spotON_sdk.Markets())
print (spotON_sdk.Markets().get_Market_by_area_code("AT").country.emoji)

for country in spotON_sdk.Markets().markets_List:
    print (country.name)

