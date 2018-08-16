from django.shortcuts import render

# Create your views here.
import json

from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Host, Manufactory, Supplier,IDC
from .forms import ServerAddForm, SupplierForm, ManufactoryForm,IdcForm
from .outexcel import excel_output
from .tasks import get_info_ansible


# Create your views here.
def asset_server(request):
    host = Host.objects.all()
    server_num = Host.objects.filter(asset_type="server").count()
    virtual_num = Host.objects.filter(asset_type="virtual").count()
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
                                     Q(os_release__icontains=keyword) |
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
    return HttpResponseRedirect(reverse(asset_server))


def server_add(request):
    """
    主机添加
    """
    if request.method == 'POST':
        form = ServerAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(asset_server))
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

    return HttpResponseRedirect(reverse(asset_server))


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
        Supplier.objects.filter(id=sid).delete()
        response['message'] = '删除成功！'

    except Exception as e:
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
    try:
        Manufactory.objects.filter(id=mid).delete()
    except:
        response['message'] = '删除失败！'
    return HttpResponse(response['message'])

def idc_add(request):
    """
    机房添加
    """
    response = {'message': '添加成功！'}
    if request.method == 'POST':
            try:
                idc_form = IdcForm(request.POST)
                if idc_form.is_valid():
                    idc_form.save()
                    return HttpResponse(response['message'])
            except:
                response['message'] = '添加失败！'
                return HttpResponse(response['message'])
    else:
        idc_form = IdcForm()
    return render(request, 'idc_add.html', {'idc_form': idc_form, })

def idc_edit(request, iid):
    """
    机房修改
    """
    response = {'message': '修改成功！'}
    idc_obj = IDC.objects.filter(id=iid).first()
    if request.method == 'POST':
        try:
            idc_form = IdcForm(request.POST, instance=idc_obj)
            if idc_form.is_valid():
                idc_form.save()
                return HttpResponse(response['message'])
        except:
            response['message'] = '修改失败！'
            return HttpResponse(response['message'])
    else:
        idc_form = IdcForm(instance=idc_obj)
    return render(request, 'idc_edit.html', {'idc_form': idc_form, 'iid': iid})

def idc_del(request, iid):
    """
    机房删除
    """
    response = {'message': '删除成功！'}
    try:
        IDC.objects.filter(id=iid).delete()
    except:
        response['message'] = '删除失败！'
    return HttpResponse(response['message'])


def server_update(request,hip):
    # 通过celery执行耗时ansible任务
    ip = hip
    res_setup = get_info_ansible.delay(ip,'setup')
    info = res_setup.get(propagate=False)
    # QuerySet 获取对应IP的对象
    host = Host.objects.get(ip_managemant=ip)
    if info.get('success'):
        ipv4_all = info['success'][ip]['ansible_facts']['ansible_all_ipv4_addresses']
        ipv4_all.remove(ip)
        if len(ipv4_all) >= 1:
            # update ip_other1
            ip_other1 = ipv4_all[0]
            host.ip_other1 = ip_other1
        if len(ipv4_all) >= 2:
            # update ip_other2
            ip_other2 = ipv4_all[1]
            host.ip_other2 = ip_other2
        # update os_type
        os_type=info['success'][ip]['ansible_facts']['ansible_distribution']
        host.os_type = os_type
        # update os_type
        os_release=info['success'][ip]['ansible_facts']['ansible_distribution_version']
        host.os_release = os_release
        # update cpu_physics_count
        cpu_physics_count=info['success'][ip]['ansible_facts']['ansible_processor_count']
        host.cpu_physics_count = cpu_physics_count
        # update cpu_core_count
        cpu_core_count=info['success'][ip]['ansible_facts']['ansible_processor_cores']
        host.cpu_core_count = cpu_core_count
        # update cpu_logic_count
        cpu_logic_count=info['success'][ip]['ansible_facts']['ansible_processor_vcpus']
        host.cpu_logic_count = cpu_logic_count
        # update mem_capacity
        mem_capacity=float(info['success'][ip]['ansible_facts']['ansible_memtotal_mb'])/1024
        host.mem_capacity = mem_capacity
        # update mac_address
        mac_address=info['success'][ip]['ansible_facts']['ansible_default_ipv4']['macaddress']
        host.mac_address = mac_address
        # update sn
        sn = info['success'][ip]['ansible_facts']['ansible_product_serial']
        host.sn = sn
        # update model
        model = info['success'][ip]['ansible_facts']['ansible_product_name']
        host.model = model
        host.save()
    return HttpResponseRedirect(reverse(asset_server))