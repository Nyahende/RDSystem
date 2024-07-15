from django.shortcuts import render, redirect
from MonitoringData.forms import MonitoringForm, CropPlantInfoForm, PestMonitoringDataForm, DiseaseMonitoringDataForm, EnvironmentalConditionForm, ManagementPracticeForm, DataCollectionToolForm, AttachmentMediaForm
from MonitoringData.models import Monitoring

def create_monitoring(request):
    if request.method == 'POST':
        monitoring_form = MonitoringForm(request.POST)
        crop_form = CropPlantInfoForm(request.POST)
        pest_form = PestMonitoringDataForm(request.POST)
        disease_form = DiseaseMonitoringDataForm(request.POST)
        env_form = EnvironmentalConditionForm(request.POST)
        manage_form = ManagementPracticeForm(request.POST)
        data_form = DataCollectionToolForm(request.POST)
        attachment_form = AttachmentMediaForm(request.POST, request.FILES)

        if all([monitoring_form.is_valid(), crop_form.is_valid(), pest_form.is_valid(), disease_form.is_valid(), env_form.is_valid(), manage_form.is_valid(), data_form.is_valid(), attachment_form.is_valid()]):
            monitoring = monitoring_form.save()
            crop = crop_form.save(commit=False)
            crop.monitoring = monitoring
            crop.save()

            pest = pest_form.save(commit=False)
            pest.monitoring = monitoring
            pest.save()

            disease = disease_form.save(commit=False)
            disease.monitoring = monitoring
            disease.save()

            env = env_form.save(commit=False)
            env.monitoring = monitoring
            env.save()

            manage = manage_form.save(commit=False)
            manage.monitoring = monitoring
            manage.save()

            data = data_form.save(commit=False)
            data.monitoring = monitoring
            data.save()

            attachment = attachment_form.save(commit=False)
            attachment.monitoring = monitoring
            attachment.save()

            return redirect('monitoring_list')

    else:
        monitoring_form = MonitoringForm()
        crop_form = CropPlantInfoForm()
        pest_form = PestMonitoringDataForm()
        disease_form = DiseaseMonitoringDataForm()
        env_form = EnvironmentalConditionForm()
        manage_form = ManagementPracticeForm()
        data_form = DataCollectionToolForm()
        attachment_form = AttachmentMediaForm()

    return render(request, 'monitoring/create_monitoring.html', {
        'monitoring_form': monitoring_form,
        'crop_form': crop_form,
        'pest_form': pest_form,
        'disease_form': disease_form,
        'env_form': env_form,
        'manage_form': manage_form,
        'data_form': data_form,
        'attachment_form': attachment_form,
    })

def monitoring_list(request):
    monitorings = Monitoring.objects.all()
    return render(request, 'monitoring/monitoring_list.html', {'monitorings': monitorings})

def monitoring_detail(request, pk):
    monitoring = Monitoring.objects.get(pk=pk)
    return render(request, 'monitoring/monitoring_detail.html', {'monitoring': monitoring})
