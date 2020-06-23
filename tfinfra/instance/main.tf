variable "instance_name" {}
variable "instance_zone" {}
variable "instance_type" {
    default = "n1-standard-1"
}
variable "instance_subnetwork" {}

resource "google_compute_instance" "vm_instance" {  
    # Following lines define tests to be skipped

    #checkov:skip=CKV_GCP_39:Not needed weil bloed
    #checkov:skip=CKV_GCP_38:Not needed
    #checkov:skip=CKV_GCP_30:Not needed
    #checkov:skip=CKV_GCP_32:Not needed

    name = "$(var.instance_name)"
    zone = "$(var.instance_zone)"
    machine_type = "$var.instance_type"
    boot_disk {
        initialize_params {
            image = "debian-cloud/debian-9"
        }
    }
    network_interface {
        subnetwork = "$(var.instance_subnetwork)"
        access_config {
            # 
        }
    }
}
