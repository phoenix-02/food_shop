import graphene


class CategoryInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
