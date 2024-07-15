from django import forms
from .models import Monitoring, CropPlantInfo, PestMonitoringData, DiseaseMonitoringData, EnvironmentalCondition, ManagementPractice, DataCollectionTool, AttachmentMedia

class MonitoringForm(forms.ModelForm):
    class Meta:
        model = Monitoring
        fields = '__all__'

class CropPlantInfoForm(forms.ModelForm):
    class Meta:
        model = CropPlantInfo
        fields = '__all__'

class PestMonitoringDataForm(forms.ModelForm):
    class Meta:
        model = PestMonitoringData
        fields = '__all__'

class DiseaseMonitoringDataForm(forms.ModelForm):
    class Meta:
        model = DiseaseMonitoringData
        fields = '__all__'

class EnvironmentalConditionForm(forms.ModelForm):
    class Meta:
        model = EnvironmentalCondition
        fields = '__all__'

class ManagementPracticeForm(forms.ModelForm):
    class Meta:
        model = ManagementPractice
        fields = '__all__'

class DataCollectionToolForm(forms.ModelForm):
    class Meta:
        model = DataCollectionTool
        fields = '__all__'

class AttachmentMediaForm(forms.ModelForm):
    class Meta:
        model = AttachmentMedia
        fields = '__all__'
