from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Permit, User
from django.template.loader import get_template
from xhtml2pdf import pisa
import datetime
from django.shortcuts import redirect
from .forms import PermitForm, UserForm


def permit_list(request):
    permits = Permit.objects.all()
    return render(request, 'plant_health/permit_list.html', {'permits': permits})

def permit_detail(request, permit_id):
    permit = get_object_or_404(Permit, id=permit_id)
    return render(request, 'plant_health/permit_detail.html', {'permit': permit})

def generate_pdf(request, permit_id):
    permit = get_object_or_404(Permit, id=permit_id)
    return render(request, 'plant_health/permit_detail.html', {'permit': permit})

def permit_detail_print(request, permit_id):
    permit = get_object_or_404(Permit, id=permit_id)
    return render(request, 'plant_health/permit_detail_print.html', {'permit': permit})

# def generate_pdf(request, permit_id):
#     permit = get_object_or_404(Permit, id=permit_id)
#     template_path = 'plant_health/permit_detail.html'
#     context = {'permit': permit}
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'filename="permit_{permit_id}.pdf"'
#     template = get_template(template_path)
#     html = template.render(context)
#     pisa_status = pisa.CreatePDF(html, dest=response)
#     if pisa_status.err:
#         return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response

# def chart_data(request):
#     permits = Permit.objects.all()
#     # Filter permits by station and time period
#     weekly_permits = permits.filter(created_at__gte=datetime.datetime.now() - datetime.timedelta(days=7))
#     monthly_permits = permits.filter(created_at__gte=datetime.datetime.now() - datetime.timedelta(days=30))
#     yearly_permits = permits.filter(created_at__gte=datetime.datetime.now() - datetime.timedelta(days=365))
#     return render(request, 'plant_health/charts.html', {
#         'weekly_permits': weekly_permits,
#         'monthly_permits': monthly_permits,
#         'yearly_permits': yearly_permits
#     })




def create_permit(request):
    if request.method == 'POST':
        form = PermitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('permit_list')
    else:
        form = PermitForm()
    return render(request, 'plant_health/permit_form.html', {'form': form})

def update_permit(request, permit_id):
    permit = get_object_or_404(Permit, id=permit_id)
    if request.method == 'POST':
        form = PermitForm(request.POST, instance=permit)
        if form.is_valid():
            form.save()
            return redirect('permit_list')
    else:
        form = PermitForm(instance=permit)
    return render(request, 'plant_health/permit_form.html', {'form': form})

def delete_permit(request, permit_id):
    permit = get_object_or_404(Permit, id=permit_id)
    if request.method == 'POST':
        permit.delete()
        return redirect('permit_list')
    return render(request, 'plant_health/permit_confirm_delete.html', {'permit': permit})

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'plant_health/user_form.html', {'form': form})

def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'plant_health/user_form.html', {'form': form})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'plant_health/user_confirm_delete.html', {'user': user})




def chart_data(request):
    permits = Permit.objects.all()
    weekly_permits = permits.filter(created_at__gte=datetime.datetime.now() - datetime.timedelta(days=7))
    monthly_permits = permits.filter(created_at__gte=datetime.datetime.now() - datetime.timedelta(days=30))
    yearly_permits = permits.filter(created_at__gte=datetime.datetime.now() - datetime.timedelta(days=365))

    # Calculate statistics for charts
    weekly_applied = weekly_permits.count()
    weekly_rejected = weekly_permits.filter(status='Rejected').count()
    weekly_passed = weekly_permits.filter(status='Pass').count()

    monthly_applied = monthly_permits.count()
    monthly_rejected = monthly_permits.filter(status='Rejected').count()
    monthly_passed = monthly_permits.filter(status='Pass').count()

    yearly_applied = yearly_permits.count()
    yearly_rejected = yearly_permits.filter(status='Rejected').count()
    yearly_passed = yearly_permits.filter(status='Pass').count()

    weekly_revenue = sum([permit.total_charge for permit in weekly_permits])
    monthly_revenue = sum([permit.total_charge for permit in monthly_permits])
    yearly_revenue = sum([permit.total_charge for permit in yearly_permits])

    return render(request, 'plant_health/charts.html', {
        'weekly_applied': weekly_applied,
        'weekly_rejected': weekly_rejected,
        'weekly_passed': weekly_passed,
        'monthly_applied': monthly_applied,
        'monthly_rejected': monthly_rejected,
        'monthly_passed': monthly_passed,
        'yearly_applied': yearly_applied,
        'yearly_rejected': yearly_rejected,
        'yearly_passed': yearly_passed,
        'weekly_revenue': weekly_revenue,
        'monthly_revenue': monthly_revenue,
        'yearly_revenue': yearly_revenue,
    })

