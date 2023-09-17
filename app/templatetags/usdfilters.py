from django import template

register=template.Library()

def count(data,arg):
    l=len(arg)
    add=0
    for i in range(len(data)):
        if data[i:i+l] == arg:
             add+=1
    return add
        
register.filter('count',count)