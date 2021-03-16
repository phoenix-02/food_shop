import graphene
from api.graphql_shop.queries import Query
from api.graphql_shop.mutations import Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
