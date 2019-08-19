# iq-option

Предполагается, что запуск будет производиться с машины под Ubuntu/root, где стоит Ansible 2.7+, Vagrantи Virtualbox.
Перед запуском Vagrantfile поменять IP на свою подсеть
Vagrant пробрасывает ключи на root гостевой машины

# Запуск Playbook

ansible-playbook main.yml

# Ad-hoc

Копируем jpg

ansible iq-option -m copy -a "src='test (1).jpg' dest=/opt/"

Привязываем альясы

ansible iq-option -m shell -a "/opt/mc config host add  minio1 http://192.168.1.18:9000  ASDsdadsafasfasfRFSAFS sdadsasdasfFGASFASFVvac"
ansible iq-option -m shell -a "/opt/mc config host add  minio2 http://192.168.1.19:9000  ASDsdadsafasfasfRFSAFS sdadsasdasfFGASFASFVvac"
ansible iq-option -m shell -a "/opt/mc config host add  minio3 http://192.168.1.20:9000  ASDsdadsafasfasfRFSAFS sdadsasdasfFGASFASFVvac"
Создаем пользователя ( реплицируется)
ansible iq-option -m shell -a "/opt/mc admin user add minio1 123 12345678" 
Назначаем права
ansible iq-option -m shell -a "/opt/mc admin policy set minio1 readwrite user=123"
Создаем bucket
ansible iq-option -m shell -a "/opt/mc mb minio1/bucket"

заливаем файл
ansible iq-option -m shell -a"/opt/mc cp /opt/test\ \(1\).jpg minio1/bucket"

#
Выкачиваем файл:
python script.py
