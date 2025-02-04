from django.shortcuts import render, redirect
from .form import AttestForm  # ✅ Import to'g'ri ekanligini tekshiring

# Create your views here.
def homeView(request):
    form = AttestForm()  # ✅ Formani POST bo'lmagan holatlar uchun ham yaratish kerak

    if request.method == "POST":
        form = AttestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")  # ✅ URL nomi to'g'ri ekanligini tekshiring
    
    return render(request, "home.html", {"form": form})  # ✅ Formani har qanday holatda ham qaytaramiz

def successView(request):
    return render(request, "success.html")
