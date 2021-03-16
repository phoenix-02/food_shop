import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from shop.models import Company


class CompanyType(DjangoObjectType):
    class Meta:
        model = Company


class Query(ObjectType):
    company = graphene.Field(CompanyType, id=graphene.Int())
    companies = graphene.List(CompanyType)

    @staticmethod
    def resolve_company(self, info, **kwargs):
        company_id = kwargs.get('dish_id')
        if company_id is not None:
            return Company.objects.get(pk=company_id)
        return None

    @staticmethod
    def resolve_companies(self, info, **kwargs):
        return Company.objects.all()
