from django.shortcuts import render

# Create your views here.
import json
from django.shortcuts import render
from .models import Host
from .forms import ServerAddForm, SupplierForm, ManufactoryForm
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
def asset_server(request):
    host = Host.objects.all()
    server_num = Host.objects.filter(asset_type="server").count()
    virtual_num = Host.objects.filter(asset_type="virtual").count()
    return render(request, 'asset_server.html', {
        'host': host,
        'server_num': server_num,
        'virtual_num': virtual_num})


def server_add(request):
    '''
    主机添加
    '''
    if request.method == 'POST':
        # ip_managemant = form.cleaned_data['ipmanagemant']
        # ip_other1 = form.cleaned_data['ip_other1']
        # ip_other2 = form.cleaned_data['ip_other2']
        # # os_type = form.cleaned_data['os_type']
        # os_release = form.cleaned_data['os_release']
        # cpu_physics_count = form.cleaned_data['cpu_physics_count']
        # cpu_core_count = form.cleaned_data['']
        # cpu_logic_count = form.cleaned_data['']
        # mem_capacity = form.cleaned_data['']
        # disk_capacity = form.cleaned_data['']
        # raid_type = form.cleaned_data['']
        # mac_address = form.cleaned_data['']
        # name = form.cleaned_data['']
        # sn = form.cleaned_data['']
        # asset_type = form.cleaned_data['']
        # model = form.cleaned_data['']
        # manufactory = form.cleaned_data['']
        # supplier = form.cleaned_data['']
        # trade_date = form.cleaned_data['']
        # expire_date = form.cleaned_data['']
        # idc = form.cleaned_data['']
        # cabinet = form.cleaned_data['']
        # cabinet_uid = form.cleaned_data['']
        # memo = form.cleaned_data['']

        form = ServerAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/asset_server/')
    else:
        form = ServerAddForm()
    return render(request, 'server_add.html', {'form': form})


def server_del(request):
    '''
    主机删除
    '''
    response = {'code': 200, 'message': '删除成功！'}
    hostid = request.GET.get("hostid")
    try:
        Host.objects.filter(id=hostid).delete()

    except:
        response['code'] = 100
        response['message'] = '删除失败！'
    return HttpResponse(json.dumps(response))


def server_edit(request, nid):
    '''
    主机编辑
    '''
    if request.method == 'GET':

        server_obj = Host.objects.filter(id=nid).first()
        form = ServerAddForm(instance=server_obj)
        return render(request, 'server_edit.html', {'form': form, 'nid': nid, })
    elif request.method == 'POST':

        server_obj = Host.objects.filter(id=nid).first()
        form = ServerAddForm(request.POST, instance=server_obj)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/asset_server/')


def server_detail(request, nid):
    '''
    主机详情
    '''

    if request.method == 'GET':
        host = Host.objects.get(id=nid)
        return render(request, 'server_detail.html', {'host': host, })


def supplier_add(request):
    '''
    供应商添加 
    '''
    response = {'message': '添加成功！'}

    if request.method == 'POST':
        try:
            supplier_form = SupplierForm(request.POST)
            if supplier_form.is_valid():
                supplier_form.save()
                # return render(request,'supplier_add.html',{'supplier_form':supplier_form,})
        except:

            response['message'] = '添加失败！'
        return HttpResponse(response['message'])
    else:
        supplier_form = SupplierForm()
        return render(request, 'supplier_add.html', {'supplier_form': supplier_form, })


def manufactory_add(request):
    '''
    制造商添加 
    '''
    response = {'message': '添加成功！'}

    if request.method == 'POST':
        try:
            manufactory_form = ManufactoryForm(request.POST)
            if manufactory_form.is_valid():
                manufactory_form.save()
                # return render(request,'supplier_add.html',{'supplier_form':supplier_form,})
        except:

            response['message'] = '添加失败！'
        return HttpResponse(response['message'])
    else:
        manufactory_form = ManufactoryForm()
        return render(request, 'manufactory_add.html', {'manufactory_form': manufactory_form, })
