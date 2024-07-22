from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import COA
from .forms import COAForm

def coa_list(request):
    coa_entries = COA.objects.all()
    form = COAForm()
    return render(request, 'coa.html', {'coa_entries': coa_entries, 'form': form})

def coa_create(request):
    if request.method == 'POST':
        form = COAForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            messages.success(request, 'COA entry created successfully.')
            return redirect('coa_list')
        else:
            if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = COAForm()
    return render(request, 'coa.html', {'form': form})

def ajax_load_detail_types(request):
    account_type = request.GET.get('account_type')
    if account_type:
        detail_types = COA.DETAIL_TYPES.get(account_type, [])
        return JsonResponse({'detail_types': detail_types})
    else:
        return JsonResponse({}, status=400)
