
import os

secret_keys = {
    "tfvar_vsphere_pwd01": os.environ['VSPHERE_PWD_FRM_SECRET01'],
    "tfvar_vsphere_pwd02": os.environ['VSPHERE_PWD_FRM_SECRET02'],
    "tfvar_vsphere_pwd03": os.environ['VSPHERE_PWD_FRM_SECRET03']
}

print(secret_keys)


