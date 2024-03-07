"""Rent_Tracking URL Configuration

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
from django.urls import path,include

from Track_app import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.log),
    path('log_post',views.log_post),
    path('forgot_password',views.forgot_password),
    path('forgot_password_post',views.forgot_password_post),
    path('admin_home',views.admin_home),
    path('logout',views.logout),
    path('change_password',views.change_password),
    path('change_password_post',views.change_password_post),
    path('add_category',views.add_category),
    path('add_category_post',views.add_category_post),
    path('view_category',views.view_category),
    path('update_category/<id>',views.update_category),
    path('update_category_post/<id>',views.update_category_post),
    path('delete_category/<id>',views.delete_category),
    path('view_store',views.view_store),
    path('approve_store/<id>',views.approve_store),
    path('reject_store/<id>',views.reject_store),
    path('view_approved_store',views.view_approved_store),
    path('view_rejected_store',views.view_rejected_store),
    path('view_user',views.view_user),
    path('view_complaint',views.view_complaint),
    path('send_reply/<id>',views.send_reply),
    path('send_reply_post/<id>',views.send_reply_post),
    path('view_feedback',views.view_feedback),

# ................................................................... STORE MODULE
    path('store_home',views.store_home),
    path('register_store',views.register_store),
    path('register_store_post',views.register_store_post),
    path('view_profile',views.view_profile),
    path('view_categories',views.view_categories),
    path('add_product',views.add_product),
    path('add_product_post',views.add_product_post),
    path('view_product',views.view_product),
    path('update_product/<id>',views.update_product),
    path('update_product_post/<id>',views.update_product_post),
    path('delete_product/<id>',views.delete_product),
    path('store_change_password',views.store_change_password),
    path('store_change_password_post',views.store_change_password_post),
    path('view_rating',views.view_rating),
    path('view_orders',views.view_orders),
    path('approve_order/<id>',views.approve_order),
    path('reject_order/<id>',views.reject_order),
    path('view_approved_order',views.view_approved_order),
    path('view_product_on_rent/<id>',views.view_product_on_rent),
    path('view_order_history',views.view_order_history),
    path('return_entry/<id>',views.return_entry),



# ..........................................................................................USER MODULE
    path('android_login',views.android_login),
    path('android_user_registration',views.android_user_registration),
    path('android_change_password',views.android_change_password),
    path('android_view_profile',views.android_view_profile),
    path('android_edit_profile',views.android_edit_profile),
    path('android_edit_profiles',views.android_edit_profiles),
    path('android_view_products',views.android_view_products),
    path('android_view_store',views.android_view_store),
    path('android_view_rating',views.android_view_rating),
    path('android_send_rating',views.android_send_rating),
    path('android_view_reply',views.android_view_reply),
    path('android_send_complaint',views.android_send_complaint),
    path('android_send_feedback',views.android_send_feedback),
    path('android_add_to_cart',views.android_add_to_cart),
    path('android_view_cart',views.android_view_cart),
    path('android_place_order',views.android_place_order),
    path('android_cancel_order',views.android_cancel_order),
    path('android_view_orders',views.android_view_orders),
    path('android_offline_payment',views.android_offline_payment),
    path('android_online_payment',views.android_online_payment),
]
