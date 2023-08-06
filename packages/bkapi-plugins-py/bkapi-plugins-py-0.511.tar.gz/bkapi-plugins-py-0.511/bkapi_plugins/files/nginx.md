
一、前言
为了满足不同需求和应用场景，Nginx提供了大量的第三方模块和插件，这些插件可以通过编译安装的方式进行添加和启用。

编译安装Nginx可以让管理员根据自己的需要选择特定的配置选项和第三方模块，从而实现更加精细化的服务器配置和优化。此外，编译安装还可以对Nginx进行自定义编译，以适配不同的操作系统和环境，提升服务器的性能和稳定性。

总之，通过编译安装Nginx可以获得更加灵活和高效的服务器配置，同时也能够满足不同应用场景的需求。下面将介绍nginx 的生产编译安装流程。



二、安装准备
配置squid代理后安装apt包

yum update -y
yum install -y libpcre3 libpcre3-dev openssl zlib1g-dev libssl-dev gcc make libxml2 libxslt1.1 libxslt1-dev libgeoip-dev libgd-dev

# 安装nginx，这样会有默认的目录和配置等，后面步骤主要是编译替换nginx二进制文件和配置文件
apt-get install nginx -y
源码包下载解压
wget https://nginx.org/download/nginx-1.20.1.tar.gz
tar xvzf nginx-1.20.1.tar.gz
二、编译nginx及自带模块
cd nginx-1.20.1;
./configure --with-cc-opt='-g -O2 -fstack-protector-strong -Wformat -Werror=format-security -fPIC -Wdate-time -D_FORTIFY_SOURCE=2' --with-ld-opt='-Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-z,now -fPIC' --prefix=/usr/share/nginx --conf-path=/etc/nginx/nginx.conf --http-log-path=/var/log/nginx/access.log --error-log-path=/var/log/nginx/error.log --lock-path=/var/lock/nginx.lock --pid-path=/run/nginx.pid --modules-path=/usr/lib/nginx/modules --http-client-body-temp-path=/var/lib/nginx/body --http-fastcgi-temp-path=/var/lib/nginx/fastcgi --http-proxy-temp-path=/var/lib/nginx/proxy --http-scgi-temp-path=/var/lib/nginx/scgi --http-uwsgi-temp-path=/var/lib/nginx/uwsgi --with-compat --with-debug --with-pcre-jit --with-http_ssl_module --with-http_stub_status_module --with-http_realip_module --with-http_auth_request_module --with-http_v2_module --with-http_dav_module --with-http_slice_module --with-threads --with-http_addition_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_sub_module --with-http_image_filter_module=dynamic --with-http_xslt_module=dynamic --with-mail=dynamic --with-stream=dynamic --with-stream_geoip_module=dynamic

