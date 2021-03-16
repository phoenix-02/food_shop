import graphene


class CompanyInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
