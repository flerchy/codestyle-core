def _make_parser_function(name, sep=','):

    def parser_f(filepath_or_buffer,
                 sep=sep,
                 dialect=None,
                 compression=None,

                 doublequote=True,
                 escapechar=None,
                 quotechar='"',
                 quoting=csv.QUOTE_MINIMAL,
                 skipinitialspace=False,
                 lineterminator=None,

                 header='infer',
                 index_col=None,
                 names=None,
                 prefix=None,
                 skiprows=None,
                 skipfooter=None,
                 skip_footer=0,
                 na_values=None,
                 na_fvalues=None,
                 true_values=None,
                 false_values=None,
                 delimiter=None,
                 converters=None,
                 dtype=None,
                 usecols=None,

                 engine='c',
                 delim_whitespace=False,
                 as_recarray=False,
                 na_filter=True,
                 compact_ints=False,
                 use_unsigned=False,
                 low_memory=_c_parser_defaults['low_memory'],
                 buffer_lines=None,
                 warn_bad_lines=True,
                 error_bad_lines=True,

                 keep_default_na=True,
                 thousands=None,
                 comment=None,
                 decimal=b'.',

                 parse_dates=False,
                 keep_date_col=False,
                 dayfirst=False,
                 date_parser=None,

                 memory_map=False,
                 nrows=None,
                 iterator=False,
                 chunksize=None,

                 verbose=False,
                 encoding=None,
                 squeeze=False,
                 mangle_dupe_cols=True,
                 tupleize_cols=True,
                 ):

        # Alias sep -> delimiter.
        if delimiter is None:
            delimiter = sep

        kwds = dict(delimiter=delimiter,
                    engine=engine,
                    dialect=dialect,
                    compression=compression,

                    doublequote=doublequote,
                    escapechar=escapechar,
                    quotechar=quotechar,
                    quoting=quoting,
                    skipinitialspace=skipinitialspace,
                    lineterminator=lineterminator,

                    header=header,
                    index_col=index_col,
                    names=names,
                    prefix=prefix,
                    skiprows=skiprows,
                    na_values=na_values,
                    na_fvalues=na_fvalues,
                    true_values=true_values,
                    false_values=false_values,
                    keep_default_na=keep_default_na,
                    thousands=thousands,
                    comment=comment,
                    decimal=decimal,

                    parse_dates=parse_dates,
                    keep_date_col=keep_date_col,
                    dayfirst=dayfirst,
                    date_parser=date_parser,

                    nrows=nrows,
                    iterator=iterator, ....
