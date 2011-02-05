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
from optparse import OptionParser

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
        (self.options, self.args) = self.parser.parse_args()
        if self.options.aws_access_key_id:
            boto.config.set('Credentials', 'aws_access_key_id',
                            self.options.aws_access_key_id)
            boto.config.set('DB', 'db_user', self.options.aws_access_key_id)
        if self.options.aws_secret_access_key:
            boto.config.set('Credentials', 'aws_secret_access_key',
                            self.options.aws_secret_access_key)
            boto.config.set('DB', 'db_passwd', self.options.aws_secret_access_key)
        if self.options.domain_name:
            boto.config.set('DB', 'db_name', self.options.domain_name)
    
