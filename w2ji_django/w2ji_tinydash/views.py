from django.shortcuts import render
from django.views.generic.base import TemplateView


class index(TemplateView):  #목록보기
    template_name = 'index.html' #뷰 전용 템플릿 생성
    queryset = None #models.bbs.objects.all() #모든 게시글을 가져온다.
    
    def get(self, request, *args, **kwargs):
        ctx = { 
            'view' : self.__class__.__name__ , #클래스의 이름
            #'lists' : self.get_queryset() ,    #self.queryset #걸색결과 
        }    #템플릿에 전달할 데이터
        return self.render_to_response(ctx)



class dashboardanalytics(TemplateView):
    template_name = 'dashboard-analytics.html'

class dashboardsales(TemplateView):
    template_name = 'dashboard-sales.html'

class dashboardsaas(TemplateView):
    template_name = 'dashboard-saas.html'   

class dashboardsystem(TemplateView):
    template_name = 'dashboard-system.html'    

class uicolor(TemplateView):
    template_name = 'ui-color.html' #뷰 전용 템플릿 생성

class uitypograpy(TemplateView):
    template_name = 'ui-typograpy.html' #뷰 전용 템플릿 생성

class uiicons(TemplateView):
    template_name = 'ui-icons.html' #뷰 전용 템플릿 생성

class uibuttons(TemplateView):
    template_name = 'ui-buttons.html' #뷰 전용 템플릿 생성

class uinotification(TemplateView):
    template_name = 'ui-notification.html' #뷰 전용 템플릿 생성

class uimodals(TemplateView):
    template_name = 'ui-modals.html' #뷰 전용 템플릿 생성

class uitabsaccordion(TemplateView):
    template_name = 'ui-tabs-accordion.html' #뷰 전용 템플릿 생성

class uiprogress(TemplateView):
    template_name = 'ui-progress.html' #뷰 전용 템플릿 생성

class calendar(TemplateView):
    template_name = 'calendar.html'

class widgets(TemplateView):
    template_name = 'widgets.html' #뷰 전용 템플릿 생성        

class form_advanced(TemplateView):
    template_name = 'form_advanced.html' #뷰 전용 템플릿 생성
    
class form_elements(TemplateView):
    template_name = 'form_elements.html' #뷰 전용 템플릿 생성
    
class form_layouts(TemplateView):
    template_name = 'form_layouts.html' #뷰 전용 템플릿 생성        

class form_upload(TemplateView):
    template_name = 'form_upload.html' #뷰 전용 템플릿 생성
    
class form_validation(TemplateView):
    template_name = 'form_validation.html' #뷰 전용 템플릿 생성
    
class form_wizard(TemplateView):
    template_name = 'form_wizard.html' #뷰 전용 템플릿 생성
    
class table_basic(TemplateView):
    template_name = 'table_basic.html' #뷰 전용 템플릿 생성    

class table_advanced(TemplateView):
    template_name = 'table_advanced.html' #뷰 전용 템플릿 생성    

class table_datatables(TemplateView):
    template_name = 'table_datatables.html' #뷰 전용 템플릿 생성    

class chart_apexcharts(TemplateView):
    template_name = 'chart_apexcharts.html' #뷰 전용 템플릿 생성
    
class chart_chartjs(TemplateView):
    template_name = 'chart_chartjs.html' #뷰 전용 템플릿 생성    

class chart_datamaps(TemplateView):
    template_name = 'chart_datamaps.html' #뷰 전용 템플릿 생성
    
class chart_inline(TemplateView):
    template_name = 'chart_inline.html' #뷰 전용 템플릿 생성

class contacts_grid(TemplateView):
    template_name = 'contacts-grid.html' #뷰 전용 템플릿 생성    

class contacts_list(TemplateView):
    template_name = 'contacts-list.html' #뷰 전용 템플릿 생성    
    
class contacts_new(TemplateView):
    template_name = 'contacts-new.html' #뷰 전용 템플릿 생성    

class files_grid(TemplateView):
    template_name = 'files-grid.html' #뷰 전용 템플릿 생성    

class files_list(TemplateView):
    template_name = 'files-list.html' #뷰 전용 템플릿 생성    
    
class page_404(TemplateView):
    template_name = 'page-404.html' #뷰 전용 템플릿 생성
        
class page_500(TemplateView):
    template_name = 'page-500.html' #뷰 전용 템플릿 생성
    
class page_blank(TemplateView):
    template_name = 'page-blank.html' #뷰 전용 템플릿 생성

class page_invoice(TemplateView):
    template_name = 'page-invoice.html' #뷰 전용 템플릿 생성

class page_orders(TemplateView):
    template_name = 'page-orders.html' #뷰 전용 템플릿 생성

class page_timeline(TemplateView):
    template_name = 'page-timeline.html' #뷰 전용 템플릿 생성
    

class auth_confirm(TemplateView):
    template_name = 'auth-confirm.html' #뷰 전용 템플릿 생성
    
class auth_login(TemplateView):
    template_name = 'auth-login.html' #뷰 전용 템플릿 생성


class auth_login_half(TemplateView):
    template_name = 'auth-login-half.html' #뷰 전용 템플릿 생성            

class auth_register(TemplateView):
    template_name = 'auth-register.html' #뷰 전용 템플릿 생성
    
class auth_resetpw(TemplateView):
    template_name = 'auth-resetpw.html' #뷰 전용 템플릿 생성    

class profile(TemplateView):
    template_name = 'profile.html' #뷰 전용 템플릿 생성    

class profile_notification(TemplateView):
    template_name = 'profile-notification.html' #뷰 전용 템플릿 생성

class profile_security(TemplateView):
    template_name = 'profile-security.html' #뷰 전용 템플릿 생성    

class profile_settings(TemplateView):
    template_name = 'profile-settings.html' #뷰 전용 템플릿 생성
    
class support_center(TemplateView):
    template_name = 'support-center.html' #뷰 전용 템플릿 생성

class support_faqs(TemplateView):
    template_name = 'support-faqs.html' #뷰 전용 템플릿 생성

class support_ticket_detail(TemplateView):
    template_name = 'support-ticket-detail.html' #뷰 전용 템플릿 생성

class support_ticket(TemplateView):
    template_name = 'support-tickets.html' #뷰 전용 템플릿 생성    

class test_index(TemplateView):
    template_name = 'test-index.html' #뷰 전용 템플릿 생성    
