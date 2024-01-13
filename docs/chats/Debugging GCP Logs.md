gcloud compute instances create-with-container skelly-bot-testing \
    --project=mocap-test-project \
    --zone=us-central1-a \
    --machine-type=e2-micro \
    --network-interface=network-tier=PREMIUM,stack-type=IPV4_ONLY,subnet=default \
    --maintenance-policy=MIGRATE \
    --provisioning-model=STANDARD \
    --service-account=nest-bot@mocap-test-project.iam.gserviceaccount.com \
    --scopes=https://www.googleapis.com/auth/cloud-platform \
    --tags=http-server,https-server \
    --image=projects/cos-cloud/global/images/cos-stable-109-17800-66-57 \
    --boot-disk-size=10GB \
    --boot-disk-type=pd-standard \
    --boot-disk-device-name=skelly-bot-testing \
    --container-image=us-east1-docker.pkg.dev/mocap-test-project/jonbot/nestbot \
    --container-restart-policy=always \
    --container-env=NODE_ENV=production \
    --no-shielded-secure-boot \
    --shielded-vtpm \
    --shielded-integrity-monitoring \
    --labels=goog-ec-src=vm_add-gcloud,container-vm=cos-stable-109-17800-66-57



TERRAFORM

# This code is compatible with Terraform 4.25.0 and versions that are backwards compatible to 4.25.0.
# For information about validating this Terraform code, see https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/google-cloud-platform-build#format-and-validate-the-configuration

resource "google_compute_instance" "skelly-bot-testing" {
  boot_disk {
    auto_delete = true
    device_name = "skelly-bot-testing"

    initialize_params {
      image = "projects/cos-cloud/global/images/cos-stable-109-17800-66-57"
      size  = 10
      type  = "pd-standard"
    }

    mode = "READ_WRITE"
  }

  can_ip_forward      = false
  deletion_protection = false
  enable_display      = false

  labels = {
    container-vm = "cos-stable-109-17800-66-57"
    goog-ec-src  = "vm_add-tf"
  }

  machine_type = "e2-micro"

  metadata = {
    gce-container-declaration = "spec:\n  containers:\n  - name: skelly-bot-testing\n    image: us-east1-docker.pkg.dev/mocap-test-project/jonbot/nestbot\n    env:\n    - name: NODE_ENV\n      value: production\n    stdin: false\n    tty: false\n  restartPolicy: Always\n# This container declaration format is not public API and may change without notice. Please\n# use gcloud command-line tool or Google Cloud Console to run Containers on Google Compute Engine."
  }

  name = "skelly-bot-testing"

  network_interface {
    access_config {
      network_tier = "PREMIUM"
    }

    queue_count = 0
    stack_type  = "IPV4_ONLY"
    subnetwork  = "projects/mocap-test-project/regions/us-central1/subnetworks/default"
  }

  scheduling {
    automatic_restart   = true
    on_host_maintenance = "MIGRATE"
    preemptible         = false
    provisioning_model  = "STANDARD"
  }

  service_account {
    email  = "nest-bot@mocap-test-project.iam.gserviceaccount.com"
    scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }

  shielded_instance_config {
    enable_integrity_monitoring = true
    enable_secure_boot          = false
    enable_vtpm                 = true
  }

  tags = ["http-server", "https-server"]
  zone = "us-central1-a"
}

