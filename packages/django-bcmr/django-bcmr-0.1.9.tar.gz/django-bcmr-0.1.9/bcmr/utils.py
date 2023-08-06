from bcmr.models import (
    AuthToken,
    TokenHistory,
    Token,
)


def generate_auth_token():
    a = AuthToken()
    a.save()
    return a


def record_token_history(category):
    token = Token.objects.get(category=category)

    icon = ''
    owner = None
    
    if token.icon:
        icon = token.icon.url
    if token.owner:
        owner = token.owner.id

    token_data = {
        'category': token.category,
        'name': token.name,
        'description': token.description,
        'symbol': token.symbol,
        'decimals': token.decimals,
        'icon': icon,
        'is_nft': token.is_nft,
        'nft_description': token.nft_description,
        'nft_types': token.nft_types,
        'status': token.status,
        'owner': owner
    }
    TokenHistory(token=token_data).save()
