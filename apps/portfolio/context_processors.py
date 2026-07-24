from .models import Profile, SocialLink
def site_profile(request):
    return {'site_profile': Profile.objects.first(), 'site_social_links': SocialLink.objects.filter(is_active=True).order_by('order')}
