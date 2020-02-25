
class Basicmiddleware(object):

    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        print('this is printed by basic midddleware in preprcessing of request')
        response=self.get_response(request)
        print('this is printed by basic midddleware in postprcessing of request')
        return response


from django.http import HttpResponse
class Maintainencemiddleware(object):

    def __init__(self,get_response):
        self.get_response=get_response

    def  __call__(self,request):
        return HttpResponse('<h1> The site is under MAINTAINENCE</h1>')


class Exceptionmiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        response=self.get_response(request)
        return response

    def process_exception(self,request,exception):
        s1='<h2> There is an exception</h2>'
        s2='<h2> RaiseException:{} </h2>'.format(exception.__class__.__name__)
        s3='<h2>Exception Details:{}</h2>'.format(exception)
        return HttpResponse(s1+s2+s3)




class Firstmiddleware(object):
     def __init__(self,get_response):
         self.get_response=get_response

     def __call__(self,request):
         print('This is printed by firstmiddlewate in preprocessing of request')
         response=self.get_response(request)
         print('This is printed by firstmiddlewate in postprocessing of request')
         return response

class Secondmiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        print('This is printed by Secondmiddleware in preprocessing of request')
        response=self.get_response(request)
        print('This is printed by  Secondmiddleware in postprocessing of request')
        return response


class Thirdmiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        print('This is printed by Thirdmiddleware in preprocessing of request')
        response=self.get_response(request)
        print('This is printed by Thirdmiddleware in postprocessing of request')
        return response
