from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import Host
from mininet.node import OVSKernelSwitch
from mininet.node import Controller, RemoteController, OVSController
from mininet.cli import CLI
from mininet.link import TCLink, Intf
from mininet.log import setLogLevel, info
import timeit
import time

class MyTopo( Topo ):


    def build( self ):
        h1 = self.addHost( 'h1', ip='10.0.0.21', mac='00:00:00:00:00:11')
        h2 = self.addHost( 'h2',ip='10.0.0.22', mac='00:00:00:00:00:12' )
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        s4 = self.addSwitch( 's4' )
        s5 = self.addSwitch( 's5' )
        s6 = self.addSwitch( 's6' )
        s7 = self.addSwitch( 's7' )
        s8 = self.addSwitch( 's8' )
        s9 = self.addSwitch( 's9' )
        s10 = self.addSwitch( 's10' )

        # Add links
        self.addLink( h1, s1 )
        self.addLink( h2, s5 )
        self.addLink( s1, s7, bw=10 )
        self.addLink( s1, s2, bw=1000)
        self.addLink( s1, s8, bw=1.544 )
        self.addLink( s2, s7, bw=1.544 )
        self.addLink( s2, s3, bw=1000 )
        self.addLink( s2, s6, bw=1.544 )
        self.addLink( s3, s4, bw=10 )
        self.addLink( s3, s5, bw=10 )
        self.addLink( s4, s5, bw=1.544 )
        self.addLink( s4, s6, bw=1000 )
        self.addLink( s5, s10, bw=1000 )
        self.addLink( s6, s10, bw=1.544 )
        self.addLink( s6, s7, bw=10 )
        self.addLink( s7, s8, bw=1.544 )
        self.addLink( s7, s9, bw=10 )
        self.addLink( s8, s9, bw=1.544 )


def topo1():
    info("Topology Python Script...\n")
    net = Mininet(topo=MyTopo(), build=False, ipBase='1024.0.0.0/8', link=TCLink)
    info("Adding the RemoteController\n")
    c0 = net.addController('c0',ip='127.0.0.1',protocol='tcp',controller=RemoteController, port = 6653)

    net.start()
    info('*** Starting Network\n')

    sta=timeit.default_timer()
    while(net.pingAll()>0.0):
    	print(net.pingAll())
    sto = timeit.default_timer() - sta

    print "convergence time: ", sto
    CLI(net)


if __name__ == '__main__':
	setLogLevel('info')
	topo1()
