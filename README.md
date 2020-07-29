This repo will allow you to create a demo Kubernetes cluster with nginx reverse proxy and 3 instances of simple Python app behind it. Tested on OSX with Docker Desktop (2.3.0)

# Installation

1. Install Docker Desktop and enable Kubernetes
2. Clone the repo:

    ```git clone https://github.com/sshmanko/bpower; cd bpower```

3. Build application docker image locally (to avoid uploading it to dockerhub):

    ```docker build --tag bpower/app:latest .```

4.  Install ingress-nginx ([official guide](https://kubernetes.github.io/ingress-nginx/deploy/)):

    ```kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v0.34.1/deploy/static/provider/cloud/deploy.yaml```

    Verify nginx deployment is finished (Completed/Running):
     `kubectl get all -n ingress-nginx`

5. Apply Kubernetes configuration (deployment, service, ingress-nginx rules):

    ```kubectl apply -f resources```

6. Application should be available at http://localhost/

