from django.urls import path,include
from sub_part import views
urlpatterns=[
    path('login',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('',views.home,name='home'),
    path('join_group',views.join_group,name='join_group'),
    path('proceed',views.proceed,name='proceed'),
    path('create_group',views.create_group,name='create_group'),
    path('viewapi',views.viewapi,name='viewapi'),
    path('member_contribution/', views.member_contribution, name='member_contribution'),
    path('view_member_contribution/', views.view_member_contribution, name='view_member_contribution'),
    path('borrow_loan/', views.borrow_loan, name='borrow_loan'),
    path('fund_loan/', views.fund_loan, name='fund_loan'),
    path('fund_loan_add/', views.fund_loan_add, name='fund_loan_add'),
    path('repay_loan/', views.repay_loan, name='repay_loan'),
    path('index/', views.index, name='index'),

  ]