def price_request(self, response):
    # ебануцо
    t = TakeFirst()
    magic_data = {'__ASYNCPOST': 'true'}

    # --- забираю зашитые данные из форм
    keys = [
        '__BOOKMARKERbmTabs',
        '__VIEWSTATE',
        '__VIEWSTATEGENERATOR',
        '__EVENTVALIDATION',
        'HiddenField'
    ]
    for k in keys:
        val = response.xpath('//input[contains(@id, "%s")]/@value' % k).extract()
        key = response.xpath('//input[contains(@id, "%s")]/@name' % k).extract()
        if key:
            magic_data[t(key)] = t(val) or ''

    val = response.xpath('//input[contains(@value, "btnGetPrice")]/@value').extract()
    key = response.xpath('//input[contains(@value, "btnGetPrice")]/@name').extract()
    if key:
        magic_data[t(key)] = t(val) or ''

    # --- неведомая херня из js
    # вызов получения цены
    js = response.xpath(u'//script[contains(text(), "$(document).ready(function ()")][contains(text(), "__doPostBack")]').re(
        "__doPostBack\('([^']+)','([^']*)'\)")
    # [\$\w0]+btnGetPrice
    magic_data['__EVENTTARGET'] = js[0]
    # обычно ''
    magic_data['__EVENTARGUMENT'] = js[1]

    # ключ от сервера, скорее всего он связан с сессией
    js = response.xpath(u'//script[contains(text(), "Sys.Application.setServerId")]').re('\("([^"]+)", "([^"]*)"\)')
    super_magic_key = js[1]

    # --- опять данные из формы которые туда должны при ините странице соваться
    js = response.xpath(u'//script[contains(text(), "Sys.WebForms.PageRequestManager._initialize")]').re("'form1', \[([^\]]+)\]")[0]
    super_magic_values = re.findall("'([^']+)'", js)
    super_magic_value_1 = super_magic_values[0]

    for m in super_magic_values[1:len(super_magic_values)]:
        if m:
            magic_data[m] = ''

    # хер его знает почему, но первую букву надо откусить, обычно это t
    super_magic_value1 = super_magic_value_1[1:len(super_magic_value_1)]

    # составное значение вида [\$\w0]+=[\$\w0]+$updPrice|[\$\w0]+btnGetPrice
    magic_data[super_magic_key] = super_magic_value1 + '|' + magic_data['__EVENTTARGET']

    return FormRequest(url=response.url,
                       formdata=magic_data,
                       dont_filter=True,
                       meta=response.meta,
                       callback=self.parse_price,
                       method='post',
                       headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                'X-Requested-With': 'XMLHttpRequest',
                                'X-MicrosoftAjax': 'Delta=true',
                                'Origin': 'http://www.exist.ru',
                                'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate',
                                'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-gb) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27'
                       })
