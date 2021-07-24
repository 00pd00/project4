from django.shortcuts import render
import openpyxl
# Create your views here.
from .models import *



def demo(request):
    if request.method == "POST":
        ex_file = request.FILES['excelfile']
        
        read_excel = openpyxl.load_workbook(ex_file)
        worksheet = read_excel["Sheet1"]
        data = list()
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            data.append(row_data)
            
        print(data)

        for i in data:
            da = MyData1(date = i[3],)
            da.save()



    else:
        pass
    return render(request,'demo.html')