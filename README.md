# Cloud cover Segmemntation on Kubernetes


This Project sets up a scalable and testable ML kubernetes service based environment:

The web service was created with flask using the code  


The app gets an image (sat file) sent to it and 

The sat file was extracted for testing as seen below:

```

    wget https://20tree-public.s3-eu-west-1.amazonaws.com/candidates/cloudmask/Sentinel2L2A_sen2cor_18TUR_20180812_clouds%3D5.3%25_area%3D99%25.tif

```

And then it was cropped to ```512 x 512``` patch as input is initially a full satellite tile which is very large to passed into the server.



The idea is that data-science workflow is structured and compiled into python libraries and the satellite data ingestion is achieved by containerization

terraform code has been employed to:
- manage the infrastructure of the code,
- fascilitating the testing 
- maintenance, and 
- making any need for migration easier.



An endpoint has been exposed to fascilitate running utils.infer_image()
- image_path is the argument of interest and 
- as the satellite image is too large to be sent, it is cropped to a ```512 x 512``` patch.


jupyter notebook in https://github.com/Funsho-Agboola/K8s-ML-Flask-Web-App/blob/main/code.ipynb was run aside to ensure keeping track of the bit-by-bit outputs and the codes.




## Containerization


The service is then containerized 

- A docker file provided for the service, exposing its port as seen in https://github.com/Funsho-Agboola/K8s-ML-Flask-Web-App/blob/main/Dockerfile



Github actions is implelmented to push the docker images automatically deployed as seen in https://github.com/Funsho-Agboola/K8s-ML-Flask-Web-App/actions

- The action builds a new image immediately a change is made and pushed to the main branch,
- The it logs in to docker and pushes the newly built image




## Multi-Node Cluster setup

The terraform code in https://github.com/Funsho-Agboola/K8s-ML-Flask-Web-App/blob/main/Infra_tf/ contains the infrastructure used in setting up the GKE multi-node cluster



For the endpoint, the full numpy array result as observed on postman is displayed in the image below



![alt text](https://github.com/Funsho-Agboola/K8s-ML-Flask-Web-App/blob/main/API-endpoint-response.png?raw=true)
