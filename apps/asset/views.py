from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Host
from .forms import ServerAddForm
from django.http import HttpResponseRedirect
# Create your views here.
def asset_server(request):

    host = Host.objects.all()
    server_num = Host.objects.filter(asset_type="server").count()
    virtual_num = Host.objects.filter(asset_type="virtual").count()
    return render(request,'asset-server.html',{
        'host':host,
        'server_num':server_num,
        'virtual_num':virtual_num})

def server_add(request):
    '''
    主机添加
    :param request: 
    :return: 
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
    return render(request,'server-add.html',{'form': form})


def server_del(request):
    '''
    主机删除
    :param request: 
    :return: 
    '''
    hostid = request.GET.get("hostid")
    # print(hostid)
    Host.objects.filter(id=hostid).delete()
    return HttpResponseRedirect('/asset_server/')