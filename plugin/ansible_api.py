#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 16:50
# @Author  : ZJJ
# @Email   : 597105373@qq.com

from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager

from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.plugins.callback import CallbackBase



class ResultCallback(CallbackBase):
    # 自定义 callback，即在运行 api 后调用本类中的 v2_runner_on_ok()，在这里会输出 host 和 result json格式
    def __init__(self, *args, **kwargs):
        super(ResultCallback, self).__init__(*args, **kwargs)
        self.host_ok = {}
        self.host_failed = {}
        self.host_unreachable = {}

    def v2_runner_on_ok(self, result):
        host = result._host.get_name()
        self.host_ok[host] = result

    def v2_runner_on_failed(self, result, *args, **kwargs):
        host = result._host.get_name()
        self.host_failed[host] = result

    def v2_runner_on_unreachable(self, result, *args, **kwargs):
        host = result._host.get_name()
        self.host_unreachable[host] = result

class Ansible_Play(object):
    def __init__(self,sources='/etc/ansible/hosts', *args, **kwargs):
        self.sources = sources
        self.variable_manager = None
        self.loader = None
        self.options = None
        self.passwords = None
        self.callback = ResultCallback()

        self.results_raw = {}

        Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'timeout', 'remote_user',
                                         'ask_pass', 'private_key_file', 'ssh_common_args', 'ssh_extra_args',
                                         'sftp_extra_args',
                                         'scp_extra_args', 'become', 'become_method', 'become_user', 'ask_value_pass',
                                         'verbosity',
                                         'check', 'listhosts', 'listtasks', 'listtags', 'syntax', 'diff'])
        self.options = Options(connection='smart', module_path=None, forks=100, timeout=10,
                               remote_user='root', ask_pass=False, private_key_file=None, ssh_common_args=None,
                               ssh_extra_args=None,
                               sftp_extra_args=None, scp_extra_args=None, become=None, become_method=None,
                               become_user='root', ask_value_pass=False, verbosity=None, check=False, listhosts=False,
                               listtasks=False, listtags=False, syntax=False, diff=False)

        self.loader = DataLoader()
        self.passwords = dict(vault_pass='secret')

        self.inventory = InventoryManager( self.loader, self.sources)
        # 把inventory传递给variable_manager管理
        self.variable_manager = VariableManager(loader=self.loader, inventory=self.inventory)

    def run_Adhoc(self, hosts, module_name, module_args):
        ###########################
        #run module from andible ad-hoc.
        ##########################
        play_source = dict(
            name="Ansible Play",
            hosts=hosts,
            gather_facts='no',
            tasks=[dict(action=dict(module=module_name, args=module_args))]
        )
        play = Play().load(play_source, variable_manager=self.variable_manager, loader=self.loader)

        # actually run it
        tqm = None
        try:
            tqm = TaskQueueManager(
                inventory=self.inventory,
                variable_manager=self.variable_manager,
                loader=self.loader,
                options=self.options,
                passwords=self.passwords,
                stdout_callback=self.callback,
            )
            tqm.run(play)
        finally:
            if tqm is not None:
                tqm.cleanup()

    def run_Playbook(self,yaml_files_list):
        playbook = PlaybookExecutor(
            playbooks=yaml_files_list,
            inventory=self.inventory,
            variable_manager=self.variable_manager,
            loader=self.loader,
            passwords=self.passwords,
            options=self.options,
        )
        playbook._tqm._stdout_callback = self.callback
        playbook.run()


    def get_result(self):
        self.results_raw = {'success': {}, 'failed': {}, 'unreachable': {}}
        for host, result in self.callback.host_ok.items():
            self.results_raw['success'][host] = result._result

        for host, result in self.callback.host_failed.items():
            self.results_raw['failed'][host] = result._result

        for host, result in self.callback.host_unreachable.items():
            self.results_raw['unreachable'][host] = result._result['msg']

        return self.results_raw


if __name__ == '__main__':
    #sources = [{"hostname": "192.168.123.166", "ansible_port": 22, "ansible_user": "root", "ansible_ssh_pass": "123456"},
    #           {"hostname": "192.168.123.168", "ansible_port": 22, "ansible_user": "root", "ansible_ssh_pass": "123456"}]
    ansible = Ansible_Play('/etc/ansible/hosts')
    ## run adhoc
    ansible.run_Adhoc('192.168.123.166','setup','filter=ansible_all_ipv4_addresses')

    ## run playbook
    #ansible.run_Playbook(['/etc/ansible/main.yml'])
    result = ansible.get_result()
    print(result)