#file which generates the nginx.conf dynamically based on the environment variable 'SCALE'
import os
n = int(os.environ['SCALE'])
print("N=",end="")
print(n)
with open('/etc/nginx/conf.d/default.conf', 'w') as f:
    f.write('upstream loadbalancer {\n')
    for i in range(1, n+1):
        f.write(f'    server unet_proj-app1-{i}:5000;\n')
    f.write('}\n\n')
    f.write('server {\n')
    f.write('    location / {\n')
    f.write('        proxy_pass http://loadbalancer;\n')
    f.write('    }\n')
    f.write('}\n')