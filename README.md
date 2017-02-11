# Overview

Welcome to the packstack-installer ansible playbook.

# Prerequisites

- A (set of) CentOS server(s) that have a minimal CentOS installation
  plus an ssh pubkey preinstalled for ansible to use in
  /root/.ssh/authorized_keys.
  
- A workstation with ansible installed, and containing the private key
  matching the public key that you installed on the server(s).
  
- An SSH config file (usually in /root/.ssh/config) which contains
  entry(ies) for the server(s) so that ansible can find them by
  name. Example:
  
  ```
  TcpKeepAlive yes
  ServerAliveInterval 60
  ForwardAgent yes

  Host packstack
  HostName packstack.local
  User root
  StrictHostKeyChecking no
  UserKnownHostsFile=/dev/null
  ```
  
- If necessary, entry(ies) in /etc/hosts so that the hostnames in the
  SSH config file can be resolved.

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

# Pre-Flight Checks

After cloning the repo, go into the conf/ directory and make a copy
of env.yaml.example called env.yaml. Go through env.yaml thoroughly
and make all necessary customizations.

# Running the Plybook

This playbook needs to be run as root.

The contents of env.yaml are used to create global variables in the
ansible playbook. To run ansible using env.yaml, use the following
command line:

```
sudo ansible-playbook -i dynamic_hosts_dev.py install.yaml
```

If ansible cannot reach the server(s), you can use the following to
test while troubleshooting DNS, SSH, etc:

```
sudo ansible target -i dynamic_hosts_dev.py -m ping
```
