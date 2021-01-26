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
    
    path('chart_apexcharts/'                , views.chart_apexcharts.as_view()   ) ,
    path('chart_chartjs/'                   , views.chart_chartjs.as_view()   ) ,
    path('chart_datamaps/'                  , views.chart_datamaps.as_view()   ) ,
    path('chart_inline/'                    , views.chart_inline.as_view()   ) ,
    
    path('contacts_grid/'                    , views.contacts_grid.as_view()   ) ,
    path('contacts_list/'                    , views.contacts_list.as_view()   ) ,
    path('contacts_new/'                    , views.contacts_new.as_view()   ) ,
    
    path('files_grid/'                    , views.files_grid.as_view()   ) ,
    path('files_list/'                    , views.files_list.as_view()   ) ,
    
    path('page_404/'                    , views.page_404.as_view()   ) ,
    path('page_500/'                    , views.page_500.as_view()   ) ,
    path('page_blank/'                    , views.page_blank.as_view()   ) ,    
    path('page_invoice/'                    , views.page_invoice.as_view()   ) ,
    path('page_orders/'                    , views.page_orders.as_view()   ) ,
    path('page_timeline/'                    , views.page_timeline.as_view()   ) ,
    
    path('auth-confirm/'                    , views.auth_confirm.as_view()   ) ,
    path('auth-login/'                    , views.auth_login.as_view()   ) ,
    path('auth-login-half/'                    , views.auth_login_half.as_view()   ) ,
    path('auth-register/'                    , views.auth_register.as_view()   ) ,
    path('auth-resetpw/'                    , views.auth_resetpw.as_view()   ) ,    
    
    path('profile/'                    , views.profile.as_view()   ) ,
    path('profile_notification/'                    , views.profile_notification.as_view()   ) ,
    path('profile_security/'                    , views.profile_security.as_view()   ) ,
    path('profile_settings/'                    , views.profile_settings.as_view()   ) ,
    
    path('support_center/'                    , views.support_center.as_view()   ) ,
    path('support_faqs/'                    , views.support_faqs.as_view()   ) ,
    path('support_ticket_detail/'                    , views.support_ticket_detail.as_view()   ) ,
    path('support_ticket/'                    , views.support_ticket.as_view()   ) ,
    
    path('test-index/'                    , views.test_index.as_view()   ) ,
    path('test-master/'                    , views.test_master.as_view()   ) ,
    
    

    
    
    
    
]

