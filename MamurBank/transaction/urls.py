from django.urls import path
from . import views

urlpatterns = [
    path('deposit/',views.DepositMoneyView.as_view(),name='deposit'),
    path('withdraw/',views.WithdrawMoneyView.as_view(),name='withdraw'),
    path('loan_request/',views.LoanRequestView.as_view(),name='loan_request'),
    path("loans/", views.LoanListView.as_view(), name="loan_list"),
    path("loans/<int:loan_id>/", views.PayLoanView.as_view(), name="pay"),
    path("report/", views.TransactionReportView.as_view(), name="transaction_report"),
]
