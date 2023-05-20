FROM nginx
COPY nginx_gen.py .
RUN apt-get update && apt-get install -y python3
ENTRYPOINT python3 nginx_gen.py && nginx -g 'daemon off;'