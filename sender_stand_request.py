import configuration
import data
import requests
# запрос на создание заказа
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.ORDER_CREATION_PATH,
                         json=data.order_body)

# print(post_new_order().text)

def get_track_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
                        params={"t": track})
