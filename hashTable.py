#Anant Jawanda
#lab05

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.loadSize = 0

# ----------------------------------------------------------- #
    def put(self,key,data):
      
      stoppingFactor = 0.5          #predetermined value when to resize hash
      hashvalue = self.hashfunction(key,len(self.slots))
      loadingFactor = self.loadSize / self.size

      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
        self.loadSize += 1
        
      else:
            if self.slots[hashvalue] == key:
                  self.data[hashvalue] = data  #replace
                  self.loadSize += 1
      
      
            
            if self.slots[hashvalue] == key:
              self.data[hashvalue] = data  #replace
              self.loadSize += 1
            else:
              nextslot = self.rehash(hashvalue,len(self.slots))
              while self.slots[nextslot] != None and \
                              self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot,len(self.slots))
                self.loadSize += 1

              if self.slots[nextslot] == None:
                
                self.slots[nextslot]=key
                self.data[nextslot]=data
                self.loadSize += 1
                
              if loadingFactor >= stoppingFactor:
                self.slots += [None]
                self.data += [None]
            
              else:
                self.data[nextslot] = data #replace
       # print(loadingFactor)

      
# ----------------------------------------------------------- #

    def hashfunction(self,key,size):
         return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
      startslot = self.hashfunction(key,len(self.slots))

      data = None
      stop = False
      found = False
      position = startslot
      while self.slots[position] != None and  \
                           not found and not stop:
         if self.slots[position] == key:
           found = True
           data = self.data[position]
         else:
           position=self.rehash(position,len(self.slots))
           if position == startslot:
               stop = True
      return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)


H=HashTable()
H.put(11, "cat")
H.put(26, "dog")
H.put(93, "lion")
H.put(22, "tiger")

