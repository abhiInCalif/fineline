from django.shortcuts import render

class bouncingBots(View):
    def get(self, request,*args,**kwargs):
        render(request, "bouncingBots.html")
 