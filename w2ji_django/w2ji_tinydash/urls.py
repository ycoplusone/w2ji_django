from django.urls import path 
from . import views

app_name = 'w2ji_tinydash'
urlpatterns = [    
    path('ui-index/'                    , views.index.as_view()     ) ,
    
    
    path('dashboard-analytics/'         , views.dashboardanalytics.as_view()   ) , 
    path('dashboard-sales/'         , views.dashboardsales.as_view()   ) , 
    path('dashboard-saas/'         , views.dashboardsaas.as_view()   ) ,
    path('dashboard-system/'         , views.dashboardsystem.as_view()   ) , 
    
    
    
    path('ui-color/'                    , views.uicolor.as_view()   ) ,    
    path('ui-typograpy/'                , views.uitypograpy.as_view()   ) ,
    path('ui-icons/'                    , views.uiicons.as_view()   ) ,
    path('ui-buttons/'                  , views.uibuttons.as_view() ) ,
    path('ui-notification/'             , views.uinotification.as_view()   ) ,
    path('ui-modals/'                   , views.uimodals.as_view()   ) ,
    path('ui-tabs-accordion/'           , views.uitabsaccordion.as_view()   ) ,
    path('ui-progress/'                 , views.uiprogress.as_view()   ) ,
    path('ui-calendar/'                 , views.calendar.as_view()   ) ,
    
    
    path('widgets/'                     , views.widgets.as_view()   ) ,
    
    path('form_advanced/'                   , views.form_advanced.as_view()   ) ,
    path('form_elements/'                   , views.form_elements.as_view()   ) ,
    path('form_layouts/'                    , views.form_layouts.as_view()   ) ,
    path('form_upload/'                     , views.form_upload.as_view()   ) ,
    path('form_validation/'                 , views.form_validation.as_view()   ) ,
    path('form_wizard/'                     , views.form_wizard.as_view()   ) ,
    
    path('table_basic/'                     , views.table_basic.as_view()   ) ,
    path('table_advanced/'                  , views.table_advanced.as_view()   ) ,
    path('table_datatables/'                  , views.table_datatables.as_view()   ) ,
    
    
]
