from models.search_result import SearchResult

def sort_by_price(price_list: [SearchResult], number_of_stops: int) -> [SearchResult]:
    #get best results for 0/1/2+ stops

    match number_of_stops:
        case 0:
            return sorted( filter(lambda x: x.direct is not None, price_list), key=lambda x:x.direct)
        case 1:
            return sorted( filter(lambda x: x.one is not None, price_list), key=lambda x:x.one)
        case 2:
            return sorted( filter(lambda x: x.two_plus is not None, price_list), key=lambda x:x.two_plus)