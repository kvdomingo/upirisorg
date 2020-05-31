import graphene
from graphene_django.types import DjangoObjectType
from .models import Member


class MemberType(DjangoObjectType):
    class Meta:
        model = Member


class Query:
    member = graphene.Field(
        MemberType,
        id=graphene.Int(),
        slug=graphene.String(),
        last_name=graphene.String(),
    )
    all_members = graphene.List(MemberType)

    def resolve_all_members(self, info, **kwargs):
        return Member.objects.all()

    def resolve_member(self, info, **kwargs):
        id = kwargs.get('id')
        slug = kwargs.get('slug')
        last_name = kwargs.get('last_name')

        if id is not None:
            return Member.objects.get(pk=id)

        if slug is not None:
            return Member.objects.get(slug=slug)

        if last_name is not None:
            return Member.objects.get(last_name=last_name)
