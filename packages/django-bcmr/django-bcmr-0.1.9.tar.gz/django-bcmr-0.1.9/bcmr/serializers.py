from rest_framework import serializers

from django.conf import settings

from bcmr.models import *


class EmptySerializer(serializers.Serializer):
    pass


class CashTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = (
            'category',
            'name',
            'symbol',
            'description',
            'decimals',
            'icon',
            'is_nft',
            'nft_description',
            'nft_types',
            'status',
            'date_created',
            'owner',
        )
        read_only_fields = (
            'date_created',
            'owner',
        )


class MainTokenSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    uris = serializers.SerializerMethodField()

    class Meta:
        model = Token
        fields = (
            'name',
            'description',
            'token',
            'status',
            'uris',
        )

    def get_token(self, obj):
        result = {
            'category': obj.category,
            'symbol': obj.symbol,
            'decimals': obj.decimals 
        }

        if obj.is_nft:
            result['nfts'] = {
                'description': obj.nft_description,
                'fields': {},
                'parse': {
                    'bytecode': '',
                    'types': obj.nft_types
                }
            }
        
        return result

    def get_uris(self, obj):
        if obj.icon:
            return {
                'icon': f'{settings.DOMAIN}{obj.icon.url}'
            }
        return {}


class RegistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Registry
        fields = (
            'id',
            'name',
            'description',
            'tokens',
            # 'owner',
        )
        read_only_fields = (
            # 'owner',
            'id',
        )


# class NoOwnerRegistrySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Registry
#         fields = (
#             'id',
#             'name',
#             'description',
#             'tokens',
#         )
#         read_only_fields = (
#             'id',
#         )


class TokenHistorySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    token = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    uris = serializers.SerializerMethodField()

    class Meta:
        model = TokenHistory
        fields = (
            'name',
            'description',
            'token',
            'status',
            'uris',
        )

    def get_name(self, obj):
        return obj.token['name']

    def get_description(self, obj):
        return obj.token['description']

    def get_status(self, obj):
        return obj.token['status']

    def get_uris(self, obj):
        if obj.token['icon']:
            return {
                'icon': f"{settings.DOMAIN}{obj.token['icon']}"
            }
        return {}

    def get_token(self, obj):
        result = {
            'category': obj.token['category'],
            'symbol': obj.token['symbol'],
            'decimals': obj.token['decimals'] 
        }

        if obj.token['is_nft']:
            result['nfts'] = {
                'description': obj.token['nft_description'],
                'fields': {},
                'parse': {
                    'bytecode': '',
                    'types': obj.token['nft_types']
                }
            }
        
        return result


class BcmrRegistrySerializer(serializers.ModelSerializer):
    version = serializers.SerializerMethodField()
    latestRevision = serializers.SerializerMethodField()
    registryIdentity = serializers.SerializerMethodField()
    identities = serializers.SerializerMethodField()

    class Meta:
        model = Registry
        fields = (
            'version',
            'latestRevision',
            'registryIdentity',
            'identities',
        )

    def get_version(self, obj):
        return {
            'major': obj.major,
            'minor': obj.minor,
            'patch': obj.patch
        }

    def get_latestRevision(self, obj):
        return obj.latest_revision

    def get_registryIdentity(self, obj):
        return {
            'name': obj.name,
            'description': obj.description
        }

    def get_identities(self, obj):
        tokens = obj.tokens.all()
        identities = {}

        for token in tokens:
            token_histories = TokenHistory.objects.filter(token__category=token.category)

            for token_history in token_histories:
                identity = TokenHistorySerializer(token_history)
                timestamp = token_history.date.isoformat()
                identities[token.category] = {}
                identities[token.category][timestamp] = identity.data

        return identities
