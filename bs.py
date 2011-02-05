import boto

class BS(dict):

    def __init__(self, access_key=None, secret_key=None):
        dict.__init__(self)
        self._ec2 = boto.connect_ec2(access_key, secret_key)

    def load(self):
        rs = self._ec2.get_all_instances()
        l = []
        for r in rs:
            for i in r.instances:
                i.groups = r.groups
                l.append(i)
        self['regions'] = self._ec2.get_all_regions()
        self['instances'] = l
        self['volumes'] = self._ec2.get_all_volumes()
        self['eips'] = self._ec2.get_all_addresses()
        self['groups'] = self._ec2.get_all_security_groups()
        self['keypairs'] = self._ec2.get_all_key_pairs()
        self['zones'] = self._ec2.get_all_zones()

    def find(self, s):
        if hasattr(s, 'id'):
            s = s.id
        print 'looking for %s' % s
        results = set()
        for key in self:
            for item in self[key]:
                for attr in item.__dict__:
                    val = item.__dict__[attr]
                    if isinstance(val, (str, unicode)):
                        if val.find(s) >= 0:
                            results.add(item)
        return results
        
        
