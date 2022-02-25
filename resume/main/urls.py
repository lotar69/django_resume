from django.urls import path
from main.views import IndexView, ContactView, PortfolioView, PortfolioDetailView, BlogView, BlogDetailView

app_name = "main"

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('portfolio/', PortfolioView.as_view(), name="portfolios"),
    path('portfolio/<slug:slug>', PortfolioDetailView.as_view(), name="portfolio"),
    path('blog/', BlogView.as_view(), name="blogs"),
    path('blog/<slug:slug>', BlogDetailView.as_view(), name="blog"),
    ]