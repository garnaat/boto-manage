#!/usr/bin/env python
# Copyright (c) 2009 Mitch Garnaat http://garnaat.org/
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
import boto
import sys
from optparse import OptionParser
from boto.manage.server import Server

class BotoManageCommand(object):

    Usage = '%prog [options]\n'
    
    def __init__(self):
        self.parser = OptionParser(usage=self.Usage)
        self.parser.add_option('-a', '--access_key', dest='aws_access_key_id',
                               default=None, help="AWS Access Key ID")
        self.parser.add_option('-s', '--secret_key', dest='aws_secret_access_key',
                               default=None, help='AWS Secret Access Key')
        self.parser.add_option('-d', '--domain', dest='domain_name',
                               default='manage', help='SimpleDB domain name')

    def main(self):
        (self.options, self.args) = parser.parse_args()

    
class RegisterServers(BotoManageCommand):
    """
    Find all EC2 instances that are not currently registered in SimpleDB
    and register them.
    """

    def main(self):
        BotoManageCommand.main()
        ec2 = boto.connect_ec2()
        for r in ec2.get_all_instances():
            for i in r.instances:
                try:
                    s = Server.find(instance_id=i.id).next()
                except StopIteration:
                    print "Instance: [%s] %s Has no server object!" % (i.id, i.public_dns_name)
                    print "Group: %s" % (r.groups[0].id)
                    print "Please enter information for this server"
                    name = raw_input("Name: ")
                    description = raw_input("Description: ")
                    s = Server.create_from_instance_id(i.id, name=name, description=description)

if __name__ == "__main__":
    sys.path.append('.')
    command = RegisterServers()
    command.main()
