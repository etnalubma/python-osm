#
# Original version by Rory McCann (http://blog.technomancy.org/)
# Modifications by Christoph Lupprich (http://www.stopbeingcarbon.com)
#

class Node(object):
    ATTRIBUTES = ['id', 'timestamp', 'uid', 'user', 'visible', 'version', 'lat', 'lon', 'changeset']
    def __init__(self, attr, tags=None):
        self.id = int(attr['id'])
        self.lon, self.lat = attr['lon'], attr['lat']
        self.uid = int(attr.get('uid','-1'))
        self.user = attr.get('user','')
        self.version = int(attr.get('version','0'))
        self.timestamp = attr.get('timestamp','')
        self.visible = attr.get('visible','')
        self.changeset = attr.get('changeset','')
        if not tags:
            self.tags = {}
        else:
            self.tags = tags

    def __cmp__(self, other):
        cmp_ref = cmp(self.tags.get('ref',''), other.tags.get('ref',''))
        if cmp_ref:
            return cmp_ref
        cmp_name = cmp(self.tags.get('name',''), other.tags.get('name',''))
        if cmp_name:
            return cmp_name
        return cmp(self.id, other.id)

    def attributes(self):
        d = dict([(k,getattr(self,k)) for k in self.ATTRIBUTES])
        for k,v in d.items():
            if type(v) == int:
                d[k] = str(v)
        return d

    def __repr__(self):
        return "Node(attr=%r, tags=%r)" % (self.attributes(), self.tags)

class Way(object):
    ATTRIBUTES = ['id', 'timestamp', 'uid', 'user', 'visible', 'version', 'changeset']
    def __init__(self, attr, nodes=None, tags=None):
        self.id = int(attr['id'])
        self.uid = int(attr.get('uid','-1'))
        self.user = attr.get('user','')
        self.version = int(attr.get('version','0'))
        self.timestamp = attr.get('timestamp','')
        self.visible = attr.get('visible','')
        self.changeset = attr.get('changeset','')

        if not nodes:
            self.nodes = []
        else:
            self.nodes = nodes
        if not tags:
            self.tags = {}
        else:
            self.tags = tags

    def __cmp__(self, other):
        cmp_ref = cmp(self.tags.get('ref',''), other.tags.get('ref',''))
        if cmp_ref:
            return cmp_ref
        cmp_name = cmp(self.tags.get('name',''), other.tags.get('name',''))
        if cmp_name:
            return cmp_name
        return cmp(self.id, other.id)

    def attributes(self):
        d = dict([(k,getattr(self,k)) for k in self.ATTRIBUTES])
        for k,v in d.items():
            if type(v) == int:
                d[k] = str(v)
        return d

    def __repr__(self):
        return "Way(attr=%r, nodes=%r, tags=%r)" % (self.attributes(), self.nodes, self.tags)

class Relation(object):
    ATTRIBUTES = ['id', 'timestamp', 'uid', 'user', 'visible', 'version', 'changeset']
    def __init__(self, attr, members=None, tags=None):
        self.id = int(attr['id'])
        self.uid = int(attr.get('uid','-1'))
        self.user = attr.get('user','')
        self.version = int(attr.get('version','0'))
        self.timestamp = attr.get('timestamp','')
        self.visible = attr.get('visible','')
        self.changeset = attr.get('changeset','')

        if not members:
            self.members = []
        else:
            self.members = members
        if not tags:
            self.tags = {}
        else:
            self.tags = tags
      
    def __cmp__(self, other):
        cmp_ref = cmp(self.tags.get('ref',''), other.tags.get('ref',''))
        if cmp_ref:
            return cmp_ref
        cmp_name = cmp(self.tags.get('name',''), other.tags.get('name',''))
        if cmp_name:
            return cmp_name
        return cmp(self.id, other.id)

    def attributes(self):
        d = dict([(k,getattr(self,k)) for k in self.ATTRIBUTES])
        for k,v in d.items():
            if type(v) == int:
                d[k] = str(v)
        return d

    def __repr__(self):
        return "Relation(attr=%r, members=%r, tags=%r)" % (self.attributes(), self.members, self.tags)

class ObjectPlaceHolder(object):
    def __init__(self, id, type=None, role=''):
        self.id = int(id)
        self.type = type
        self.role = role

        self.tags = {}
        self.nodes = []
        self.members =[]

    def __repr__(self):
        return "ObjectPlaceHolder(id=%r, type=%r, role=%r)" % (self.id, self.type, self.role)

