import os


from reader.compress import bpzip, gpzip

extension map = {
    'bz2': bpzip.opener,
    'gz': gpzip.opener,
}



class Reader:
    def __init__(self, filename):
        extension = os.path.splitext(filename)[1]
        opener = extension.map.get (extension, open)
        self.f = opener(filename, "rt")

    def close(self):
        self.f.close()


    def read(self):
       return self.f.read()



def  main():

    pass


if __name__ == '__main__':
    main()
    exit(0)