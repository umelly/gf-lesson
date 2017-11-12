一次HTTP请求的过程
===
> 以mac/centos为例

1. 访问一个域名 a.com
2. 首先读取系统hosts对应的ip地址 /etc/hosts
3. 查询dns服务器(/etc/resolv.conf), 找到域名和IP的对应关系
  - DNS解析(dnspod.com，各大域名商都会有dns解析系统)
4. 找到服务器IP后, web服务器(nginx)解析域名与应用通讯的对应管理
5. 应用根据uri和请求的数据(get,post数据)处理数据响应，并返回内容
