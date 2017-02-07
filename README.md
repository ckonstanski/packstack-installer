# Overview

Welcome to the packstack-installer ansible playbook.

# Prerequisites

- A (set of) CentOS server(s) that have a minimal CentOS OS
  installation plus an ssh pubkey preinstalled for ansible to use.
  
- A workstation with ansible installed, and containing the private key
  matching the public key that you installed on the server(s).
  
- An ansible.cfg file which points to the private key. Here's an
  example:
  
```
[defaults]
host_key_checking = False
remote_user = root
log_path = /var/log/ansible/log
private_key_file = /root/.ssh/id_rsa
forks = 40

[ssh_connection]
pipelining = True

[privilege_escalation]
become = True
become_user = root
become_method = sudo
```

