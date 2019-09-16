gcc sniff-pcap.c -o sniffer -lpcap
sudo ./sniffer "$1"
