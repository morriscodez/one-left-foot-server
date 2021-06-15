"""oneleftfoot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from oneleftfootapi.views import login_user, register_user, DanceUserView, DanceTypeView, \
                                    SkillLevelView, DayView, AvailabilityView, PartnerView, \
                                        DanceTypeJoinView, RoleView, ProfileView, RequestView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'danceusers', DanceUserView, 'danceuser')
router.register(r'dancetypes', DanceTypeView, 'dancetype')
router.register(r'skilllevels', SkillLevelView, 'skilllevel')
router.register(r'days', DayView, 'day')
router.register(r'availability', AvailabilityView, 'available')
router.register(r'partners', PartnerView, 'partner')
router.register(r'mydances', DanceTypeJoinView, 'mydance')
router.register(r'roles', RoleView, 'role')
router.register(r'profile', ProfileView, 'profile')
router.register(r'requests', RequestView, 'request')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
]
