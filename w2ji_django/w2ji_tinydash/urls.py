from django.urls import path 
from . import views

app_name = 'w2ji_tinydash'
urlpatterns = [    
    path(''                             , views.index.as_view()     ) ,
    path('ui-color/'                    , views.uicolor.as_view()   ) ,    
    path('ui-typograpy/'                , views.uitypograpy.as_view()   ) ,
    path('ui-icons/'                    , views.uiicons.as_view()   ) ,
    path('ui-buttons/'                  , views.uibuttons.as_view() ) ,
    path('ui-notification/'             , views.uinotification.as_view()   ) ,
    path('ui-modals/'                   , views.uimodals.as_view()   ) ,
    path('ui-tabs-accordion/'           , views.uitabsaccordion.as_view()   ) ,
    path('ui-progress/'                 , views.uiprogress.as_view()   ) ,
]
