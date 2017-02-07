#!/usr/bin/python

from __future__ import print_function
import hashlib
import json
import os
import random
import sys
import yaml


def sha_half():
    return sha()[:16]


def sha():
    return hashlib.sha1(str(random.getrandbits(256)).encode("utf-8")).hexdigest()[:32]


def doit():
    ENV_YAML_PATH = os.path.dirname(__file__) + "/conf/env.yaml"
    environ = ""
    for env in ["dev"]:
        if env in os.path.basename(__file__):
            environ = env
            break
    if environ == "":
        print("Unable to determine environment. Exiting.", file=sys.stderr)
        sys.exit(1)
    if not os.path.isfile(ENV_YAML_PATH):
        print("Unable to find env.yaml. Exiting.", file=sys.stderr)
        sys.exit(1)
    with open(ENV_YAML_PATH, 'r') as stream:
        config = yaml.load(stream)
        hosts = []
        hostvars = {}
        outobj = {}
        for ee in config["environments"]:
            for e in [x for x in ee if x == environ]:
                host = ee[e]["ansible_ssh_host"]
                hosts.append(host)
                hostvars[host] = {"host": host,
                                  "ssh_key": ee[e]["ssh_key"],
                                  "locale": ee[e]["locale"],
                                  "amqp_enable_auth": ee[e]["amqp_enable_auth"],
                                  "amqp_enable_ssl": ee[e]["amqp_enable_ssl"],
                                  "aodh_install": ee[e]["aodh_install"],
                                  "ceilometer_install": ee[e]["ceilometer_install"],
                                  "debug_mode": ee[e]["debug_mode"],
                                  "gnocchi_install": ee[e]["gnocchi_install"],
                                  "heat_install": ee[e]["heat_install"],
                                  "horizon_install": ee[e]["horizon_install"],
                                  "ironic_install": ee[e]["ironic_install"],
                                  "lbaas_install": ee[e]["lbaas_install"],
                                  "manila_install": ee[e]["manila_install"],
                                  "nagios_install": ee[e]["nagios_install"],
                                  "neutron_fwaas": ee[e]["neutron_fwaas"],
                                  "neutron_metering_agent_install": ee[e]["neutron_metering_agent_install"],
                                  "neutron_vpnaas": ee[e]["neutron_vpnaas"],
                                  "provision_demo": ee[e]["provision_demo"],
                                  "run_tempest": ee[e]["run_tempest"],
                                  "sahara_install": ee[e]["sahara_install"],
                                  "swift_install": ee[e]["swift_install"],
                                  "trove_install": ee[e]["trove_install"],
                                  "amqp_auth_password": ee[e]["amqp_auth_password"],
                                  "ceilometer_ks_pw": ee[e]["ceilometer_ks_pw"],
                                  "ceilometer_secret": sha_half(),
                                  "cinder_db_pw": ee[e]["cinder_db_pw"],
                                  "cinder_ks_pw": ee[e]["cinder_ks_pw"],
                                  "default_password": ee[e]["default_password"],
                                  "glance_db_pw": ee[e]["glance_db_pw"],
                                  "glance_keystone_pw": ee[e]["glance_keystone_pw"],
                                  "heat_db_pw": ee[e]["heat_db_pw"],
                                  "heat_domain_password": ee[e]["heat_domain_password"],
                                  "heat_ks_pw": ee[e]["heat_ks_pw"],
                                  "heat_auth_enc_key": sha_half(),
                                  "horizon_secret_key": sha(),
                                  "keystone_admin_pw": ee[e]["keystone_admin_pw"],
                                  "keystone_db_pw": ee[e]["keystone_db_pw"],
                                  "keystone_demo_pw": ee[e]["keystone_demo_pw"],
                                  "keystone_admin_token": sha(),
                                  "mariadb_pw": ee[e]["mariadb_pw"],
                                  "nagios_pw": ee[e]["nagios_pw"],
                                  "neutron_db_pw": ee[e]["neutron_db_pw"],
                                  "neutron_ks_pw": ee[e]["neutron_ks_pw"],
                                  "neutron_metadata_pw": ee[e]["neutron_metadata_pw"],
                                  "nova_db_pw": ee[e]["nova_db_pw"],
                                  "nova_ks_pw": ee[e]["nova_ks_pw"],
                                  "swift_ks_pw": ee[e]["swift_ks_pw"],
                                  "swift_hash": sha_half(),
                                  "ntp_servers": ee[e]["ntp_servers"],
                                  "amqp_host": ee[e]["amqp_host"],
                                  "compute_hosts": ee[e]["compute_hosts"],
                                  "config_keystone_ldap_url": ee[e]["config_keystone_ldap_url"],
                                  "controller_host": ee[e]["controller_host"],
                                  "mariadb_host": ee[e]["mariadb_host"],
                                  "mongodb_host": ee[e]["mongodb_host"],
                                  "network_hosts": ee[e]["network_hosts"],
                                  "redis_host": ee[e]["redis_host"],
                                  "sahara_host": ee[e]["sahara_host"],
                                  "storage_host": ee[e]["storage_host"],
                                  "nova_network_fixedrange": ee[e]["nova_network_fixedrange"],
                                  "nova_network_floatrange": ee[e]["nova_network_floatrange"],
                                  "provision_demo_floatrange": ee[e]["provision_demo_floatrange"],
                                  "provision_tempest_floatrange": ee[e]["provision_tempest_floatrange"],
                                  "keystone_admin_email": ee[e]["keystone_admin_email"],
                                  "ssl_cert_subject_mail": ee[e]["ssl_cert_subject_mail"],
                                  "cinder_volumes_size": ee[e]["cinder_volumes_size"],
                                  "keystone_api_version": ee[e]["keystone_api_version"],
                                  "keystone_token_format": ee[e]["keystone_token_format"],
                                  "nova_network_pubif": ee[e]["nova_network_pubif"],
                                  "swift_storage_fstype": ee[e]["swift_storage_fstype"],
                                  "swift_storage_size": ee[e]["swift_storage_size"],
                                  "provision_image_url": ee[e]["provision_image_url"],
                                  "provision_uec_image_disk_url": ee[e]["provision_uec_image_disk_url"],
                                  "provision_uec_image_kernel_url": ee[e]["provision_uec_image_kernel_url"],
                                  "provision_uec_image_ramdisk_url": ee[e]["provision_uec_image_ramdisk_url"]}
        outobj["target"] = {"hosts": hosts}
        outobj["_meta"] = {"hostvars": hostvars}
        print(json.dumps(outobj))


if __name__ == "__main__":
    doit()
sys.exit(0)
