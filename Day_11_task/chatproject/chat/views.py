from django.shortcuts import render

# def chat_view(request):
#     return render(request, 'chat.html')

def chat_view(request, username):
    return render(request, 'chat.html', {'username': username})
