from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories


class DemoCustomCheck(BaseResourceCheck):
    def __init__(self):
        name = "Ensure VM instance is not tagged 'foo'"
        id = "CKV_GCP_101"
        supported_resources = ['google_compute_instance']
        # CheckCategories are defined in models/enums.py
        categories = [CheckCategories.CONVENTION]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        """
            Looks for ...:
            https://www.terraform.io/docs/providers/google/r/compute_instance.html
        :param conf: google_compute_instance configuration
        :return: <CheckResult>
        """
        if 'tags' in conf.keys():
            if any("foo" in sublist for sublist in conf['tags']):
                return CheckResult.FAILED
        return CheckResult.PASSED


scanner = DemoCustomCheck()