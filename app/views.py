from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from django.http import HttpResponse
# Create your views here.

"""

=> First install the following package
pip install --pre xhtml2pdf 

"""
###function that helps to generate the pdf file
def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

def home(request):
  return render(request,'app/index.html')

def view_pdf(request):
  data = {
	'customer':'waseem',
  'amount':'$25',
  'date':'25/2/2020'
	}
  pdf = render_to_pdf('app/certificate.html', data)
  return HttpResponse(pdf, content_type='application/pdf')


def download_pdf(request):
  data = {
	'customer':'waseem',
  'amount':'$25',
  'date':'25/2/2020'
	}
  pdf = render_to_pdf('app/certificate.html', data)
  response = HttpResponse(pdf, content_type='application/pdf')
  filename = "Invoice_%s.pdf" %("12341231")
  content = "attachment; filename=%s" %(filename)
  response['Content-Disposition'] = content
  return response
