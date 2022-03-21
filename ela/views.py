from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from ela.utils import ELA
# Create your views here.
from PIL import Image 
import base64
from io import BytesIO

def index(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        print(file_url)
        image = ELA(file_url,90)
        # img = Image.fromarray(image, 'RGB')
        # data = BytesIO()
        # img.save('test.png') # pick your format
        # data64 = base64.b64encode(data.getvalue())
        # img_file = u'data:img/jpeg;base64,'+data64.decode('utf-8') 
        print(image)
        image.save('media/test.png')
        img_url = fss.url('test.png')
        print(img_url)
        return render(request, 'index.html', {'file_url': file_url,'img_file':img_url})
    return render(request, 'index.html')


    