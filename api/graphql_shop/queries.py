from api.graphql_shop.all_queries import company
from api.graphql_shop.all_queries import category, dish, cart


class Query(dish.Query, category.Query, company.Query, cart.Query):
    pass
