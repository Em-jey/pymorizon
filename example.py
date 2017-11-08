from morizon.category import get_category
from morizon.offer import get_offer_data

# url = 'https://www.morizon.pl/do-wynajecia/mieszkania/gdynia/witomino-lesniczowka/?ps[number_of_rooms_from]=2'
url = 'https://www.morizon.pl/do-wynajecia/mieszkania/warszawa/srodmiescie/?ps%5Bliving_area_from%5D=30&ps%5Bliving_area_to%5D=50&ps%5Bnumber_of_rooms_from%5D=2&ps%5Bnumber_of_rooms_to%5D=2&ps%5Bnumber_of_floors_from%5D=4&ps%5Bnumber_of_floors_to%5D=4'

# offers = get_category('mieszkania', 'Gdynia', 'Witomino Leśniczówka', 'do-wynajecia', {'[number_of_rooms_from]': 2})
offers = get_category(url=url)
# print(len(offers))
# for el in offers:
#     print(el)

for urls_from_offers in offers:
    data = get_offer_data(urls_from_offers)
    # print(urls_from_offers, ' ')
    print(data)