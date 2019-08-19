# -*- mode: ruby -*-
# vi: set ft=ruby :

$mach_quant = 3

Vagrant.configure("2") do |config|
 
  config.vm.provider "virtualbox" do |vb|
      vb.gui = false
      vb.memory=512
      vb.cpus=1
      vb.check_guest_additions=false
  config.vm.box_check_update=false
  config.vm.box="ubuntu/xenial64"
  config.vm.provision "shell" do |s|
    ssh_pub_key = File.readlines("/var/root/.ssh/id_rsa.pub").first.strip
    s.inline = <<-SHELL
      echo #{ssh_pub_key} >> /home/vagrant/.ssh/authorized_keys
      echo #{ssh_pub_key} >> /root/.ssh/authorized_keys
    SHELL
  end

 end

(1..$mach_quant).each do |i|
    config.vm.define "node#{i}" do |node|
        node.vm.network "public_network", ip: "192.168.1.#{17+i}"
        node.vm.hostname = "node#{i}"
    end
end
  
end