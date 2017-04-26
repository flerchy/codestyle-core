import logging
logging.basicConfig(level=logging.DEBUG)


class Category(object):

    """docstring for Category"""
    logging.debug("***************************Category*****************************")

    def __init__(self, arg):
        super(Category, self).__init__()
        self.arg = arg
        self.name = "test name"

    def __str__(self):
        logging.debug("***************************Category*****************************")
        return self.name


if __name__ == '__main__':
    c = Category('a')
    logging.debug("Category is '{0}'".format(c))
