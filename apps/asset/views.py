from django.shortcuts import render

# Create your views here.
import json
from django.db.models import Q
from django.shortcuts import render
from .models import Host, Manufactory, Supplier,IDC
from .forms import ServerAddForm, SupplierForm, ManufactoryForm
from django.http import HttpResponseRedirect, HttpResponse
from .outexcel import excel_output


# Create your views here.
def asset_server(request):
    host = Host.objects.all()
    server_num = Host.objects.filter(asset_type="服务器").count()
    virtual_num = Host.objects.filter(asset_type="虚拟机").count()
    idcs = IDC.objects.all()
    manufactorys = Manufactory.objects.all()
    return render(request, 'asset_server.html', {
        'host': host,
        'server_num': server_num,
        'virtual_num': virtual_num,
        'idcs':idcs,
        'manufactorys':manufactorys,})

def change_filter(request):
    os_type_word = request.GET.get('os_type')
    asset_type_word = request.GET.get('asset_type')
    idc_word = request.GET.get('idc')
    manufactory_word = request.GET.get('manufactory')

    host_list = Host.objects.filter(Q(os_type=os_type_word) |
                                    Q(asset_type=asset_type_word) |
                                    Q(idc__name=idc_word) |
                                    Q(manufactory__name=manufactory_word))

    return render(request, 'change_filter.html',{'host': host_list})

def server_search(request):
    keyword = request.GET.get('q')
    error_msg = '请输入关键词'
    blank_msg = '没有搜索到符合条件的主机'

    if not keyword:
        return render(request, 'asset_server.html', {'error_msg': error_msg})

    match_list = Host.objects.filter(Q(ip_managemant__icontains=keyword) |
                                     Q(ip_other1__icontains=keyword) |
                                     Q(ip_other2__icontains=keyword) |
                                     Q(os_type__icontains=keyword) |
                                     Q(mac_address__icontains=keyword) |
                                     Q(sn__icontains=keyword) |
                                     Q(asset_type__contains=keyword) |
                                     Q(model__icontains=keyword) |
                                     Q(trade_date__icontains=keyword) |
                                     Q(expire_date__icontains=keyword) )


    # Q(manufactory__icontains=keyword) |
    # Q(supplier__icontains=keyword) |

    # Q(idc__icontains=keyword)

    return render(request, 'asset_server.html', {'host': match_list, 'blank_msg': blank_msg})


def output_excel(request):
    """
    excel 导出 
    """
    host = Host.objects.all()
    excel_output(host)
    return HttpResponseRedirect('/asset_server/')


def server_add(request):
    """
    主机添加
    """
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
    """
    主机删除
    """

    response = {'code': 200, 'message': '删除成功！'}
    hostid = request.GET.get("hostid")

    try:
         Host.objects.filter(id=hostid).delete()

    except:
        response['code'] = 100
        response['message'] = '删除失败！'
    return HttpResponse(json.dumps(response))


def server_edit(request, nid):
    """
    主机编辑
    """
    server_obj = Host.objects.filter(id=nid).first()
    if request.method == 'GET':

        form = ServerAddForm(instance=server_obj)
        return render(request, 'server_edit.html', {'form': form, 'nid': nid, })
    elif request.method == 'POST':
        form = ServerAddForm(request.POST, instance=server_obj)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'server_edit.html', {'form': form, 'nid': nid, })

    return HttpResponseRedirect('/asset_server/')


def server_detail(request, nid):
    """
    主机详情
    """

    if request.method == 'GET':
        host = Host.objects.get(id=nid)
        return render(request, 'server_detail.html', {'host': host, })


def supplier_add(request):
    """
    供应商添加 
    """
    response = {'message': '添加成功！'}

    if request.method == 'POST':
        try:
            supplier_form = SupplierForm(request.POST)
            if supplier_form.is_valid():
                supplier_form.save()
                return HttpResponse(response['message'])
        except:
            response['message'] = '添加失败！'
            return HttpResponse(response['message'])
    else:
        supplier_form = SupplierForm()
    return render(request, 'supplier_add.html', {'supplier_form': supplier_form, })


def supplier_edit(request, sid):
    """
    供应商修改 
    """
    response = {'message': '修改成功！'}
    supp_obj = Supplier.objects.filter(id=sid).first()
    if request.method == 'POST':
        try:
            supplier_form = SupplierForm(request.POST, instance=supp_obj)
            if supplier_form.is_valid():
                supplier_form.save()
                return HttpResponse(response['message'])
        except:
            response['message'] = '修改失败！'
            return HttpResponse(response['message'])
    else:

        supplier_form = SupplierForm(instance=supp_obj)
    return render(request, 'supplier_edit.html', {'supplier_form': supplier_form, 'sid': sid})


def supplier_del(request, sid):
    """
    供应商删除
    """
    response = {'message': '删除成功！'}

    try:
        print(sid)
        Supplier.objects.filter(id=sid).delete()

    except:
        response['message'] = '删除失败！'
    return HttpResponse(response['message'])


def manufactory_add(request):
    """
    制造商添加 
    """
    response = {'message': '添加成功！'}

    if request.method == 'POST':
        try:
            manufactory_form = ManufactoryForm(request.POST)
            if manufactory_form.is_valid():
                manufactory_form.save()
                return HttpResponse(response['message'])
        except:
            response['message'] = '添加失败！'
            return HttpResponse(response['message'])
    else:
        manufactory_form = ManufactoryForm()
    return render(request, 'manufactory_add.html', {'manufactory_form': manufactory_form, })


def manufactory_edit(request, mid):
    """
    制造商修改 
    """
    response = {'message': '修改成功！'}
    manu_obj = Manufactory.objects.filter(id=mid).first()
    if request.method == 'POST':
        try:
            manufactory_form = ManufactoryForm(request.POST, instance=manu_obj)
            if manufactory_form.is_valid():
                manufactory_form.save()
                return HttpResponse(response['message'])
        except:
            response['message'] = '修改失败！'
            return HttpResponse(response['message'])
    else:
        manufactory_form = ManufactoryForm(instance=manu_obj)
    return render(request, 'manufactory_edit.html', {'manufactory_form': manufactory_form, 'mid': mid})


def manufactory_del(request, mid):
    """
    制造商删除
    """
    response = {'message': '删除成功！'}
    print(mid)
    try:
        Manufactory.objects.filter(id=mid).delete()

    except:
        response['message'] = '删除失败！'
    return HttpResponse(response['message'])
