class Column(object):
    """
        Элемент конфигурации
    """
    def __init__(self, *args, **kwargs):

        hid = False
        filters = []
        sorters = []

        if len(args) == 3:
            inner_name, verbose_name, width = args
        elif len(args) == 2:
            inner_name, verbose_name = args
            width = 20
        elif len(args) == 4:
            inner_name, verbose_name, width, hid = args
        elif len(args) == 5:
            inner_name, verbose_name, width, hid, filters = args
        elif len(args) == 6:
            inner_name, verbose_name, width, hid, filters, sorters = args
	elif len(args) == 2:
            inner_name, verbose_name = args
            width = 20
        elif len(args) == 4:
            inner_name, verbose_name, width, hid = args
        elif len(args) == 5:
            inner_name, verbose_name, width, hid, filters = args
        elif len(args) == 6:
            inner_name, verbose_name, width, hid, filters, sorters = args

        special_attrs = ['locked', 'editable']

        self.code = inner_name
        self.name = verbose_name
        self.width = width
        self.hidden = hid
        self.idx = 0
        if sorters:
            sorters.column = self
        if filters:
            filters.column = self
            filters.code = self.code

        #здесь хранятся экземпляры фильтров для колонок
        self.filters = filters
        #здесь хранятся экземпляры сортировщиков для колонок
        self.sorters = sorters

    def get_config(self):
        ''' ?
        '''
        config = dict()
        config['data_index'] = self.code
        config['header'] = self.name
        config['width'] = self.width
        config['hidden'] = self.hidden

        return config
