
from django.contrib import admin
from django.urls import include, path

from api.views import AnalyzeDepressionView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('analyze/', AnalyzeDepressionView.as_view(), name='analyze_text'),

]

