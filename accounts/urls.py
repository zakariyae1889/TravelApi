from django.urls import path


from .views import Authentication

urlpatterns = [
   path('singup/',Authentication.signup_view),
   path('login/',Authentication.login_views),

   path('logout/',Authentication.logout_views),

   path('current_user/',Authentication.current_user),

   path('changePassword/',Authentication.changePassword)

]