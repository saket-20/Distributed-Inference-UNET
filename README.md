# Distributed-Inference-UNET

An application that performs semantic segmentation on images in  
a folder using UNET. Multiple images are sent in parallel to a
server and then using a load balancer the images are sent to
different docker containers for processing. Load balancing is done using NGINX. 
