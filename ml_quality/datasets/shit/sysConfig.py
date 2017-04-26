#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Qiqiang Guan'


class SysConfig(object):

    """this is the configuration of all the Foundry companies"""
    # following technology data from Foundry companies, they are located at
    # the specified paths
    tsmc45_6 = {"lef": "/A/B/C/tsmc/45nm/6ml/physical/tech.lef /A/B/C/tsmc/45nm/6ml/physical/macro.lef",
                "lib": "/D/E/F/tsmc/45nm/6ml/fast/corner.lib /D/E/F/tsmc/45nm/6ml/fast/stdcell.lib /D/E/F/tsmc/45nm/6ml/fast/io.lib",
                "sdc": "/D/E/F/tsmc/45nm/6ml/fast/timing/tapeout.sdc",
                "drc": "/A/B/C/tsmc/45nm/6ml/drc/tapeout.drc",
                "lvs": "/A/B/C/tsmc/45nm/6ml/lvs/tapeout.lvs",
                "synthesis": "/B/G/H/tsmc/6ml/45nm/syn.teh"}

    tsmc45_7 = {"lef": "/A/B/C/tsmc/45nm/7ml/physical/tech.lef /A/B/C/tsmc/45nm/7ml/physical/macro.lef",
                "lib": "/D/E/F/tsmc/45nm/7ml/fast/corner.lib /D/E/F/tsmc/45nm/7ml/fast/stdcell.lib /D/E/F/tsmc/45nm/7ml/fast/io.lib",
                "sdc": "/D/E/F/tsmc/45nm/7ml/fast/timing/tapeout.sdc",
                "drc": "/A/B/C/tsmc/45nm/7ml/drc/tapeout.drc",
                "lvs": "/A/B/C/tsmc/45nm/7ml/lvs/tapeout.lvs",
                "synthesis": "/B/G/H/tsmc/7ml/45nm/syn.teh"}

    tsmc65_6 = {"lef": "/A/B/C/tsmc/65nm/physical/tech.lef /A/B/C/tsmc/65nm/physical/macro.lef",
                "lib": "/D/E/F/tsmc/65nm/fast/corner.lib /D/E/F/tsmc/65nm/fast/stdcell.lib /D/E/F/tsmc/65nm/fast/io.lib",
                "sdc": "/D/E/F/tsmc/65nm/fast/timing/tapeout.sdc",
                "drc": "/A/B/C/tsmc/65nm/drc/tapeout.drc",
                "lvs": "/A/B/C/tsmc/65nm/lvs/tapeout.lvs",
                "synthesis": "/B/G/H/tsmc/65nm/syn.teh"}

    umc45_6 = {"lef": "/A/B/C/umc/45nm/physical/tech.lef /A/B/C/umc/45nm/physical/macro.lef",
               "lib": "/D/E/F/umc/45nm/fast/corner.lib /D/E/F/umc/45nm/fast/stdcell.lib /D/E/F/umc/45nm/fast/io.lib",
               "sdc": "/D/E/F/umc/45nm/fast/timing/tapeout.sdc",
               "drc": "/A/B/C/umc/45nm/drc/tapeout.drc",
               "lvs": "/A/B/C/umc/45nm/lvs/tapeout.lvs",
               "synthesis": "/B/G/H/umc/45nm/syn.tec"}

    hlp = '''
OPERATION
    -t Technology (tsmc65 or umc45)
    -p Process(6m)
    -g layout_full_path [/home/design/top.gds]
    -s sch_full_path [/home/design/top.sch]
    -n top_cell_name [TOP]
    -r RTL_verilog_full_path [/home/design/top.v]
    -d DEF_full_path [/home/design/top.def]
    -v power_value [5 (volt.)]
HELP
    -h display help
CLEAR
    -c clear all the results
EXAMPLES
    ./operate.py -t tsmc65 -p 6m
    ./operate.py -t tsmc45 -p 7m -v 6v -d /home/Peter/top.def -n Peter_Top -g /home/peter/design/top.gds
    ./operate.py -t umc45 -p 6m -g /home/peter/top.gd -s /home/peter/top.sch -n NewTop -r /home/peter/top.v -d /home/peter/top.def -v 10v
'''

    # my default design data
    # def_topcell_name = 'TOP'
    # def_gds = '/home/design/top.gds'
    # def_sch = '/home/design/top.sch'
    # def_def = '/home/design/top.def'
    # def_rtl = '/home/design/top.v'
    # def_pwr = '5 (volt.)'

    def_config = {'top': 'TOP', 'gds': '/home/design/top.gds', 'sch': '/home/design/top.sch',
                  'defi': '/home/design/top.def', 'rtl': '/home/design/top.v', 'pwr': '5 (volt.)'}

    tsmc45_6 = dict(tsmc45_6.items() + def_config.items())
    tsmc45_7 = dict(tsmc45_7.items() + def_config.items())
    tsmc65_6 = dict(tsmc65_6.items() + def_config.items())
    umc45_6 = dict(umc45_6.items() + def_config.items())

if __name__ == '__main__':
    print SysConfig.tsmc45_6
    print SysConfig.umc45_6
