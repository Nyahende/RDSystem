import matplotlib.pyplot as plt
from io import BytesIO
from django.http import HttpResponse
from MonitoringData.models import Monitoring

def report_chart(request):
    monitorings = Monitoring.objects.all()

    dates = [monitoring.monitoring_date for monitoring in monitorings]
    counts = [monitoring.pestmonitoringdata_set.count() for monitoring in monitorings]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, counts, marker='o')
    plt.title('Pest Monitoring Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Pests Observed')
    plt.grid(True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    return HttpResponse(buffer, content_type='image/png')