make && make install
mv /usr/sbin/nginx /usr/sbin/nginx.old
cp objs/nginx /usr/sbin/nginx
mkdir /usr/share/nginx/modules/
cp objs/*.so /usr/share/nginx/modules/

三、编译nginx第三方模块-aws鉴权模块
AWS 鉴权模块是一个 Nginx 第三方模块，用于在 Nginx 服务器中实现 AWS 认证和访问控制。它允许您使用 AWS 凭证对请求进行签名，并根据您的 AWS 资源策略来限制对这些资源的访问。

具体来说，AWS 鉴权模块可以帮助您实现以下功能：

对请求进行签名：使用 Access Key 和 Secret Key 对请求进行签名，以验证请求者的身份。
签名版本支持：支持 AWS Signature Version 4 签名算法，是目前 AWS 所推荐的签名方式。
请求处理：对经过签名认证的请求进行处理，包括验证时间戳、计算签名等。
访问控制：根据您的 AWS 资源策略（policy）来限制对特定资源的访问，从而保护您的数据安全。
缓存支持：可配置缓存来提高性能，避免频繁地向 AWS 服务发送请求。
总之，AWS 鉴权模块可以帮助您在 Nginx 服务器中实现 AWS 认证和访问控制，保护您的数据安全，同时提高性能和效率。

cd nginx-1.20.1
git clone https://github.com/anomalizer/ngx_aws_auth.git -b AuthV2
./configure --with-compat --add-dynamic-module=ngx_aws_auth && make modules
cp objs/ngx_http_aws_auth_module.so /usr/share/nginx/modules/
四、编译nginx第三方模块-nginx exporter
promethues监控nginx可选两个exporter，通过nginx_exporter主要是获取nginx-status中的内建的指标，nginx自身提供status信息，较为简单，promethues中对应的metrics也较少，想要监控更多的指标可以通过nginx-vts-exporter采集信息，依赖在编译nginx的时候添加nginx-module-vts模块来实现。

nginx virtual host traffic status模块是nginx第三方模块之一，vts提供了访问虚拟主机状态的信息，包含server，upstream以及cache的当前状态，类似于NGINX Plus 提供的在线活动监控功能。

cd nginx-1.20.1
git clone -b v0.1.18 https://github.com/vozlt/nginx-module-vts
wget https://github.com/hnlq715/nginx-vts-exporter/releases/download/v0.10.3/nginx-vts-exporter-0.10.3.linux-amd64.tar.gz
tar -zxvf nginx-vts-exporter-0.10.3.linux-amd64.tar.gz
mv nginx-vts-exporter-0.10.3.linux-amd64/nginx-vts-exporter /usr/local/bin/nginx-vts-exporter
./configure --with-compat --add-dynamic-module=nginx-module-vts  && make modules
cp objs/ngx_http_vhost_traffic_status_module.so /usr/share/nginx/modules

五、增加nginx配置
在/etc/nginx/conf.d/下新增如下配置 stats.conf

cat > /etc/nginx/conf.d/stats.conf << EOF
server {
   server_name 127.0.0.1;
   location /status {
       allow 127.0.0.1;
       deny all;
       vhost_traffic_status_display;
       vhost_traffic_status_display_format json;
   }
}
EOF
六、增加vts-exporter启动配置
cat > /usr/lib/systemd/system/vts-exporter.service << EOF
[Unit]
Description=vts-exporter
After=network-online.target
[Service]
Type=simple
ExecStart=/usr/local/bin/nginx-vts-exporter -nginx.scrape_uri=http://127.0.0.1/status/format/json
Restart=always
RestartSec=10
ExecStop=/bin/kill -9 $MAINPID
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=vts-exporter
[Install]
WantedBy=multi-user.target
EOF
设置开机启动
systemctl start vts-exporter.service && systemctl enable vts-exporter.service && systemctl status vts-exporter.service
nginx module配置
#nginx module-enable 配置初始化
mkdir /etc/nginx/modules-enabled
cd /etc/nginx/modules-enabled
echo "load_module modules/ngx_http_aws_auth_module.so;" > 50-mod-http_aws_auth.conf
echo "load_module modules/ngx_http_image_filter_module.so;" > 50-mod-http-image-filter.conf
echo "load_module modules/ngx_http_xslt_filter_module.so;" > 50-mod-http-xslt-filter.conf
echo "load_module modules/ngx_mail_module.so;" > 50-mod-mail.conf
echo "load_module modules/ngx_stream_module.so;" > 50-mod-stream.conf
echo "load_module modules/ngx_stream_geoip_module.so;" > 70-mod-stream-geoip.conf
echo "load_module modules/ngx_http_vhost_traffic_status_module.so;" > module-vts.conf
nginx 主配置文件参考配置
vim /etc/nginx/nginx.conf
user www-data;
worker_processes 56; #进程数不要用auto，和CPU数匹配
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf; #动态模块加载

events {
 worker_connections 102400;  # 单个工作进程可以允许同时建立外部连接的数量
 # multi_accept on;
}

http {
    vhost_traffic_status_zone;  # vts 数据采集模块
    gzip                on;  # 打开gizp压缩
    gzip_disable        "MSIE [1-6]\.(?!.*SV1)";
    gzip_proxied        any;
    gzip_buffers        16 8k;
    gzip_types          text/plain application/javascript application/x-javascript text/javascript text/xml text/css;
    gzip_vary           on;

    server_tokens       off;  # returns "Server: nginx"  # 隐藏nginx版本信息

    include mime.types;
    proxy_set_header X-Real-IP $remote_addr;  # 将$remote_addr的值放进变量X-Real-IP中
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header Host $http_host;
    # 增加http头部信息
    add_header X-Frame-Options SAMEORIGIN;
    add_header X-Content-Type-Options "nosniff";
    add_header X-XSS-Protection "1; mode=block";
    real_ip_recursive on;

    # 保存server_names相关的hash表
    server_names_hash_bucket_size  128;
    server_names_hash_max_size     2048;

    # 保存proxy_headers相关的hash表
    proxy_headers_hash_bucket_size 256;
    proxy_headers_hash_max_size    2048;

    # 保存variables的hash表
    variables_hash_bucket_size     128;
    variables_hash_max_size        2048;
        log_format time_detail '$http_x_forwarded_for[$remote_addr][$host] - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent $request_length "$http_referer" '
                    '"$http_user_agent" "$http_x_forwarded_for"'
                    '$connection $upstream_addr '
                    'upstream_response_time $upstream_response_time request_time $request_time upstream_connect_time'
                    '$upstream_connect_time upstream_header_time $upstream_header_time ';
        log_format main '$remote_addr[$host] - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" '
                    '"$http_user_agent" "$http_x_forwarded_for"'
                    '$connection $upstream_addr '
                    'upstream_response_time $upstream_response_time request_time $request_time ';

 include /etc/nginx/conf.d/*.conf;
}

stream{
  include /etc/nginx/streams/*.conf;
}
nginx 启动配置
前提步骤安装了nginx会默认设置开机启动步骤，可以不设置配置，但是需要restart nginx，因为替换了nginx 二进制文件和nginx配置

创建目录
mkdir -p /var/lib/nginx/body

七、添加nginx systemctl管理
cat > /usr/lib/systemd/system/nginx.service << EOF
[Unit]
Description=A high performance web server and a reverse proxy server
Documentation=man:nginx(8)
After=network.target nss-lookup.target

[Service]
Type=forking
PIDFile=/run/nginx.pid
ExecStartPre=/usr/sbin/nginx -t -q -g 'daemon on; master_process on;'
ExecStart=/usr/sbin/nginx -g 'daemon on; master_process on;'
ExecReload=/usr/sbin/nginx -g 'daemon on; master_process on;' -s reload
ExecStop=-/sbin/start-stop-daemon --quiet --stop --retry QUIT/5 --pidfile /run/nginx.pid
TimeoutStopSec=5
KillMode=mixed

[Install]
WantedBy=multi-user.target
EOF
设置开机启动和restart nginx
systemctl daemon-reload && systemctl enable nginx.service  && systemctl restart nginx.service && systemctl status nginx.service
nginx 后端配置server.conf模版
server {
    listen              80;
    server_name         <server_name>;
    location /{
        return 307 https://<server_name>$request_uri;
    }
}
server {
    #开始 http2的支持
    listen              443 ssl http2;
    server_name         <server_name>;
    keepalive_timeout   70;

    access_log /var/log/nginx/<server_name>.access.log main buffer=16k flush=1s;
    error_log /var/log/nginx/<server_name>.error.log;
    ssl_certificate     /etc/nginx/certs/<server_name>/ssl.chain.crt;
    ssl_certificate_key /etc/nginx/certs/<server_name>/server.key;
    #配置 tls 协议支持
    ssl_protocols       TLSv1.2 TLSv1.3;
    ssl_ciphers         HIGH:!aNULL:!MD5;


    location / {
        proxy_set_header Host $host;
        #配置 x-forward-for
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header   X-Real-IP          $remote_addr;
        proxy_http_version 1.1;
        proxy_set_header Connection "";
        proxy_pass http://ingress;
    }
}